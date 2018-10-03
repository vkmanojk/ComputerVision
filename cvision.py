import numpy as np
import cv2

# pic = cv2.imread('F:\Images\School\IMG-20170328-WA0007.jpg',0)
# threshold_value = 100
# (T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary',binary_threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# pic = cv2.imread('F:\Images\School\IMG-20170328-WA0007.jpg')
# matrix = (7,7)
# blur = cv2.GaussianBlur(pic,matrix,0)
# cv2.imshow('blurred',blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pic = cv2.imread('F:\Images\School\IMG-20170328-WA0007.jpg')
cv2.imshow('orig',pic)
# kernel = 3
# median = cv2.medianBlur(pic,kernel)
# dimpixel = 7
# color = 100
# space = 100
# filter = cv2.bilateralFilter(pic,dimpixel,color,space)

thresholdval1 = 50
thresholdval2 = 100

canny = cv2.Canny(pic,thresholdval1,thresholdval2)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img = cv2.imread('F:\Images\School\IMG-20170328-WA0007.jpg')
# col = img.shape[1]
# row = img.shape[0]
#
# center = (col/2,row/2)
# m = np.float32([[1,0,150], [0,1,70]])
# angle = 90
# n = cv2.getRotationMatrix2D(center,angle,1)
# shifted = cv2.warpAffine(img,n,(col,row))
# cv2.imshow('shifted', shifted)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# pic = np.zeros((5000,5000,3), dtype='uint8')
#
# cv2.rectangle(pic, (0,0), (500,150), (123,200,98), 3, lineType=6, shift=0)
# cv2.line(pic,(350,350), (500,350), (123,245,254))
# cv2.circle(pic, (450,450), 60, (255,0,255))
# font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(pic, 'Hello World!', (50, 250), font, 2, (100, 0, 100), 4, cv2.LINE_8)
# cv2.imshow('dark',pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

