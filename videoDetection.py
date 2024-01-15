import os
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
ecgClassificator = cv2.CascadeClassifier('classifier/cascade.xml')

data = 'prediction'
if not os.path.exists(data):
    print('folder created: ', data)
    os.makedirs(data)

count = len(os.listdir(data))
print(count)


def on_mouse_click(event, x, y, flags, param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:  # Detectar clic izquierdo
        cv2.imwrite(data + '/prediction_{}.jpg'.format(count), object)
        print(f'Stored Image: /prediction_{count}.jpg')
        count += 1


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ecg = ecgClassificator.detectMultiScale(gray, scaleFactor=2.1, minNeighbors=70, minSize=(120, 200))
    
    for (x, y, w, h) in ecg:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'ECG', (x, y-10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    object = np.copy(frame)
    cv2.imshow('Frame', frame)
    cv2.setMouseCallback('Frame', on_mouse_click)
    if cv2.waitKey(1) == 27:
        break
            
cap.release()
cv2.destroyAllWindows()
