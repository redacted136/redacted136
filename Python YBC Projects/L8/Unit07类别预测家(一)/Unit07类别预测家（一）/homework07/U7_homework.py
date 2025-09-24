from sklearn.neighbors import KNeighborsClassifier
from src_animal import main


class Machinelearning():

    def __init__(self):
        self.name = "物种预测仪"

    def model_use(self, train_data, train_label, new_data):
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(train_data,train_label)
        result = model.predict(new_data)
        return result


ml = Machinelearning()
main(ml)
