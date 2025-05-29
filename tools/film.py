import cv2
from ultralytics import YOLO

# Załaduj model
model = YOLO("model.pt")

# Parametry
input_video_path = 'in.mp4'
output_video_path = 'out.mp4'
conf_threshold = 0.6  # Próg pewności (confidence threshold)

# Otwórz wideo
cap = cv2.VideoCapture(input_video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Zapis wideo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Pętla przetwarzania
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Predykcja z filtrem
    results = model(frame, conf=conf_threshold)[0]

    # Gotowa adnotowana klatka
    annotated = results.plot()

    out.write(annotated)

# Zwolnienie zasobów
cap.release()
out.release()
cv2.destroyAllWindows()

print("Gotowe. Zapisano do:", output_video_path)
