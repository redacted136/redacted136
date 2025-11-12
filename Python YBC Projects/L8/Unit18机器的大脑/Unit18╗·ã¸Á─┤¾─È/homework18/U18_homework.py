import deepAI

# 录入训练集[体重,身高]
train_data = [[60, 165], [73, 183], [69, 178], [54, 153]]
train_label = [0, 1, 1, 0]
# 数据预处理，训练数据和标签
train_data = deepAI.prepare_data(train_data)
train_label = deepAI.prepare_data(train_label)
# 输入爸爸和妈妈的身高体重，[体重，身高]
father = deepAI.prepare_data([70,100])
mother = deepAI.prepare_data([50,160])
# 初始化神经网络的权重，并利用神经网络进行训练
network = deepAI.OurNeuralNetwork()
network.train(train_data, train_label)
# 神经网络预测，并输出结果
print('爸爸: ' + str(network.score(father)))
print('妈妈: ' + str(network.score(mother)))















