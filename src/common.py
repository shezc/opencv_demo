from pathlib import Path

import cv2
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "assets"
OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_IMAGE_PATH = ASSETS_DIR / "sample.jpg"


def ensure_output_dir() -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    return OUTPUT_DIR


def create_demo_image() -> np.ndarray:
    """Create a simple BGR image when assets/sample.jpg is not available."""
    image = np.full((420, 640, 3), 245, dtype=np.uint8)

    cv2.rectangle(image, (60, 80), (260, 260), (30, 144, 255), thickness=-1)
    cv2.circle(image, (430, 170), 90, (80, 200, 120), thickness=-1)
    cv2.line(image, (80, 340), (560, 320), (180, 70, 220), thickness=8)
    cv2.putText(
        image,
        "OpenCV",
        (230, 370),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.6,
        (40, 40, 40),
        4,
        cv2.LINE_AA,
    )

    return image


def load_image_or_demo(path: Path = DEFAULT_IMAGE_PATH) -> np.ndarray:
    image = cv2.imread(str(path))
    if image is not None:
        print(f"Loaded image: {path}")
        return image

    print(f"Image not found: {path}")
    print("Using a generated demo image instead.")
    return create_demo_image()


def save_image(name: str, image: np.ndarray) -> Path:
    output_path = ensure_output_dir() / name
    cv2.imwrite(str(output_path), image)
    print(f"Saved: {output_path}")
    return output_path
