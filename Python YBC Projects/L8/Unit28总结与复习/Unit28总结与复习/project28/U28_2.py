import cv2

video = cv2.VideoCapture('video/video1.mp4')  # 加载视频

frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频总帧数
fps = int(video.get(cv2.CAP_PROP_FPS))  # 帧率
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高

# 创建视频写对象
videoWriter = cv2.VideoWriter('video_result/result.mp4', cv2.VideoWriter_fourcc('ｍ', 'ｐ', '4', 'ｖ'), fps, (w, h))

for i in range(frame_num):  # 帧数遍历，逐帧操作
    success, img = video.read()  # 读取视频帧
    if not success:
        break
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
    img_gray = cv2.equalizeHist(img_gray)  # 直方图均衡化
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # 加载级联分类器
    faces = face_cascade.detectMultiScale(img_gray)  # 检测面部
    for (x, y, w, h) in faces:  # 绘制面部矩形
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 5)
    videoWriter.write(img)  # 视频对象写入