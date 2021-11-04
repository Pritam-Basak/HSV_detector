import cv2 as cv
from matplotlib import pyplot
import numpy as np

cap = cv.VideoCapture(0)

def empty(x):
    pass

cv.namedWindow("track")
cv.createTrackbar("Hue min: ","track",0,179,empty)
cv.createTrackbar("Hue max: ","track",179,179,empty)
cv.createTrackbar("Sat min: ","track",0,255,empty)
cv.createTrackbar("Sat max: ","track",255,255,empty)
cv.createTrackbar("Val min: ","track",0,255,empty)
cv.createTrackbar("Val max: ","track",255,255,empty)


while True:
    _,frame = cap.read()
    frame = cv.resize(frame,(720,480))
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue min: ","track")
    h_max = cv.getTrackbarPos("Hue max: ","track")
    s_min = cv.getTrackbarPos("Sat min: ","track")
    s_max = cv.getTrackbarPos("Sat max: ","track")
    v_min = cv.getTrackbarPos("Val min: ","track")
    v_max = cv.getTrackbarPos("Val max: ","track")

    l_hsv = np.array([h_min,s_min,v_min])
    h_hsv = np.array([h_max,s_max,v_max])
    mask = cv.inRange(hsv,l_hsv,h_hsv)
    res = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("frame",frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if cv.waitKey(1) & 0xFF == ord('s'):
        print(h_max,h_min,s_max,s_min,v_max,v_min)
cv.destroyAllWindows()
cap.release()