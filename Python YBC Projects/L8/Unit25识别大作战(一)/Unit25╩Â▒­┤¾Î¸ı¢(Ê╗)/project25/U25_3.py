import cv2

img = cv2.imread('img/test3.png')  # 读取图片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化

eye = cv2.CascadeClassifier('haarcascade_eye.xml')  #加载眼睛级联分类器
eyes = eye.detectMultiScale(img_gray)  #多尺度检测眼睛
for (ex,ey,ew,eh) in eyes:  #绘制眼部矩阵框
    img = cv2.rectangle(img, (ex,ey), (ex+ew,ey+eh), (255, 255, 0), 2)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载面部级联分类器
faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测面部
for (x, y, w, h) in faces:  # 遍历所有检测到的脸
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 5)  # 绘制矩形框

cv2.imshow('Detection', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示
