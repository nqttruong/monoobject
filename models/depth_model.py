# Dự đoán depth map từ 1 ảnh RGB (monocular depth estimation)

import torch
import cv2
import numpy as np

class DepthEstimator:
    def __init__(self):
        self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
        self.model.eval()
        self.model.to("cuda")

        self.transform = torch.hub.load(
            "intel-isl/MiDaS", "transforms"
        ).small_transform

    def predict(self, image):
        input_batch = self.transform(image).to("cuda")
        with torch.no_grad():
            prediction = self.model(input_batch)
            depth = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=image.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()
        return depth.cpu().numpy()
