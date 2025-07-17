# Untitled-1.py

from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Run prediction
results = model("your_image.jpg")  # This returns a list

# Show first result
results[0].show()
