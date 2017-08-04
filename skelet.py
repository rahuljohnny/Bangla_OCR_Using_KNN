
#-------------------------------------------------------------------------------
# Name : skeleton.py

# 1)Blur with gaussian function
# 2)Threshold with otsus binariasation
# 3)Inverted the image so that white is forground and black is back ground
# 4) Then used  morphological functions erode and dilate continuosly until
#    the very narrow skeleton was obtained
#-------------------------------------------------------------------------------
import cv2
import numpy as np

#def skele(img):


img = cv2.imread('s.jpg', 0)
h = img[0]
w = img[1]


cv2.imshow("b4 skele",img)
cv2.waitKey(0)


size=np.size(img)
skel=np.zeros(img.shape,np.uint8)

blur= cv2.GaussianBlur(img,(5,5),0)
ret,thrs=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
inv=cv2.bitwise_not(thrs)

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
done = False

while( not done):
 eroded = cv2.erode(inv,element)
 temp = cv2.dilate(eroded,element)
 temp = cv2.subtract(inv,temp)
 skel = cv2.bitwise_or(skel,temp)
 inv = eroded.copy()

 zeros = size - cv2.countNonZero(inv)
 if zeros==size:
    done = True


cv2.imshow("skele",skel)
cv2.waitKey(0)

