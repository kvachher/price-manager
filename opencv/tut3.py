import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True: 
    # returns frame as image itself, ret is bool if worked properly
    ret, frame = cap.read()
    width, height = int(cap.get(3)), int(cap.get(4))

    img = np.zeros(frame.shape, np.uint8) # creating empty numpy array of same shape as frame
    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5) # resizes to 1/4 screen
    img[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    img[height//2:, :width//2] = smaller_frame
    img[height//2:, width//2:] = smaller_frame
    img[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q') : # waits up to 1 ms or returns ascii value
        break

cap.release() # releases camera resource
cv2.destroyAllWindows()