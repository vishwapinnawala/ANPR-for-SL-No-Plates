from datetime import datetime
from os import O_CREAT
startTime = datetime.now()
import cv2
import re
import numpy as np
import imutils
import easyocr
import sys
print("Import Time:",datetime.now() - startTime)

mypath=r"C:\Users\WUSC SRILANKA\Desktop\Number Plates\3.jpg"

#mypath=sys.argv[1]
#r"C:\Users\WUSC SRILANKA\Desktop\Number Plates\1.jpg"
#from matplotlib import pyplot as plt
#plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
#plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
#plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
#imgplot = plt.imshow(grayed)
#plt.show()

startTime = datetime.now()
reader = easyocr.Reader(['en'],gpu=False)
print("EasyOCR Initialize Time:",datetime.now() - startTime)

cap = cv2.VideoCapture(0)

def opencv(path):
 startTime = datetime.now()
 img = cv2.imread(path)
 
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
 bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
 edged = cv2.Canny(bfilter, 30, 200) #Edge detection
 cv2.cvtColor(edged, cv2.COLOR_BGR2RGB)
 keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 contours = imutils.grab_contours(keypoints)
 contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
 


 location = None
 for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

 mask = np.zeros(gray.shape, np.uint8)
 new_image = cv2.drawContours(mask, [location], 0,255, -1)
 new_image = cv2.bitwise_and(img, img, mask=mask)
 
 cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
 (x,y) = np.where(mask==255)
 (x1, y1) = (np.min(x), np.min(y))
 (x2, y2) = (np.max(x), np.max(y))
 cropped_image = gray[x1:x2+1, y1:y2+1]
 cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
 inverted = np.invert(cropped_image)
 cv2.imshow("asdfe",inverted)
 cv2.waitKey(0)
 print("OpenCV Time",datetime.now() - startTime)
 return cropped_image

def reading(mypath):
 startTime = datetime.now()
 result = reader.readtext(opencv(mypath))
 
 mylist=[]
 count=0

 for items in result:
    mylist.insert(count,items[1])
    count=count+1

 #result = result[0][1]
 # mylist[0]="vishwa"
 #for details in mylist:
 # print(details)
 #vish =mylist[0]+mylist[1]
 #count = mylist.count(0)
 print(count)
 print(mylist)

 s = 'dfssswsfsf212357'
 counter = 0
 temp = list(s)
 for item in temp:
    if(item.isdigit()):
        counter = counter + 1
    else:
        pass
 print (counter)
 
 #print("Result: ",result)

 joinlist=' '.join(mylist)
 print(joinlist)
 #joinlist=re.sub('#.*?', '', result)
 #print(joinlist)

 print("Read Time",datetime.now() - startTime)
 
 return result

#reading()
reading(mypath)
