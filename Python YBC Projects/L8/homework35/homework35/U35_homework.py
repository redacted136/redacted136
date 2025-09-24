import ybc_speech_recognition as ysr
import pyttsx3
import NLP_AI

# 结束短语
c_remarks = ['拜拜', '再见', '结束', '88', '八八']
# 结束谈话标志
flag = 0
while True:
    # 判断结束谈话标志是否为1
    if flag == 1:
        # 结束谈话
        break

    print('请提问~')

    audio = ysr.record(5)
    text = ysr.get_audio_info(audio)
    print('问题：', text)

    # 循环遍历结束短语
    for i in c_remarks:
        # 判断结束短语是否存在于谈话内容中
        if i in text:
            # 结束谈话标志设置为1
            flag = 1

    model = NLP_AI.load_model('成熟的编码解码模型.h5')
    answer = NLP_AI.predict(model, text)
    print(answer)

    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

