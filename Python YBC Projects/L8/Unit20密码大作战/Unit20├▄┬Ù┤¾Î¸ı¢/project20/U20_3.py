from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as TTS
import time
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans


Digits = load_digits()
train_data, test_data, train_label, test_label = TTS(Digits.data, Digits.target, test_size=0.3, random_state=0)

# KNN模型
time_start = time.time()
model1 = KNeighborsClassifier(n_neighbors=10)
model1.fit(train_data,train_label)
result = model1.predict(test_data)
print('accuracy_score of KNN: ', str(accuracy_score(result,test_label)))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

# 感知机模型
time_start = time.time()
model2 = Perceptron()
model2.fit(train_data,train_label)
result = model2.predict(test_data)
print("accuracy_score of Perceptron: %.4f" % accuracy_score(result,test_label))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

# 决策树模型
time_start = time.time()
model3 = DecisionTreeClassifier(criterion='entropy')
model3.fit(train_data,train_label)
result = model3.predict(test_data)
print("accuracy_score of DecisionTree: " , str(accuracy_score(result,test_label)))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

# SVM模型
time_start = time.time()
model4 = SVC(kernel='linear')
model4.fit(train_data,train_label)
result = model4.predict(test_data)
print("accuracy_score of svm: ", str(accuracy_score(result,test_label)))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

# 聚类模型
time_start = time.time()
model5 = KMeans(n_clusters=10, random_state=0)
model5.fit(train_data)
result = model5.predict(test_data)
print("accuracy_score of kmeans: ", str(accuracy_score(result,test_label)))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

# 深度学习模型
time_start = time.time()
model = MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100, 100), max_iter=2000, random_state=0)
model.fit(train_data, train_label)
result = model.predict(test_data)
print("accuracy_score of MLP: ", str(accuracy_score(result,test_label)))
time_end = time.time()
print('time cost: ', (time_end-time_start), 's')

