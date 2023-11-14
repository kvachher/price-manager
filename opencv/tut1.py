import cv2

# modes -> imread_color (-1), imread_grayscale (0), imread_unchanged (1)
img = cv2.imread('/Users/kushvachher/personalworkspace/price-manager/opencv/assets/s-l1600.jpeg', 1)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5) # resize
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate

cv2.imwrite('new_logo.jpeg', img) # writes an image to a new file

cv2.imshow('knicks-logo', img)
cv2.waitKey(0) # waits an infinite amount of time
cv2.destroyAllWindows()