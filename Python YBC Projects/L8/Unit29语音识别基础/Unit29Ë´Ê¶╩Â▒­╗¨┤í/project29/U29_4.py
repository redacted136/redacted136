import librosa.display
from matplotlib import pyplot

#加载‘大家好我是壮猿.wav音频’，并转存为数组
a, s = librosa.load('大家好我是壮猿.wav')

#绘制音频的波形
librosa.display.waveshow(y=a,sr=s)

#显示绘制的波形图
pyplot.show()

