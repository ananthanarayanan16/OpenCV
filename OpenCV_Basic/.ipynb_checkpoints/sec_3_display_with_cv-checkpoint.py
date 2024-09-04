# DISPLAY IMAGE WITH OPENCV LIBRARY

import cv2

img = cv2.imread('/home/srijanani/GIT/OpenCV/Images/puppy.jpeg')

while True:
    
    cv2.imshow('Puppy', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()