             ┌───────────────┐
             │  Video Frame  │
             └──────┬────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
   ┌────▼────┐              ┌───▼─────┐
   │  YOLO   │              │ MiDaS   │
   │ Detect  │              │ Depth   │
   └────┬────┘              └───┬─────┘
        │                       │
        │                   Relative Depth
        │                       │
        │                Scale Calibration
        │                       │
        │                 Backprojection (2D -> 3D)
        │                       │
        │                 3D Point Cloud
        │                       │
        │                RANSAC Plane Fit
        │                       │
        │              Plane Stabilization
        │                       │
        └──────────────┬────────┘
                       │
               Ray Construction
                       │
             Ray-Plane Intersection
                       │
                 Object Distance
                       │
                MAE / RMSE Eval



                Video Frame
                    ↓
                ObjectDetector (YOLOv8)
                    ↓
                Bounding Boxes
                    ↓
                DepthEstimator (MiDaS)
                    ↓
                Relative Depth
                    ↓
                ScaleCalibrator
                    ↓
                Metric Depth
                    ↓
                Backproject (FX, FY, CX, CY)
                    ↓
                3D Point Cloud
                    ↓
                RANSAC Plane Fit
                    ↓
                PlaneStabilizer
                    ↓
                For each bounding box:
                    ↓
                    Ray direction from pixel center
                    ↓
                    Ray-Plane Intersection
                    ↓
                    Object Distance (meters)
                    ↓
                MAE / RMSE Evaluation