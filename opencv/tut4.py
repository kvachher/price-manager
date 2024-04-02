import cv2

cap = cv2.VideoCapture(0)

while True: 
    # returns frame as image itself, ret is bool if worked properly
    ret, frame = cap.read()
    width, height = int(cap.get(3)), int(cap.get(4))

    # drawing lines
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 0, 0), 10)

    # rectangle
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)

    # circle, filled in (indicated by -1)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Kush is the GOAT', (10, height - 10), font, 2, (255, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q') : # waits up to 1 ms or returns ascii value
        break

cap.release() # releases camera resource
cv2.destroyAllWindows()