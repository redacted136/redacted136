import cv2
from U27_settings import mosaic


capture = cv2.VideoCapture(0)  #加载摄像头
while True:  #不断循环获取画面
    success, img = capture.read()   #读取当前摄像头画面
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度处理
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载分类器
    faces = face.detectMultiScale(img_gray)  #多尺度检测
    for (x, y, w, h) in faces:  #遍历检测到的面部

        img = mosaic(img, y, y+h, x, x+w)  #马赛克处理


    cv2.imshow("output", img)  #输出画面
    if cv2.waitKey(1) == ord('q'):  #如果按下q键，跳出循环
        break #跳出循环

capture.release()   # 释放摄像头




