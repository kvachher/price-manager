import cv2
import random

img = cv2.imread('/Users/kushvachher/personalworkspace/price-manager/opencv/assets/s-l1600.jpeg', -1)


# code changes pixels in the image
for i in range(100) : 
    for j in range(img.shape[1]) : # shape -> (rows, cols, channels)
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# copy and pastes one part of an image to another using numpy slice
tag = img[300:500, 600:900]
img[100:300, 100:400] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()