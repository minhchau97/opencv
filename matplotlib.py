import cv2 as cv
# import pyplot từ thư viện matplotlib
from matplotlib import pyplot as plt

# tạo các hình ảnh bao gồm hình ảnh góc và hình ảnh ngưỡng màu
img = cv.imread('gradient.png',0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# tạo ra các tiêu đề và mảng hình ảnh
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]

# tạo ra một vòng lặp chứa mảng hình ảnh và mảng tiêu đề
for i in range(6) :
    plt.subplot(3, 2, i+1) # tạo ra 3 hàng và mỗi hàng có 2 hình
    plt.imshow(images[i], 'gray') # hiện các hình ảnh theo mảng
    plt.title(titles[i]) # tạo các tiêu đề cửa sổ
    plt.xticks([]),plt.yticks([]) # ẩn đi các đồ thị x và y
plt.show() # hiển thị tất cả lên nền matplotlib
