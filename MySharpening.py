import cv2
import numpy as np
def mySharpening(picture):

    laplacian =[[-1,-1, -1], [-1, 9, -1], [-1, -1, -1]]
    lfilter=np.zeros((int(picture.shape[0]),int(picture.shape[1]),1),np.uint8)
    filtered=np.zeros((int(picture.shape[0])*int(picture.shape[1]),1),'int32')
    counter=0
    maks=0
    mini=0
    x=int(picture.shape[0])
    y=int(picture.shape[1])
    for i in range(1,x-2,1):
        for j in range(1,y-2,1):
            filtered[counter]=laplacian[0][0]*picture[i-1][j-1] + laplacian[0][1]*picture[i-1][j+0] + \
                 laplacian[0][2]*picture[i-1][j+1] + laplacian[1][0]*picture[i+0][j-1] + \
                      laplacian[1][1]*picture[i+0][j+0] + laplacian[1][2]*picture[i+0][j+1] + \
                           laplacian[2][0]*picture[i+1][j-1] + laplacian[2][1]*picture[i+1][j+0] + \
                                laplacian[2][2]*picture[i+1][j+1]

            if (filtered[counter] > 255):
                maks = filtered[counter]
                filtered[counter]=255
            if (filtered[counter] < 0):
                mini = filtered[counter]
                filtered[counter]=0
            lfilter[i][j]=filtered[counter]
            counter=counter+1
    print(maks, mini)
    cv2.imwrite("deneme.png",lfilter)
    cv2.imshow('Final Version', lfilter)
    return lfilter

picture = cv2.imread("picture.png",0) 
cv2.imshow("First Version",picture)
img=cv2.imread("denem.png",0)
mySharpening(picture)
mySharpening(img)    
cv2.waitKey()
