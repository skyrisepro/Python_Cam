import cv2 as r

z = r.VideoCapture(0)
x = while True:


x
    ret, frame = z.read()
    r.imshow('Camera', frame)
    if z.waitKey(1) & 0xFF == ord('q'):
        break


