import ybc_speech_recognition as ysr
import pyttsx3
import NLP_AI

while True:
    print('请提问~')

    audio = ysr.record(5)
    text = ysr.get_audio_info(audio)
    print('问题：', text)

    model = NLP_AI.load_model('成熟的编码解码模型.h5')
    answer = NLP_AI.predict(model, text)
    print(answer)

    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

