import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.resize = (frame, (1020,500))
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()