
#
# 题目三 ：
# 添加绘制矩形框与文本信息的部分代码，完成以下效果。
# （ 需补全部分参数信息。）

from U25_settings import get_train_data
import cv2

# 加载预测图像,找到面部位置
img = cv2.imread('img_predict/unknown1.jpg')
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

# 矩形标出人脸
# cv2.rectangle(???, (x, y), (x + w, y + h), (255, 255, 0), 2)
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
# 在矩形周围标出文本信息
# cv2.putText(???, ???, (x, y), cv2.FONT_ITALIC, 1.5, (255, 255, 0), 2)
cv2.putText(img, emo_result, (x, y), cv2.FONT_ITALIC, 1.5, (255, 255, 0), 2)

# 显示预测结果
cv2.imshow('Emotion detection', img)
cv2.waitKey()

