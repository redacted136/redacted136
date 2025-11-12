import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # sigmoid函数的导数
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


def prepare_data(lst):
    if lst[1] == 1 or lst[1] == 0:
        return np.array(lst)
    elif len(lst) == 2:
        l = [lst[0]-61, lst[1]-168]
        return np.array(l)
    else:
        l = [[i[0]-61, i[1]-168] for i in lst]
        return np.array(l)


class OurNeuralNetwork():

    def __init__(self):
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def score(self, x):
        # x ： [input1, input2]
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 1000
        ech = []
        los = []

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # 前向传播
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1  # 单个样本的预测值

                # 反向传播
                # 计算偏导数
                # 损失函数针对于预测结果求导 d_L / d_ypred
                d_L_d_ypred = -2 * (y_true - y_pred)

                # 神经元 o1
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)  # ypred 函数针对于 w5 的导数
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)  # ypred 函数针对于 w6 的导数
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)  # ypred 函数针对于 b3 的导数

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)  # ypred 函数针对于 h1 的导数
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)  # ypred 函数针对于 h1 的导数

                # 神经元 h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)  # h1 函数针对于 w1 的导数
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)  # h1 函数针对于 w2 的导数
                d_h1_d_b1 = deriv_sigmoid(sum_h1)  # h1 函数针对于 b1 的导数

                # 神经元 h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)  # h2 函数针对于 w3 的导数
                d_h2_d_w4 = x[0] * deriv_sigmoid(sum_h2)  # h2 函数针对于 w4 的导数
                d_h2_d_b2 = deriv_sigmoid(sum_h2)  # h2 函数针对于 b2 的导数

                # 更新权重和偏置
                # 神经元 o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

                # 神经元 h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # 神经元 h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2


            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.score, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                ech.append(epoch)
                los.append(loss)
                print("Epoch %d loss: %.5f" % (epoch, loss))

        plt.plot(ech, los)
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.show()
