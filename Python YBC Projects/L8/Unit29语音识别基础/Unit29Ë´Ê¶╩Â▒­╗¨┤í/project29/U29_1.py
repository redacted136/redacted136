#pip install SpeechRecognition
import speech_recognition as sr
from mic_record import record

r = sr.Recognizer()
mic = sr.Microphone()
print('正在录音中...请说话，时长为5秒钟')
audio = record(r, mic, 5)
print('录音结束，语音转文字结果如下：')
text = r.recognize_google(audio, language='cmn-Hans-CN')
print(text)

