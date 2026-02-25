# Làm mượt (stabilize) vector pháp tuyến mặt phẳng theo thời gian
# Xử lý realtime 

import numpy as np

class PlaneStabilizer:
    def __init__(self, alpha=0.9):
        self.alpha = alpha
        self.prev_normal = None

    def update(self, normal):
        if self.prev_normal is None:
            self.prev_normal = normal
        else:
            normal = self.alpha * self.prev_normal + (1 - self.alpha) * normal
            normal = normal / np.linalg.norm(normal)
            self.prev_normal = normal
        return normal
