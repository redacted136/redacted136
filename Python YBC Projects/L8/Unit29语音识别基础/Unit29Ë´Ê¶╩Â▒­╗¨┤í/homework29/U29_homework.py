import librosa.display
from matplotlib import pyplot

#加载音频
a,s = librosa.load('课后作品.wav')
#绘制音频波形
librosa.display.waveshow(y=a,sr=s)
#提取音频mfcc特征
result = librosa.feature.mfcc(y=a,sr=s)
#打印特征提取结果
print('mfcc特征：:',result)
#显示波形图
pyplot.show()



