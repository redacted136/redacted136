import cv2







def cat_fr(img_path):
    model_cat = 'haarcascade_frontalcatface.xml'
    img = cv2.imread(img_path)  # 读取图片
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化

    face_cascade = cv2.CascadeClassifier(model_cat)  # 加载模型
    faces = face_cascade.detectMultiScale(img_gray)  # 检测面部

    for (x, y, w, h) in faces:  # 遍历所有检测到的面部
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 5)  # 绘制矩形框

    return img
