import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import time

# SET CAMERA
cap = cv2.VideoCapture(2)
cap.set(6, 640) # set chiều rộng
cap.set(8, 480) # set chiều cao

scanned_data = []
print("Bắt đầu quét... Đưa mã QR vào trước camera.")

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Không thể truy cập camera, tùy chỉnh thông số dòng 7 trong code (= 0,1,2,3,...)")
            break

        # DECODE
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')

            if myData not in scanned_data:
                scanned_data.append(myData)
                print(f"Đã quét: {myData}")
                time.sleep(0.5)

        cv2.imshow('Camera QR Scanner', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

    if scanned_data:
        df = pd.DataFrame(scanned_data, columns=['Scanned_Data'])
        df.to_csv('qr_scanned_data.csv', index=False)
        print(f"\nĐã lưu {len(scanned_data)} mã QR vào file qr_scanned_data.csv")
    else:
        print("\nKhông có dữ liệu nào được quét để lưu.")