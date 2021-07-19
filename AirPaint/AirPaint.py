import cv2
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

colors = [[80, 115, 87, 89, 255, 255]]
colorval = [[144, 226, 50]]


myPoints = []


def findColor(img, colors, colorval):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow('Image', mask)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, colorval[count], cv2.FILLED)
        if x != 0 and y != 0:
            newpoints.append([x, y, count])
        count += 1
    return newpoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, colorval[0], 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y


def drawonCanvas(myPoints, colorval):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorval[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findColor(img, colors, colorval)
    if len(newpoints) != 0:
        for newpoint in newpoints:
            myPoints.append(newpoint)
    if len(myPoints) != 0:
        drawonCanvas(myPoints, colorval)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

