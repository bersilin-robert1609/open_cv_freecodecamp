import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Boston", img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow("translated", translated)

# Rotation

def rotate(img, angle, rotation_pnt = None):
    (height, width) = img.shape[:2]

    if rotation_pnt is None:
        rotation_pnt = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotation_pnt, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow("Rotated Rotated", rotated_rotated)

# resizing

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# flipping

flip = cv.flip(img, -1)
cv.imshow("flip", flip)

#cropping

cropped = img[200:300, 300:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)