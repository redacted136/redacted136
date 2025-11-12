import cv2


img = cv2.imread('img/cat3.png')  # 读取图片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化

img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化


face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')  # 加载级联分类器
faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测

cv2.imshow('cat', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

