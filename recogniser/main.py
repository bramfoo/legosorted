from point import Point
from lego_block import LegoBlock
import imutils
import cv2
import glob

debug = True


def display(title, image):
    if debug:
        cv2.imshow(title, image)
        cv2.waitKey(0)


def threshold_image(region):
    display("region", region)

    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    display("gray", gray)

    blurred = cv2.medianBlur(gray, 5)
    display("blurred", blurred)

    thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)[1]
    display("thresh", thresh)

    return thresh


def detect_shape(contour):
    # Get the (outer) length of the contour
    curve_length = cv2.arcLength(contour, True)

    if curve_length < 100:
        # Ignore small shapes which are likely light reflections, or regions from the side of the image
        return None

    approximated_poly = cv2.approxPolyDP(contour, 0.04 * curve_length, True)

    if len(approximated_poly) != 4:
        # For now, we're only interested in squares and rectangles
        return None

    return LegoBlock(approximated_poly)  # "square" if 0.95 <= ratio <= 1.05 else "rectangle"


def find_single_block(file_name, top_left, lower_right):
    image = cv2.imread(file_name)
    region = image[top_left.y:lower_right.y, top_left.x:lower_right.x]
    thresholded = threshold_image(region)

    # Find contours in the thresholded image and initialize the shape detector
    contours = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]
    lego_blocks = []

    for contour in contours:
        try:
            shape = detect_shape(contour)
            if shape is not None:
                lego_blocks.append(shape)
        except Exception:
            # Ignore this, most likely a contour from
            pass

    if len(lego_blocks) > 1:
        raise Exception('more than 1 block detected in ' + file_name)
    elif len(lego_blocks) < 1:
        raise Exception('no block detected in ' + file_name)

    return lego_blocks[0]


def main():
    top_left = Point(110, 45)
    lower_right = Point(430, 340)

    # TODO create the image and feed it to find_single_block()

    for f in glob.glob("*.png"):
        try:
            lego_block = find_single_block(f, top_left, lower_right)
            print str(lego_block)
        except Exception as e:
            print "%s" % e


if __name__ == "__main__":
    main()
