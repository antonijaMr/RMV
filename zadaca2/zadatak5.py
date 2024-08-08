import tensorflow as tf
import cv2
import numpy as np

# Učitaj TensorFlow YOLO model
model = tf.saved_model.load("yolov3_saved_model")

# Preuzmi funkciju za detekciju iz modela
infer = model.signatures['serving_default']

# Učitaj klase
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Učitaj sliku
image = cv2.imread("input.jpg")
height, width, _ = image.shape

# Pripremi sliku za model
blob = cv2.resize(image, (416, 416))
blob = blob / 255.0
blob = np.expand_dims(blob, axis=0).astype(np.float32)

# Izvrši detekciju
input_tensor = tf.convert_to_tensor(blob)
output = infer(input_tensor)

# Procesiraj rezultate
boxes = output['yolo_boxes'].numpy()[0]
scores = output['yolo_scores'].numpy()[0]
class_ids = output['yolo_classes'].numpy()[0]

# Filteriraj rezultate
confidence_threshold = 0.5
indices = np.where(scores > confidence_threshold)

for i in indices[0]:
    box = boxes[i]
    class_id = int(class_ids[i])
    confidence = scores[i]
    
    # Preračunaj koordinate u originalnoj slici
    x_center, y_center, w, h = box
    x = int((x_center - w / 2) * width)
    y = int((y_center - h / 2) * height)
    w = int(w * width)
    h = int(h * height)
    
    label = str(classes[class_id])
    color = (0, 255, 0)  # Zelena boja za pravougaonike
    
    # Nacrtaj pravougaonike i tekst na slici
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Prikazi sliku sa detekcijama
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
