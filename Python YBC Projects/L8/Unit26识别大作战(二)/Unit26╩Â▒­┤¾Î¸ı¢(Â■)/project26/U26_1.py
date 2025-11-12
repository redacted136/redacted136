import cv2

video = cv2.VideoCapture('video/test1.mp4')  # 加载视频

frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频总帧数

print(frame_num) #输出结果


