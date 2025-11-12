import tensorflow as tf 
from tensorflow.keras.optimizers import Adam
import numpy as np
import cv2
import warnings
warnings.filterwarnings('ignore')


def test_image(path):
    INIT_LR = 1e-3
    EPOCHS = 25
    model = tf.keras.models.load_model('model.h5')
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
    model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
    image = cv2.imread(path)
    imageCpy = cv2.resize(image, (224, 224))
    images = [imageCpy]
    data = np.stack(images, axis=0)
    LABEL = ["covid-positive", "covid-negetive"]
    pred = model.predict(data)
    label = LABEL[pred.argmax()]
    print(label)
    cv2.putText(image, label, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def model():
    return
def train(m):
    return
def predict_image(img):
    return