''' File này dùng để hiệu chỉnh (scale calibration) giá trị khoảng cách 
dự đoán từ model sao cho khớp với khoảng cách thực (ground truth).
'''

import numpy as np

class ScaleCalibrator:
    def __init__(self):

        # dtrue​=alpha x d(pred)+β

        self.alpha = 1.0
        self.beta = 0.0

    def fit(self, pred, gt):
        
        # Tìm alpha, beta
        
        pred = np.array(pred)
        gt = np.array(gt)
        A = np.vstack([pred, np.ones(len(pred))]).T
        self.alpha, self.beta = np.linalg.lstsq(A, gt, rcond=None)[0]

    def apply(self, d):
        return self.alpha * d + self.beta
