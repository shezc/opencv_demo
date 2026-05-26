import cv2

from common import load_image_or_demo, save_image


def main() -> None:
    image = load_image_or_demo()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    print(f"Found contours: {len(contours)}")

    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 0, 255), 3)

    for index, contour in enumerate(contours, start=1):
        area = cv2.contourArea(contour)
        if area < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            result,
            str(index),
            (x, max(20, y - 8)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2,
            cv2.LINE_AA,
        )

    save_image("04_threshold.jpg", threshold)
    save_image("04_contours.jpg", result)

    cv2.imshow("Threshold", threshold)
    cv2.imshow("Contours", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
