import cv2
import numpy as np
import imutils
import easyocr
#mypath=r"C:\Users\WUSC SRILANKA\Desktop\ANPR-for-SL-No-Plates\1.jpg"
reader = easyocr.Reader(['en'],gpu=False)#Initializing OCR Engine

while True:

  def opencv():
    capture = cv2.VideoCapture('http://192.168.43.1:6852/video')
    #cv2.waitKey(2000) 
    ret,frame = capture.read()
    #img = cv2.imread(frameinput)
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#BGRTOGRAY
    cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)#BGRTORGB
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #CannyEdge detection

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#Finding contours
    #cv2.imshow("Contours",keypoints)
    #cv2.waitkey(0)
    print(keypoints)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
 
    location = None
    for items in contours:
       approx = cv2.approxPolyDP(items, 10, True)
       if len(approx) == 4:
          location = approx
          break

    mask = np.zeros(gray.shape, np.uint8)#mask
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
 
 
    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]#Cropped image
    inverted = np.invert(cropped_image)#Inverting the image
    cv2.imshow("Inverted",inverted)#Displaying Inverted
    cv2.waitKey(5000)
    return cropped_image

    #OCR Part
  def reading():
    result = reader.readtext(opencv())#Calling OpenCV function
 
    mylist=[]
    count=0

    for items in result:
       mylist.insert(count,items[1])#inserting item[1] in list to mylist
       count=count+1 #Counting Items in list

    print("Count: ",count)#how many Segmented Text
    #print(mylist)


    joinlist=' '.join(mylist)#Joining the (mylist)list items together
    print(joinlist)

 
    return joinlist
   
  if cv2.waitKey(1) & 0xFF == ord('1'):
       break

cv2.waitKey(5000)
reading()
   
