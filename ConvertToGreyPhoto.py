import cv2
import numpy as np

pictures=cv2.imread("picture.png",0) # read and assing real picture from folder
cv2.imshow("Midterm photo",pictures) # Display function of new photo on screen
cv2.imwrite("picturegray.png",pictures) # write and save new photo to folder

cv2.waitKey(0) 
cv2.destroyAllWindows() 
