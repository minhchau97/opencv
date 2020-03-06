
import cv2
import numpy as np

img = cv2.imread('gradient.png')
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # ngưỡng ảnh binary chỉ 0 và 1 trắng và đen
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) # ngưỡng ảnh binary đảo
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # cắt ngắn ngưỡng 1
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # tăng cường ngưỡng 1 và giảm thiểu ngưỡng 0
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) # giảm mức 1 giữ mức 0
cv2.imshow('Thesh_Ogriginal',img)
cv2.imshow('Thesh_Binary',th1)
cv2.imshow('Thesh_Binary_IVT',th2)
cv2.imshow('Thesh_Trunc',th3)
cv2.imshow('Thesh_To_Zero',th4)
cv2.imshow('Thesh_To_Zero_IVT',th5)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ADAPTIVE_THRESH_


import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2); # thay đổi ngưỡng
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2); # làm mờ

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()
