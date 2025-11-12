from U24_settings import cat_fr
import cv2


img_path = 'img/cat1.png'
img = cat_fr(img_path)
cv2.imshow('catface', img)  # 检测效果预览
cv2.waitKey()  # 保持窗口显示

