import ybc_speech_recognition as ysr
import pyttsx3

print('请你提问~')

audio = ysr.record(5)
text = ysr.get_audio_info(audio)
print('问题：', text)

myDict = {
    '谁是编程最好的学生': '壮猿是编程最好的学生'
}
answer = myDict[text]
print('答案：', answer)

# 调用pyttsx3中的init()函数，创造一个语音合成器
engine = pyttsx3.init()

#语音合成器调用say()函数，对文字进行语音合成
engine.say(answer)

# 语音合成器调用runAndWait()函数进行声音播放
engine.runAndWait()
