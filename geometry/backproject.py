'''Hàm backproject() dùng để chuyển depth map (2D) thành point cloud 3D (X, Y, Z) 
dựa trên camera intrinsics.'''


import numpy as np

def backproject(depth, fx, fy, cx, cy):
    h, w = depth.shape
    i, j = np.meshgrid(np.arange(w), np.arange(h))
    
    Z = depth
    X = (i - cx) * Z / fx
    Y = (j - cy) * Z / fy
    
    points = np.stack((X, Y, Z), axis=-1)
    return points.reshape(-1, 3)
