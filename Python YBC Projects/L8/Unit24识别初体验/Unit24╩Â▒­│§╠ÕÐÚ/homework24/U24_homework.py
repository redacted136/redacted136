import cv2


img = cv2.imread('img/cat2.png')  # 读取图片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化

img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化



face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')  # 加载级联分类器a
faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
print(faces)
# 遍历所有检测到的猫脸：
    # 绘制圆形框
for (x, y, w, h) in faces:
    # 补全绘制圆形框的代码  img = cv2.circle(图像,圆心坐标,半径,边框颜色,边框粗细)
    image = cv2.circle(img, (x+w//2,y+h//2),w//2,(22,22,22),5)
cv2.imshow('cat', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

