import numpy as np
import cv2
from matplotlib import pyplot as plt
import pylab
from scipy import ndimage

video_capture = cv2.VideoCapture(0)
scale_factor = 1.3
font = cv2.FONT_HERSHEY_DUPLEX
color = (255, 255, 255)
font_black = (0, 0, 0)

while 1:
    ret, pic = video_capture.read()
    image = pic
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.png', gray_image)
    image = cv2.imread('gray_image.png')
    cv2.getGaussianKernel(9, 9)
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite('blur.png', blur)
    image = cv2.imread('blur.png')
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(image, -1, kernel)
    plt.subplot(121), plt.imshow(image), plt.title('blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('averaged')
    plt.xticks([]), plt.yticks([])
    # plt.show()
    cv2.imwrite('averaged.png', dst)
    image = cv2.imread('averaged.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imwrite('thresh_image.jpg', thresh)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    print("No. of pests in the image: ")
    labelarray, particle_count = ndimage.measurements.label(sure_bg)
    print(particle_count)
    cv2.imshow('Pest',pic)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # wait for ESC key to exit
        break
cv2.destroyAllWindows()