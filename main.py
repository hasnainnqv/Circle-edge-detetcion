from turtle import circle
import cv2 as c
import numpy as np

img= c.imread("smarties.png")
outp=img.copy()
gray= c.cvtColor(img,c.COLOR_BGR2GRAY)
gray=c.medianBlur(gray,5)




cicles=c.HoughCircles(gray,c.HOUGH_GRADIENT,1,20,param1=50,param2=40,minRadius=0,maxRadius=0)

detected_cir=np.uint16(np.around(cicles))
for x,y,r in detected_cir[0,:]:
    c.circle(outp,(x,y),r,(0,0,0),3)
    c.circle(outp,(x,y),2,(0,0,0),3)
    # print(x,y,r)

c.imshow('output',outp)
c.waitKey(0)
c.destroyAllWindows()
