from ultralytics import YOLO

# Load a model
model = YOLO("yolov11n.pt")

# Train the model
train_results = model.train(data="coco8.yaml", epochs=100,
                            imgsz=640, device="cpu")

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("people.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")
