from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as TTS

Digits = load_digits()
train_data, test_data, train_label, test_label = TTS(Digits.data, Digits.target, test_size=0.3, random_state=0)

model = MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100, 100), max_iter=2000, random_state=0)
model.fit(train_data, train_label)
result = model.predict(test_data)
acc = accuracy_score(result,test_label)
print("accuracy_score of MLP: ", acc)

