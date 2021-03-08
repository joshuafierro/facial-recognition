from cv2 import cv2

har_classifier_path = ''
face_cascade = cv2.CascadeClassifier(har_classifier_path)

print("Imported successfully")
cap = cv2.VideoCapture(0)
cap.set(3, 614) # width
cap.set(4, 480) # height

while True:
    sucess, feed = cap.read()
    gray = cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(feed,(x,y), (end_cord_x, end_cord_y), color, stroke)
    
    cv2.imshow("Video", feed)
    #shutdown program when video feed is in focus
    if cv2.waitKey(20) & 0xFF == ord('q'):
        print("Shutting down...")
        break
cap.release()
cv2.destroyAllWindows()