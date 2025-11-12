import cv2
from U27_settings import get_train_data


# 构建（LBPH）情绪检测模型
model = cv2.face.LBPHFaceRecognizer_create()
# 调用之前写的函数，得到包含多个人脸矩阵的序列和它们对于的标签
train_data, train_label = get_train_data()
# 应用数据，进行训练



capture = cv2.VideoCapture(0)  #加载摄像头


while True:  #不断循环获取画面
    success, img = capture.read()   #读取当前摄像头画面
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度处理
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载分类器
    faces = face.detectMultiScale(img_gray)  #多尺度检测
    for (x, y, w, h) in faces:  #遍历检测到的面部
        # 进行预测
        result = model.predict(img_gray[y:y + h, x:x + w])  # 调用模型进行识别
        emo = ['', 'Happy', 'Sad']  # 将标签对应的情绪单词填写在列表中
        emo_result = emo[result[0]]  # 调用识别结果中的标签，获得情绪列表中的单词

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 5) #绘制矩形框
        cv2.putText( img,emo_result ,(x ,y),cv2.FONT_ITALIC, 2, (0, 255, 255), 5)  #添加文本


    cv2.imshow('output', img)  #输出画面
    if cv2.waitKey(1) == ord('q'):  #如果按下q键，跳出循环
        #跳出循环
        break
capture.release()   # 释放摄像头




