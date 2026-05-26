import cv2

from common import load_image_or_demo, save_image


def main() -> None:
    image = load_image_or_demo()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges_low = cv2.Canny(blurred, 50, 150)
    edges_high = cv2.Canny(blurred, 100, 220)

    save_image("03_gray.jpg", gray)
    save_image("03_blurred.jpg", blurred)
    save_image("03_edges_low_threshold.jpg", edges_low)
    save_image("03_edges_high_threshold.jpg", edges_high)

    cv2.imshow("Gray", gray)
    cv2.imshow("Blurred", blurred)
    cv2.imshow("Canny Edges", edges_low)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
