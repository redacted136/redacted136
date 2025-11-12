# 题目二 ：
# 补全部分代码，完成对给出视频的人脸检测，生成检测后的新视频。
# 1、补全逐帧遍历的for循环语句。
# 2、补全最后的写入操作。
# 3、运行代码，生成新视频。

import cv2
#____________________________________________________
video = cv2.VideoCapture('video/test1.mp4')  # 加载视频
frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频总帧数
fps = video.get(cv2.CAP_PROP_FPS)  # 帧率
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高

videoWriter = cv2.VideoWriter('result.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (w, h))  # 创建视频写对象
print('正在检测面部中。。。')
#____________________________________________________
# 帧数遍历，逐帧操作

success, img = video.read()  # 读取视频帧
if not success:
    break
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载脸部识别器
faces = face_cascade.detectMultiScale(img_gray)  # 检测面部
for (x, y, w, h) in faces:  # 绘制面部矩形
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 5)
    # ____________________________________________________
    # 视频对象写入
