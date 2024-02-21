import cv2

image = cv2.imread("pbl pic 3.jpeg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

cv2.waitKey(0)