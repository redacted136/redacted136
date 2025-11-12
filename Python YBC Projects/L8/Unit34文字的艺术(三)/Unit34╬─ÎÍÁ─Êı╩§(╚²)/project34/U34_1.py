#pip uninstall numpy   输入命令回车后在输入字母：y ，再回车
#pip install numpy==1.19.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
import NLP_AI

#数据划分
train_data, test_data, train_label, test_label = NLP_AI.split('情感分析数据.txt')

#实例化模型
model = NLP_AI.rnn_model()

#训练
model2 = NLP_AI.train(model, train_data , train_label )

#预测集测试分数
acc = NLP_AI.accuracy( model2 , test_data , test_label )
print(acc)

#自定义预测
result = NLP_AI.predict( model2 , 'I like this movie')
print(result)
