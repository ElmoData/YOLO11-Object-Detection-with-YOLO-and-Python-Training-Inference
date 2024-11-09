# YOLO11-Object-Detection-with-Python-Training-Inference
This repository demonstrates object detection using YOLOv8 and Python, covering the essential steps from training a model on a custom COCO dataset to evaluating its performance and running object detection on sample images. The trained model is also exported in ONNX format, making it ready for flexible deployment across various platforms.

## Features
- Model Training: Train a YOLOv8 model on a custom dataset.
- Performance Evaluation: Evaluate the trained model’s performance.
- Object Detection: Perform object detection on sample images.
- Export Model: Export the trained model in ONNX format for compatibility with other frameworks.

## Getting Started
### Prerequisites
- Python 3.x
- ultralytics library (for YOLOv8)
- Necessary dependencies for training and exporting models

Install the required packages:
-pip install ultralytics-

### Usage
1. Load a Pretrained Model:
   -from ultralytics import YOLO-
   -model = YOLO("yolov11n.pt")-
2. Train the Model: Train the model on a custom COCO dataset.
   -train_results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device="cpu")-
3. Evaluate Model Performance: Evaluate the model’s accuracy on a validation set.
   -metrics = model.val()-
4. Run Object Detection on a Sample Image: Use the trained model to detect objects in an image.
   -results = model("people.jpg")-
   -results[0].show()-
5. Export the Model: Export the model in ONNX format for flexible deployment.
   -path = model.export(format="onnx")-

### Example
Run the script to train the model and test it on sample images. Export the model once training is complete to use it in other frameworks that support ONNX.
