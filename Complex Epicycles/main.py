import numpy as np 
import matplotlib.pyplot as plt  
from matplotlib import animation,rc
import cv2
import epicycles
MAX_N = 50
pts = []
drawing = False
pt1_x , pt1_y = None , None

def line_drawing(event,x,y,flags,param):
    global pt1_x,pt1_y,drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        pt1_x,pt1_y=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(img,(pt1_x,pt1_y),(x,y),color=(255,255,255),thickness=3)
            pt1_x,pt1_y=x,y
            pts.append([(x-256)/25.6,-(y-256)/25.6])
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.line(img,(pt1_x,pt1_y),(x,y),color=(255,255,255),thickness=3)        

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Fourier Epicycles')
cv2.setMouseCallback('Fourier Epicycles',line_drawing)

while(1):
    cv2.imshow('Fourier Epicycles',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

pts = np.array(pts).T

#plot
epicycles.epicycle(x=pts[0],y=pts[1],precise=MAX_N)