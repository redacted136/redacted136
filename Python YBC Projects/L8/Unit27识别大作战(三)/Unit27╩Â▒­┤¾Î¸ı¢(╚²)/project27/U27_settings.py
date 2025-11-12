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
        image = cv2.imread(image_path, 0)


        face, rect = detect_face(image)
        if face is not None:
            faces.append(face)
            labels.append(label)


    return faces, np.array(labels)


def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)

    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_img.shape[0]
    xx1 = 0
    xx2 = png_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > jpg_img.shape[1]:
        xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
        x2 = jpg_img.shape[1]
    if y2 > jpg_img.shape[0]:
        yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
        y2 = jpg_img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_jpg = 1 - alpha_png

    # 开始叠加
    for c in range(0, 3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg * jpg_img[y1:y2, x1:x2, c]) + (alpha_png * png_img[yy1:yy2, xx1:xx2, c]))

    return jpg_img

def mosaic(pic,h1,h2,l1,l2):
    #马赛克效果
    cha = pic.shape
    height, width, deep = cha
    if h1 < 0 or h1 > height: h1 = 0
    if h2 < 0 or h2 > height: h2 = height
    if l1 < 0 or l1 > width: l1 = 0
    if l2 < 0 or l2 > width: l2 = width
    for m in range(h1, h2):  #马赛克
        for n in range(l1, l2):
            if m%10 == 0 and n%10 == 0 :
                for i in range(10):
                    for j in range(10):
                        b, g, r = pic[m,n]
                        pic[m+i, n+j] = (b, g, r)
    return pic

