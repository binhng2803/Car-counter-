from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture('./assets/videos/cars.mp4')
# cap.set(3, 640)
# cap.set(4, 480)
while True:
    flag, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(x1, y1, x2, y2)
            x, y, w, h = map(int, box.xywh[0])
            print(x, y, w, h)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            
    cv2.imshow('image', img)
    cv2.waitKey(1)
   