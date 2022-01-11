import cv2 as cv

# #Rescaling Images

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)

def rescale_frame(frame, scale = 0.75):

    # works with photos, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img_resized = rescale_frame(img, 0.4)

# cv.imshow("Cat-resized", img_resized)

# cv.waitKey(0)

#Reading Videos

def change_res(width, height):

    # only live videos

    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow("Video Rescaled", frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

#Resizing videos