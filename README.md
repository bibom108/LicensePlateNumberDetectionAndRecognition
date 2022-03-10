# License Plate Number Detection And Recognition
Các bước giải quyết bài toán:
1. Nhận diện biển số xe có trong hình.
2. Lấy phần hình của biển số xe nhận diện được ở bước 1 và nhận diện OCR.  
3. Đóng gói kết quả trên giao diện **PYQT5**
  
Chi tiết các bước được trình bày bên dưới.

## Nhận diện biển số xe trong hình
Sử dụng **YOLOV5** để nhận diện ô tô có trong hình.  
Vì trong model trained sẵn của **YOLOV5** không có nhận diện biển số xe,
do đó ta phải tự train từ đầu. Qua tìm kiếm, ta nhận thấy data trên **Kaggle**
đã được label sẵn và tập dataset khá lớn. Do đó ta chọn dataset này để train
cho việc nhận diện biển số xe.  
  
Nhưng các file label của dataset có đuôi là **.xml**, nhưng để train được với
**YOLOV5** thì đuôi phải là **.txt**, do đó ta phải chuyển định dạng các file
label, sau đó tiến hành train.
  
Qua bước này, ta có có tập tọa độ các biển số xe có trong hình để chuyển 
sang bước tiếp theo.

## Nhận diện ký tự trên biển số xe
Trước tiên, ta phải tiền xử lý biển số xe để các ký tự được rõ ràng nhất bằng
các phép xử lý ảnh trên thư viện **OpenCV**.
  
Sau đó, ta thử qua thư viện **Tesseract OCR**, nhưng thư viện này trên dataset
cho kết quả khá kém, bên cạnh đó chưa hỗ trợ nhận diện các ký tự của Hàn Quốc, 
do đó ta sẽ thử với thư viện khác.
  
Việc thử với thư viện **EasyORC** cho kết quả khả quan hơn, bên cạnh đó thư viện
này hỗ trợ nhận diện nhiều ngôn ngữ khác nhau nếu muốn mở rộng project thành 
nhận diện cả biển số xe, tuy nhiên do nằm ngoài phạm vi của project, nên ta chỉ
lấy 4 số cuối của biển số xe.
  
Sau cùng ta vẽ bounding của biển số xe và 4 số cuối của biển số.

## Xây dựng giao diện trên PYQT5
Giao diện gồm các thành phần:
- Thay đổi level 2 hoặc 3: có thể chọn level 2 để tự vẽ bounding box kiểm tra
màu sắc.
- Button để upload ảnh.
- Button để Run/ Process/ Save.

## Tham khảo
1. Thư viện **EasyOCR**: https://github.com/JaidedAI/EasyOCR
2. Thư viện **YOLOV5**: https://github.com/ultralytics/yolov5
3. Dataset biển số xe trên **Kaggle**: https://www.kaggle.com/andrewmvd/car-plate-detection
4. Chuyển đổi định dạng **.xml** sang **.txt**: https://github.com/Isabek/XmlToTxt
