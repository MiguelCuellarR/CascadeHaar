import cv2
import numpy as np
import imutils
import os

datos = 'n'
if not os.path.exists(datos):
    print('carpeta creada: ', datos)
    os.makedirs(datos)

count = len(os.listdir(datos))
print(count)


def on_mouse_click(event, x, y, flags, param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:  # Detectar clic izquierdo
        cv2.imwrite(datos + '/object_{}.jpg'.format(count), object)
        print(f'Stored Image: /object_{count}.jpg')
        count += 1

cap = cv2.VideoCapture(1)

x1, y1 = 50, 110
x2, y2 = 570, 360

while True:
    ret, frame = cap.read()
    if ret == False: break

    imgAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    object = imgAux[y1:y2, x1:x2]
    object = imutils.resize(object, width=128)

    cv2.imshow('Frame', frame)
    cv2.imshow('Object', object)
    k = cv2.waitKey(1)
    if k == 27:
        break

    cv2.setMouseCallback('Frame', on_mouse_click)

cap.release()
cv2.destroyAllWindows()