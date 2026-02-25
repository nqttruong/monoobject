import cv2
import numpy as np
import argparse

from config import *
from models.detector import ObjectDetector
from models.depth_model import DepthEstimator
from geometry.backproject import backproject
from geometry.plane_fitting import fit_plane_ransac
from geometry.ray_plane import ray_plane_intersection
from geometry.stabilization import PlaneStabilizer


def process_frame(frame, detector, depth_model, stabilizer):
    boxes = detector.detect(frame)
    depth = depth_model.predict(frame)

    points = backproject(depth, FX, FY, CX, CY)
    normal, d = fit_plane_ransac(points)
    normal = stabilizer.update(normal)

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)

        foot_x = int((x1 + x2) / 2)
        foot_y = int(y2)

        ray = np.array([
            (foot_x - CX) / FX,
            (foot_y - CY) / FY,
            1.0
        ])

        distance = ray_plane_intersection(ray, normal, d)

        # Vẽ box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Hiển thị khoảng cách
        cv2.putText(
            frame,
            f"{distance:.2f} cm",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

        print("Distance:", distance)

    return frame


def run_image(image_path):
    detector = ObjectDetector()
    depth_model = DepthEstimator()
    stabilizer = PlaneStabilizer()

    image = cv2.imread(image_path)
    if image is None:
        print("❌ Không đọc được ảnh")
        return

    result = process_frame(image, detector, depth_model, stabilizer)

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run_camera(source=0):
    detector = ObjectDetector()
    depth_model = DepthEstimator()
    stabilizer = PlaneStabilizer()

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("❌ Không mở được camera/video")
        return

    print("✅ Nhấn Q để thoát")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = process_frame(frame, detector, depth_model, stabilizer)

        cv2.imshow("Monocular Ground Distance", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, help="Path to image")
    parser.add_argument("--video", type=str, help="Path to video file")
    parser.add_argument("--webcam", action="store_true", help="Use webcam")

    args = parser.parse_args()

    if args.image:
        run_image(args.image)
    elif args.video:
        run_camera(args.video)
    elif args.webcam:
        run_camera(0)
    else:
        print("⚠️ Vui lòng chọn --image hoặc --video hoặc --webcam")