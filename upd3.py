import cv2

z = cv2.VideoCapture(0)


while True:
    ret, frame = z.read()
    cv2.imshow('Camera', frame)
    if z.waitKey(1) & 0xFF == ord('q'):
        break

