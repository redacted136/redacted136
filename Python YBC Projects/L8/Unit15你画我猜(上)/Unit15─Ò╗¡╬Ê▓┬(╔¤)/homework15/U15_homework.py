from handWriting import convert, get_train_data, get_test_data
from sklearn.neighbors import KNeighborsClassifier
import cv2

'''读取图像和转换图像'''
#读图
pic = cv2.imread('screenshot.jpg')
#将使用的字符串存储在变量tokens中
tokens = '10'
#转字符图像
convert(pic, tokens, 'output.txt', 'testingData')

'''获取训练数据,实例化模型,训练模型'''
#实例化KNN模型
model = KNeighborsClassifier(n_neighbors=3)
#获得训练模型的数据
train_data, train_label = get_train_data('trainingData')
#训练模型
model.fit(train_data, train_label)

'''获取测试数据,预测,输出结果'''
#获取测试数据
result = get_test_data()
#预测
result.predict()
#输出预测的结
