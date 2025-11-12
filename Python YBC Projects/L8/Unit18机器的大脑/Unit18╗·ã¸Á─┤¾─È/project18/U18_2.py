import deepAI

# 收集数据
train_data = [[60, 165], [73, 183], [69, 178], [54, 153]]  # 录入训练集的[体重，身高]
train_label = [0, 1, 1, 0]  # 录入标签，0代表女生，1代表男生

# 数据预处理
train_data = deepAI.prepare_data(train_data)
train_label = deepAI.prepare_data(train_label)
XiaoMing = deepAI.prepare_data(  )  # 输入小明的[体重67，身高180]
XiaoHong = deepAI.prepare_data(  )  # 输入小红的[体重55，身高164]

# 训练过程
network = deepAI.OurNeuralNetwork()  # 初始化神经网络的权重
network.train(train_data, train_label)       # 利用神经网络进行训练

# 预测过程，如果结果接近0，预测是女生，如果结果接近1，预测是男生
print("XiaoMing: " + )
print("XiaoHong: " +  )
