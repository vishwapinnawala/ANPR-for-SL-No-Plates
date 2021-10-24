import cv2
#https://rsdharra.com/blog/lesson/26.html

cap = cv2.VideoCapture(0)


car_cascade = cv2.CascadeClassifier(r"C:\Users\WUSC SRILANKA\Downloads\cars.xml")


while True:
    
    ret, frames = cap.read()
    
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale( gray, 1.1, 1)
   
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        # Display frames in a window
        cv2.imshow('Car Detection', frames)
    
    # Wait for Enter key to stop
    if cv2.waitKey(33) == 13:
        break

cv2.destroyAllWindows()