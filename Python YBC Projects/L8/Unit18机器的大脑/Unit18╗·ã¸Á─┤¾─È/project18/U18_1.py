import deepAI

# 收集数据
train_data = [[60, 165], [73, 183], [69, 178], [54, 153]]  # 录入训练集的[体重，身高]
train_label = [0, 1, 1, 0]  # 录入标签，0代表女生，1代表男生

# 数据预处理
#train_data = deepAI.prepare_data(train_data)
#train_label = deepAI.prepare_data(train_label)
#Jia = deepAI.prepare_data([58, 160])  # 输入甲的[体重，身高]
#Yi = deepAI.prepare_data([70, 173])  # 输入乙的[体重，身高]

# 训练过程
#network = deepAI.OurNeuralNetwork()  # 初始化神经网络的权重
#network.train(train_data, train_label)       # 利用神经网络进行训练

# 预测过程
#print("Jia: " + str(network.score(Jia)))  # 结果接近0，预测是女生
#print("Yi: " + str(network.score(Yi)))   # 结果接近1，预测是男生
