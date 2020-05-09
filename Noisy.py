import cv2
img = cv2.imread('Task.png',0) # Load image
img_median = cv2.medianBlur(img, 5) # Add median filter to image
cv2.imshow('img', img_median) # Display img with median filter
cv2.imwrite("median.png",img_median)
cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.

#################################
import numpy as np 
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread('median.png',0) 
dst = cv2.fastNlMeansDenoising(img,None,9,13)
cv2.imshow("ilk",img)
cv2.imshow("son",dst)
cv2.imwrite("noisy1.png",dst)
plt.subplot(121), plt.imshow(img) 
plt.subplot(122), plt.imshow(dst) 
plt.show() 
cv2.waitKey()
#################################
import cv2
import numpy as np
img = cv2.imread('noisy1.png',0)
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) #side by side comparison
cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows
#################################
