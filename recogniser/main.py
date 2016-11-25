from point import Point
import imutils
import cv2


def threshold_image(region):
    cv2.imshow("region", region)
    cv2.waitKey(0)

    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)

    blurred = cv2.medianBlur(gray, 5)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("blurred", blurred)
    cv2.waitKey(0)

    thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)

    return thresh


def detect_shape(contour):
    # Get the (outer) length of the contour
    curve_length = cv2.arcLength(contour, True)

    if curve_length < 100:
        # Ignore small shapes which are likely light reflections, or regions from the side of the image
        return None

    approx_poly = cv2.approxPolyDP(contour, 0.04 * curve_length, True)

    if len(approx_poly) != 4:
        # For now, we're only interested in squares and rectangles
        return None

    # Get the bounding box of the contour and use the bounding box to compute the aspect ratio
    (x, y, w, h) = cv2.boundingRect(approx_poly)
    ratio = w / float(h)

    return "square" if 0.95 <= ratio <= 1.05 else "rectangle"


def main():
    image = cv2.imread('screen-shot.png')

    top_left = Point(100, 35)
    lower_right = Point(430, 370)

    region = image[top_left.y:lower_right.y, top_left.x:lower_right.x]
    thresholded = threshold_image(region)

    # find contours in the thresholded image and initialize the shape detector
    contours = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]

    for contour in contours:
        try:
            # compute the center of the contour, then detect the name of the shape using only the contour
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            shape = detect_shape(contour)

            if shape is not None:
                cv2.drawContours(region, [contour], -1, (0, 255, 0), 2)
                cv2.putText(region, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                cv2.imshow("image", region)
                cv2.waitKey(0)

        except Exception:
            pass


if __name__ == "__main__":
    main()
