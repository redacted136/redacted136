import cv2
import os

#读取img文件架下的所有文件，存为列表
images = os.listdir('img')
for img_name in images: #遍历获取每个图像文件
    img = cv2.imread('img/'+img_name)  # 都区对应路径下的图像文件

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化

    #加载级联分类器
    face_cascade = cv2.Cascade.Classifier('haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测
    for (x, y, w, h) in faces:  # 遍历所有检测到的面部
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 5)  # 绘制矩形框
    cv2.imwrite('img_result/'+img_name, img) #输出图像到指定路径

