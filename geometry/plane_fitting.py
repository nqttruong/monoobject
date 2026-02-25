# Ước lượng mặt phẳng (plane fitting) từ point cloud 3D bằng RANSAC

import numpy as np
from sklearn.linear_model import RANSACRegressor

def fit_plane_ransac(points):
    X = points[:, :2]
    y = points[:, 2]

    ransac = RANSACRegressor()
    ransac.fit(X, y)

    a, b = ransac.estimator_.coef_
    d = ransac.estimator_.intercept_

    # Plane: aX + bY - Z + d = 0
    normal = np.array([a, b, -1.0])

    norm = np.linalg.norm(normal)
    normal = normal / norm
    d = d / norm  # ⚠️ QUAN TRỌNG

    return normal, d
