import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow('Boston', img)

# Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image

dilated  = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("dilated", dilated)

# eroding

eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("erode", eroded)

# Resize

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resized)

# Cropping

cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv. waitKey(0)