import cv2

from common import load_image_or_demo, save_image


def main() -> None:
    image = load_image_or_demo()

    height, width, channels = image.shape
    print(f"Image size: {width}x{height}")
    print(f"Channels: {channels}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    save_image("01_original.jpg", image)
    save_image("01_gray.jpg", gray)

    # imshow opens GUI windows. Press any key in an image window to close them.
    cv2.imshow("Original", image)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
