import cv2
import os

path = 'photos'
images = os.listdir(path)

for image in images:
    frame = cv2.imread(path + '/' + image)

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ecgClassificator = cv2.CascadeClassifier('cascade.xml')
    ecg = ecgClassificator.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=120, minSize=(500, 600))
    for (x, y, w, h) in ecg:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('prediction/' + image, frame)
    frame = cv2.resize(frame, (620, 480))

    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
