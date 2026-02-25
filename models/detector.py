# Phát hiện vật thể (bounding box) trong ảnh

from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image):
        results = self.model(image)[0]
        boxes = results.boxes.xyxy.cpu().numpy()
        return boxes
