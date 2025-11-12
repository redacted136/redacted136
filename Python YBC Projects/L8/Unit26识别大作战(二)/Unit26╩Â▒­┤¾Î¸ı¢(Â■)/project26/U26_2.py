#
#
# 题目一 ：
# 补全代码，输出指定视频的帧率，宽，和高。
# 输出结果如图所示：

import cv2

video = cv2.VideoCapture('video/test1.mp4')  # 加载视频

frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) # 视频总帧数
fps = int(video.get(cv2.CAP_PROP_FPS))  # 帧率
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高

print('总帧数：',frame_num )
print('帧率：',fps )
print('宽：', w)
print('高：', h)



