# IMAGES
import cv2
import numpy as np

def nothing(x):
    pass
# tạo một cửa sổ có tên Tracking và tạo ra các thanh trackbar chỉnh màu
cv2.namedWindow("Tracking") 
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
# 
while True:
    frame = cv2.imread('smarties.png') # đọc hình ảnh
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # tạo một biến HSV chuyển màu của hình ảnh theo màu HSV
# tạo 3 biến lấy màu BGR của lower HSV
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
# tạo 3 biến lấy màu BGR của upper HSV
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v]) # đưa tông màu vào biến l_b giới hạn ngưỡng màu dưới
    u_b = np.array([u_h, u_s, u_v]) # # đưa tông màu vào biến l_b giới hạn ngưỡng màu trên

    mask = cv2.inRange(hsv, l_b, u_b) # tiến hành lọc màu sắc HSV theo ngưỡng ( mặt nạ màu sắc trắng đen 0 -1)

    res = cv2.bitwise_and(frame, frame, mask=mask) # tiến hành hiển thị ảnh gốc và chỉ định phần tử có ngưỡng màu xác định sẽ thay đổi là mask

    cv2.imshow("frame", frame) #  hiển thị ảnh gốc
    cv2.imshow("mask", mask) # hiển thị ảnh trắng đen 
    cv2.imshow("res", res)# hiển thị ảnh gốc thay đỗi theo HSV

    key = cv2.waitKey(1)
    if key == 27: # nhấn esc để thoát vòng lặp
        break

cv2.destroyAllWindows()
###################################################################################################
# VIDEOS
import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0); # lấy id của camera 
# tạo một cửa sổ có tên Tracking và tạo ra các thanh trackbar chỉnh màu
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    _, frame = cap.read() # đọc dữ liêu từ camera

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
