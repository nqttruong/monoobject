# cấu hình (global config) của toàn bộ pipeline

import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Camera intrinsics example (test theo chuẩn KITTI.)
FX = 721.5
FY = 721.5
CX = 609.5
CY = 172.8

# ngưỡng sai số (inlier threshold)
RANSAC_THRESH = 0.2

# số lần lặp của RANSAC 
RANSAC_ITER = 10000000
