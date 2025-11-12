#卸载opencv-contrib-python的指令: pip uninstall opencv-contrib-python
#再卸载opencv-python的指令: pip uninstall opencv-python
#然后先安装opencv-python的指令: pip install opencv-python==4.5.5.62
#最后再安装opencv-contrib-python的指令: pip install opencv-contrib-python==4.6.0.66
from U25_settings import get_train_data
import cv2
import numpy as np

# 加载预测图像,找到面部位置
img = cv2.imread('img_predict/unknown2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化
img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载面部级联分类器
faces = face_cascade.detectMultiScale(img_gray)  # 多尺度检测面部
(x, y, w, h) = faces[0]  #面部位置

# 构建（LBPH）情绪识别模型
model = cv2.face.LBPHFaceRecognizer_create()
# 调用之前写的函数，得到包含多个人脸矩阵的序列和它们对于的标签
train_data, train_label = get_train_data()
# 应用数据，进行训练
model.train(train_data, train_label)

# 进行预测
result = model.predict(img_gray[y:y + h, x:x + w]) #脸部区域的图像传入模型中
emo = ['', 'Happy', 'Sad']  #标签
emo_result = emo[result[0]]  #将识别出的结果对应标签，获得最终结果
print(emo_result)  #输出结果


