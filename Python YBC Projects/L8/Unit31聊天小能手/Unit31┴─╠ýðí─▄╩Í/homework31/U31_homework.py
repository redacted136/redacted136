import ybc_speech_recognition as ysr
import pyttsx3
r.record(5)
text = ysr.get_audio_info(audio)
print('问题：', text)

myDict = {
     '谁是编程最好的学生': '壮猿是编程最好的学生',
    '你是谁':'我是你的机器人',
    '你在干什么？':'我在跟你聊天'
    }
if text in myDict.keys():
    answer = myDict[text]
else:
    answer = '我的知识库里没有啊'
print('答案：', answer)

engine = pyttsx3.init()
engine.say(answer)
engine.runAndWait()

