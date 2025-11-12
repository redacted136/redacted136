# 题目一 ：
# 补全下面代码，实现开启摄像头。

import cv2

capture =   #加载摄像头


#不断循环获取画面

    success, img = capture.read()   #读取当前摄像头画面

    cv2.imshow('output', img)  #输出画面

    if cv2.waitKey(1) == ord('q'):  #如果按下q键，跳出循环

        #跳出循环

capture.release()   #释放摄像头
