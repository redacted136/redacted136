from sklearn.tree import DecisionTreeClassifier
from src_homework import main

class Machinelearning():

    def __init__(self):
        self.name = "决策树模型升级版"

    def model_use(self, train_data, train_label, new_data):
        # 实例化决策树模型，决策标准设为熵
        model = DecisionTreeClassifier(criterion='entropy')
        # 输入数据与标签进行决策树模型构建
        model.fit(train_data,train_label)
        # 模型预测
        result = model.predict(new_data)
        return result

ml = Machinelearning()
main(ml)