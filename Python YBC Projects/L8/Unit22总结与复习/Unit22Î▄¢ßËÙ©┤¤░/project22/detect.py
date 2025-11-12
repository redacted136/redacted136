import Covid_AI

model = Covid_AI.model()
Covid_AI.train(model)
image = Covid_AI.test_image('normal1.jpeg')
Covid_AI.predict_image(image)
s