import ybc_speech_recognition as ysr

print('请你提问~')

audio = ysr.record(5)
text = ysr.get_audio_info(audio)
print('问题：', text)

#创建'问题-->答案'的字典
#问题：'谁是编程最好的学生' 答案：'壮猿是编程最好的学生'
myDict = {'谁是编程最好的学生', '答案：壮猿是编程最好的学生'}

#从字典中取到对应答案
answer = myDict[text]

#输出答案
print('答案：', answer)
