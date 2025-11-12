import cv2

#题目一 ： 补全代码，实现图像灰度化与直方图均衡化的操作。
img = cv2.imread('img/cat3.png')  # 读取图片

#—------补全下方代码—------
# 灰度化处理（使用openCV内置函数）
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 直方图均衡化（使用openCV内置函数）
img_gray = cv2.equalizeHist(img_gray)

cv2.imshow('cat', img_gray)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

