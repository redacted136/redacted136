import CNN_AI

dataset_dir = 'data'
train_data, test_data, train_label, test_label = CNN_AI.split(dataset_dir)

model = CNN_AI.CNN_model()
CNN_AI.train(model, train_data, train_label)
result = CNN_AI.predict(test_data)
acc = CNN_AI.accuracy_score(result, test_label)
