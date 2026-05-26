import cv2
import numpy as np

from common import load_image_or_demo, save_image


def main() -> None:
    image = load_image_or_demo()

    print("OpenCV stores color images as BGR, not RGB.")
    print(f"Top-left pixel BGR value: {image[0, 0].tolist()}")

    blue, green, red = cv2.split(image)

    zeros = np.zeros_like(blue)
    only_blue = cv2.merge([blue, zeros, zeros])
    only_green = cv2.merge([zeros, green, zeros])
    only_red = cv2.merge([zeros, zeros, red])

    marked = image.copy()
    h, w = marked.shape[:2]
    y1, y2 = h // 4, h // 2
    x1, x2 = w // 4, w // 2
    marked[y1:y2, x1:x2] = (0, 0, 255)

    rgb_for_matplotlib = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    save_image("02_only_blue.jpg", only_blue)
    save_image("02_only_green.jpg", only_green)
    save_image("02_only_red.jpg", only_red)
    save_image("02_marked_region.jpg", marked)
    save_image("02_rgb_converted.jpg", rgb_for_matplotlib)

    cv2.imshow("Original BGR", image)
    cv2.imshow("Marked Region", marked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
