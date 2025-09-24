import cv2
from matplotlib import pyplot as plt


def conv(image, kernel, mode='same'):
    if mode == 'fill':
        h = kernel.shape[0] // 2
        w = kernel.shape[1] // 2

        image = np.pad(image, ((h, h), (w, w), (0, 0)), 'constant')
    conv_b = _convolve(image[:, :, 0], kernel)
    conv_g = _convolve(image[:, :, 1], kernel)
    conv_r = _convolve(image[:, :, 2], kernel)
    res = np.dstack([conv_b, conv_g, conv_r])
    return res


def _convolve(image, kernel):
    h_kernel, w_kernel = kernel.shape
    h_image, w_image = image.shape

    res_h = h_image - h_kernel + 1
    res_w = w_image - w_kernel + 1

    res = np.zeros((res_h, res_w), np.uint8)
    for i in range(res_h):
        for j in range(res_w):
            res[i, j] = normal(image[i:i + h_kernel, j:j + w_kernel], kernel)
    return res

def normal(image, kernel):
    res = np.multiply(image, kernel).sum()
    if res > 255:
        return 255
    elif res<0:
        return 0
    else:
        return res


def convolution(path, choice):
    image = cv2.imread(path)
    res = conv(image, choice, 'fill')
    plt.imshow(res)
    plt.savefig('result.jpg', dpi=600)
    plt.show()




print('模型正在初始化中...')
import os
import numpy as np
from tensorflow.keras.applications.densenet import DenseNet121
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.python.keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split


dataset_dir = 'data'


def loadImages(data_dir):
    data = {}
    for c in ['dandelion', 'roses', 'sunflowers']:
        data[c] = []
        if c == 'dandelion':
            label = 0
        elif c == 'roses':
            label = 1
        elif c == 'sunflowers':
            label = 2

        files = os.listdir(data_dir + '/' + c)
        files = files[0:300]
        #files = files[0:600]  # Maximum number objects for each class

        for f_name in files:
            img_path = data_dir + '/' + c + '/' + f_name

            img = image.load_img(img_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            data[c].append([x, label])

    return data

data = loadImages(dataset_dir)

def split(dataset_dir):
    Xtrain = []
    Xtest = []
    Ytrain = []
    Ytest = []
    return Xtrain, Xtest, Ytrain, Ytest



def accuracy_score(A,B):
    train_classObj1, test_classObj1 = train_test_split(data['dandelion'], test_size=0.25)
    train_classObj2, test_classObj2 = train_test_split(data['roses'], test_size=0.25)
    train_classObj3, test_classObj3 = train_test_split(data['sunflowers'], test_size=0.25)

    train_objs = train_classObj1 + train_classObj2 + train_classObj3
    test_objs = test_classObj1 + test_classObj2 + test_classObj3

    train_data = [x[0] for x in train_objs]
    train_label = [y[1] for y in train_objs]

    test_data = [x[0] for x in test_objs]
    test_label = [y[1] for y in test_objs]

    X_train = np.array(train_data)
    X_test = np.array(test_data)

    train_data = np.squeeze(X_train)
    train_label = np.array(train_label)

    test_data = np.squeeze(X_test)
    test_label = np.array(test_label)
    base_model = DenseNet121(weights='imagenet', include_top=False)

    training_feature = [base_model.predict(x).flatten() for x in X_train]
    test_feature = [base_model.predict(x).flatten() for x in X_test]

    training_feature = np.array(training_feature)
    test_feature = np.array(test_feature)

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(32, activation='relu')(x)
    predictions = Dense(3, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    # Freeze all convolutional DenseNet layers and train only top layers (FC)
    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
    history = model.fit(train_data, to_categorical(train_label),
                        epochs=9,
                        batch_size=32,
                        validation_data=(test_data, to_categorical(test_label)))
    return history


def CNN_model():
    return

def train(A, B, C):
    return

def predict(A):
    return
