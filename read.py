import cv2 as cv

#Reading Images

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

#Reading Videos

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if isTrue:
        if cv.waitKey(20) and 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
