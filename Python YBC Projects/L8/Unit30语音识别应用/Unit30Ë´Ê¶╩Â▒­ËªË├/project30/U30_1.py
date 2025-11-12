import librosa
from dtw_algorithm import dtw

a1, s1 = librosa.load('train/a1.wav') #读取a1语音
a2, s2 = librosa.load('train/a2.wav') #读取a2语音
b2, s3 = librosa.load('train/b2.wav') #读取b2语音

result1 = librosa.feature.mfcc(y=a1, sr=s1) #提取a1的mfcc特征
result2 = librosa.feature.mfcc(y=a2, sr=s2) #提取a2的mfcc特征
result3 = librosa.feature.mfcc(y=b2, sr=s3) #提取b2的mfcc特征

#计算a1与a2的差异
diffrence1 = dtw(result1,result2)
#打印差异
print(diffrence1)
#计算a1与b2的差异
diffrence2 = dtw(result1,result3)
#打印差异
print(diffrence2)