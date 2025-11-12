from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as TTS

Iris = load_iris()
#data.target有0，1，2三个品种的花
train_data, test_data, train_label, test_label = TTS(Iris.data, Iris.target, test_size=0.3)

#实例化模型
model = MLPClassifier(hidden_layer_sizes=(5))
#将数据与标签输入模型进行训练
model.fit(train_data, train_label)
#模型对新数据的类别进行预测
result = model.score(test_data, test_label)
print(result)

