import os
import cv2
import numpy as np

def detect_face(img):
    #将图像转变成灰度图像，因为OpenCV人脸检测器需要灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

    #加载OpenCV人脸识别器，注意这里的路径是前面下载识别器时，你保存的位置
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    #scaleFactor表示每次图像尺寸减小的比例，minNeighbors表示构成检测目标的相邻矩形的最小个数
    #这里选择图像尺寸减小1.2倍。minNeighbors越大，识别出来的人脸越准确，但也极易漏判
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1)

    # 如果图中没有人脸，该图片不参与训练，返回None
    if len(faces) == 0:
        return None, None

    # 提取面部区域
    (x, y, w, h) = faces[0]

    #返回人脸及其所在区域
    return gray[y:y + w, x:x + h], faces[0]


def get_train_data():
    #读取训练文件夹中的图片名称
    dirs = os.listdir(r'./img_train')
    faces = []
    labels = []
    for image_path in dirs:
        #如果图片的名称以happy开头，则标签为1l；sad开头，标签为2
        if image_path[0] == 'h':
            label = 1
        else:
            label = 2

        #得到图片路径
        image_path = './img_train/' + image_path

        #返回灰度图，返回Mat对象
        image = cv2.imread(image_path,0)


        face, rect = detect_face(image)
        if face is not None:
            faces.append(face)
            labels.append(label)


    return faces, np.array(labels)

def predict(test_img, face_recognizer):
    # 将标签1，2转换成文字
    subjects = ['', 'Happy', 'Sad']

    # 得到图像副本
    img = test_img.copy()

    # 从图像中检测脸部
    face, rect = detect_face(img)
    print(face,rect)

    # 使用我们的脸部识别器预测图像
    label = face_recognizer.predict(face)

    # 获取由人脸识别器返回的相应标签的名称
    label_text = subjects[label[0]]

    # 脸部矩形尺寸
    (x, y, w, h) = rect

    # 将需要的数据返回
    return x, y, w, h, label_text



