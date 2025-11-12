import librosa

#加载'大家好我是壮猿.wav'音频文件，并转存为数组
a, s = librosa.load('大家好我是壮猿.wav')

#提取音频的mfcc特征
result = librosa.feature.mfcc(y=a,sr=s)

#打印出mfcc特征
print(result)

