import ybc_speech_recognition as ysr
import pyttsx3

print('请你提问~')
audio = ysr.record(5)
text = ysr.get_audio_info(audio)
print('问题：', text)

myDict = {
    '谁是编程最好的学生': '壮猿是编程最好的学生'
}

#判断字典dict中是否有text键。如果有，取出对应值；如果没有，输出'我的知识库里没有啊'。
if text in myDict.keys():
    answer = myDict[text]
else:
    answer = '我的知识库里没有啊'
print('答案：', answer)

engine = pyttsx3.init()
engine.say(answer)
engine.runAndWait()

