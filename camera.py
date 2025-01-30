import cv2 as r

z = r.VideoCapture(0)


while True do:
    ret, frame = z.read()
    r.imshow('Camera', frame)
    if z.waitKey(1) & 0xFF == ord('q'):
        break


