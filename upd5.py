
import cv2

# Открываем камеру (0 - первая камера, если есть несколько)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Ошибка: Не удалось открыть камеру")
    exit()

while True:
    # Захват кадра
    ret, frame = cap.read()
    if not ret:
        print("Ошибка: Не удалось получить кадр")
        break

    # Отображение кадра
    cv2.imshow("Webcam", frame)

    # Выход по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
