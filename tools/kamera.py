import torch
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
from ultralytics import YOLO
import PIL
import cv2

model = YOLO('model.pt').to('cuda')

#print(model.names)
cap = cv2.VideoCapture(0)  # 0 to domyślna kamera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Przekazanie klatki do modelu YOLO
    results = model(frame)

    for result in results:
        annotated_frame = result.plot()  # Metoda plot() zwraca klatkę z bounding boxami
        cv2.imshow('YOLO Real-Time Detection', annotated_frame)
    #jezeli 'q' to przerwij
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()