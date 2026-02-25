# Khoảng cách từ camera đến điểm giao giữa một tia (ray) và mặt phẳng

import numpy as np

def ray_plane_intersection(ray_dir, plane_normal, plane_d):
    numerator = -plane_d
    denominator = np.dot(plane_normal, ray_dir)
    t = numerator / denominator
    point = t * ray_dir
    return np.linalg.norm(point)


# def ray_plane_intersection(ray_dir, plane_normal, plane_d):
#     denom = np.dot(plane_normal, ray_dir)

#     if abs(denom) < 1e-6:
#         return None  # ray song song plane

#     t = -plane_d / denom

#     if t < 0:
#         return None  # giao phía sau camera

#     point = t * ray_dir
#     return np.linalg.norm(point)