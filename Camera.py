import cv2


capture = cv2.VideoCapture('http://192.168.43.1:6852/video')

count = 0;

while True:

    ret,frame = capture.read()
    #cv2.imshow("Capturing",frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('Capturing',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Capturing', 1000,600)
    cv2.imshow("Capturing",frame)
    #print('Running..')
    if cv2.waitKey(1) & 0xFF == ord('2'):
        cv2.imwrite(r"C:\Users\WUSC SRILANKA\Desktop\ANPR-for-SL-No-Plates\frame.jpg", frame)
        #cv2.imwrite("frame%d.jpg" % count, frame) 

    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

    count += 1

capture.release()
cv2.destroyAllWindows()