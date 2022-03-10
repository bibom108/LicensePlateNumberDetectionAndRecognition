import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from collections import Counter
import torch
import easyocr

cor = []

def drawBox(x1, y1, x2, y2, text, img):
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (36,255,12), 2)
    img = cv2.putText(img, text, (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2, cv2.LINE_AA)

def getNumber(cur):
    gray = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.medianBlur(gray, 3)

    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    dilation = cv2.dilate(thresh, rect_kern, iterations=1)
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(dilation)
    text = ''
    for detection in result:
        text += detection[-2]
    return text

def mainFunc(img_path):
    # FILE
    global car
    img = cv2.imread(img_path)

    # GET COR BY YOLOV5
    model_yolov = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    results = model_yolov(img)
    results = results.pandas().xyxy[0].to_numpy()
    for x in results:
        cor.append([int(x[0]), int(x[1]), int(x[2]), int(x[3])])

    # GET NUMBER
    for x in cor:
        tmp = img[x[1]:x[3], x[0]:x[2]]
        text = getNumber(tmp)
        if text == '':
            continue
        text = (''.join(c for c in text if c.isdigit()))[-4:]
        print(text)
        drawBox(x[0], x[1], x[2], x[3], text, img)
    return img