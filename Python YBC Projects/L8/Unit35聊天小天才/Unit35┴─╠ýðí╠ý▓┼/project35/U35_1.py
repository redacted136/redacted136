import NLP_AI

model = NLP_AI.load_model('成熟的编码解码模型.h5')

question = '你吃了没'

answer = NLP_AI.predict(model, question)

print('问题:', question)

print('回答:', answer)
