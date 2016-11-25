from shapedetector import ShapeDetector
from point import Point
import imutils
import cv2


# The region we're interested in
top_left = Point(90, 35)
lower_right = Point(430, 370)

# assume image is 600 * 400
image = cv2.imread('screen-shot.png')

region = image[top_left.y:lower_right.y, top_left.x:lower_right.x]
cv2.imshow("region", region)
cv2.waitKey(0)

gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

blurred = cv2.medianBlur(gray, 5)
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

thresh = cv2.threshold(blurred, 10, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

# find contours in the thresholded image and initialize the shape detector
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]
sd = ShapeDetector()

for contour in contours:
    # compute the center of the contour, then detect the name of the shape using only the contour
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    shape = sd.detect(contour)

    cv2.drawContours(region, [contour], -1, (0, 255, 0), 2)
    cv2.putText(region, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("image", region)
    cv2.waitKey(0)
