import cv2
from ultralytics import YOLO
import os
import time

# Load trained model
model = YOLO("runs/detect/Fire_detector3/weights/best.pt")

# Save path
save_path = "/Users/kundanrajsingh/Library/CloudStorage/GoogleDrive-kundansingh.iitm@gmail.com/My Drive/model_images_snapshot3/"
os.makedirs(save_path, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture("http://10.254.208.202:8080/video")

last_save = 0
cooldown = 5   # seconds between saves

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Run prediction
    results = model(frame, conf=0.4)

    fire_detected = False

    for r in results:
        for box in r.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            label = model.names[cls]

            # Draw bounding box
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

            text = f"{label} {conf:.2f}"
            cv2.putText(frame,text,(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

            if label == "fire":
                fire_detected = True

    # Save image when fire detected
    if fire_detected and (time.time() - last_save > cooldown):

        filename = os.path.join(save_path, f"fire_{int(time.time())}.jpg")

        cv2.imwrite(filename, frame)

        print("🔥 Fire detected! Saved:", filename)

        last_save = time.time()

    cv2.imshow("Fire Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()