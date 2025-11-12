import pandas as pd
import numpy

data = pd.read_csv('height_data.csv')
train_data = data['父亲身高']
train_data = numpy.array(train_data)
print(train_data)

# 将'孩子身高'数据存入train_label变量中
?

# 将train_label数据形式转换为numpy数组
?

print(train_label)
