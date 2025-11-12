import cv2
from U23_settings import human_fr


img_path = 'img/human2.png'
img = human_fr(img_path)
cv2.imshow('humanface', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

