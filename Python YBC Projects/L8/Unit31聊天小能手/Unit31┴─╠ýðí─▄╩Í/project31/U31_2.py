import ybc_speech_recognition as ysr


print('请你提问~')

#录制五秒音频
audio = ysr.record(5)
#将保存的语音转换为中文文字
text = ysr.get_audio_info(audio)
#输出文字
print('问题：', text)

