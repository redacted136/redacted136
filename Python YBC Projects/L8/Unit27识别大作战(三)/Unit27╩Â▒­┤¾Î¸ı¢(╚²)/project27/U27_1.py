import cv2

capture = cv2.VideoCapture(0)  #加载摄像头


while True:  #不断循环获取画面

    success, img = capture.read()   #读取当前摄像头画面

    cv2.imshow('output', img)  #输出画面

    cv2.waitKey(1000)

    print('循环')

