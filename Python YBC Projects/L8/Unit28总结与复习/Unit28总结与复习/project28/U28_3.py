import cv2

#加载摄像头
capture = cv2.VideoCapture(0)
#不断循环获取画面
while True:
    success, img = capture.read()   #读取画面内容
    if not success:
        break
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度处理
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载级联分类器
    faces = face.detectMultiScale(img_gray)  #检测人脸
    for (x, y, w, h) in faces:  #绘制面部矩形
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 5)
        #添加文本信息
        cv2.putText(img, '36.5', (x, y), cv2.FONT_ITALIC, 2, (0, 255, 255), 5)  #给框加标签

    cv2.imshow('output', img)  #输出画面内容
    if cv2.waitKey(1) == ord('q'):  #按q退出
        break

capture.release()   # 释放摄像头
