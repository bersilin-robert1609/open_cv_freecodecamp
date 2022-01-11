import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')
cv.imshow("Blank Image", blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", mask)

mask2 = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+100, img.shape[0]//2+100), 255, -1)
cv.imshow("mask2", mask2)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked", masked)

masked2 = cv.bitwise_and(img, img, mask = mask2)
cv.imshow("Masked2", masked2)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

weird_shape = cv.bitwise_and(rectangle, circle)
cv.imshow("Weird shape", weird_shape)

masked3 = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow("Masked3", masked3)

cv.waitKey(0)
