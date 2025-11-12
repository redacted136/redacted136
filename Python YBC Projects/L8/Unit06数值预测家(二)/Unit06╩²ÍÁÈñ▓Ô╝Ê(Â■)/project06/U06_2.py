# pip install scikit-learn==0.24.2 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
# pip install scikit-image==0.18.2 -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
from sklearn.linear_model import LinearRegression
from src import main

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
        ?
        # 将数据与标签输入模型进行训练
        ?
        # 模型根据新数据进行预测
        ?

        return result

ml = Machinelearning()
main(ml)
