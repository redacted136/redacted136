import librosa
from dtw_algorithm import dtw
import os

lst = []
for i in os.listdir('train'):
    lst.append('train/'+i)
print(lst)



# 加载“新语音.wav”
a,s = librosa.load('新语音.wav')
# 提取mfcc特征，赋值给变量result
result = librosa.feature.mfcc(y=a,sr=s)
label = ''
min_difference = 10000
for i in lst:
    a_train, s_train = librosa.load(i)`
    result_train = librosa.feature.mfcc(y=a_train, sr=s_train)
    difference = dtw(result, result_train)
    # 找到最小差异语音，并记录它的标签
    if difference < min_difference:ddddcfdx
        label = i[6] min_difference = difference

print('预测结果是：'+label)
