import numpy as np

def mae(pred, gt):
    return np.mean(np.abs(np.array(pred) - np.array(gt)))

def rmse(pred, gt):
    return np.sqrt(np.mean((np.array(pred) - np.array(gt))**2))
