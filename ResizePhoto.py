import cv2
import numpy as np

def resizeToQuarter(resizedpicture,pictures):
    i=-1
    j=-1
    for num0 in range (0,int((pictures.shape[0]))-1,2):
        j=-1
        i=i+1
        for num1 in range(0,int((pictures.shape[1]))-1,2):
            j=j+1 
            resizedpicture[(i,j)]=(pictures[(num0,num1)])/4+\
                (pictures[(num0+1,num1)])/4+(pictures[(num0,num1+1)])/4+(pictures[(num0+1,num1+1)])/4
    cv2.imshow("Resized picture", resizedpicture)
    cv2.imwrite("Resized picture.png",resizedpicture)
    print("Pictures",pictures.shape[0],"*",pictures.shape[1],"=",pictures.shape[0]*pictures.shape[1],'Pixels')
    print("Resized picture",resizedpicture.shape[0],'*',resizedpicture.shape[1],"=",resizedpicture.shape[0]*resizedpicture.shape[1],'Pixels')

pictures=cv2.imread("picture.png",0)
cv2.imshow("Midterm photo",pictures)
cv2.imwrite("picturegray.png",pictures)

resizedpicture=np.zeros((int((pictures.shape[0])/2),int((pictures.shape[1])/2),1),np.uint8)
resizeToQuarter(resizedpicture,pictures)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
