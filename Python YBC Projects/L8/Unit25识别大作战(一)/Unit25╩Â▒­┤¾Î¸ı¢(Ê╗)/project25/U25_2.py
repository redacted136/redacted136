# 题目二 ：
# 修改面部识别的部分代码，完成眼部识别。
# 补充加载级联分类器部分的代码。（分类器名：eye_cascade，参数：haarcascade_eye.xml）
# 补充多尺度检测与绘制矩形框部分的代码。（注意对应的变量名eyes与eye_cascade）

import cv2

img = cv2.imread('img/test3.png')  # 读取图片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化

#加载眼睛级联分类器
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#多尺度检测眼睛
eye = eye_cascade.detectMultiScale(img_gray)

for (x, y, w, h) in faces:  #绘制眼部矩阵框
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

cv2.imshow('Eye detection', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

