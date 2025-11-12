from sklearn.linear_model import LinearRegression
from src_3 import main

class Machinelearning():

    def __init__(self):
        self.name = "身高预测仪"

    def model_use(self, train_data, train_label, new_data):

        '''
        说明：
        train_data变量存储了训练数据
        train_label变量存储了训练标签
        new_data变量存储了待预测的新数据
        '''

        # 实例化模型
        model = LinearRegression()
        # 将数据与标签输入模型进行训练
        model.fit(train_data, train_label)
        # 模型根据新数据进行预测
        result = model.predict(new_data)

        return result

ml = Machinelearning()
main(ml)
