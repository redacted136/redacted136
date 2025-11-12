import cv2
from U27_settings import merge_img

capture = cv2.VideoCapture(0)  #加载摄像头
while True:  #不断循环获取画面
    success, img = capture.read()   #读取当前摄像头画面
    #读取要替换的图片
    img2 = cv2.imread('img/gd.png', cv2.IMREAD_UNCHANGED)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度处理
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载分类器
    faces = face.detectMultiScale(img_gray)  #多尺度检测
    for (x, y, w, h) in faces:  #遍历检测到的面部


        img2 = cv2.resize(img2, (w, h)) #调整图片大小
        img = merge_img(img, img2, y, y+h, x, x+w) #将图片融合 参数：图1 图2 图片插入的位置坐标


    cv2.imshow("output", img)  #输出画面
    if cv2.waitKey(1) == ord('q'):  #如果按下q键，跳出循环
        break #跳出循环

capture.release()   # 释放摄像头




