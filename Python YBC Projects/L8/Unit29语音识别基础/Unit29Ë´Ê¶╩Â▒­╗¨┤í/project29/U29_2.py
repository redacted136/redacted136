#pip install pyttsx3
import pyttsx3

#创建语音合成器
engine =pyttsx3.init()

#对文字进行语音合成
engine.say("吃屎")

#播放合成的语音
engine.runAndWait()
