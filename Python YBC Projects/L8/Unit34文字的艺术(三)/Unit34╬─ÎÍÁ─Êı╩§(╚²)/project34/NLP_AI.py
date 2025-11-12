from keras.layers.core import Activation, Dense
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import collections
import nltk
import numpy as np

maxlen = 0
word_freqs = collections.Counter()
num_recs = 0
with open('情感分析数据.txt', 'r+') as f:
    for line in f:
        sentence, label = line.strip().split("\t")
        words = nltk.word_tokenize(sentence.lower())
        if len(words) > maxlen:
            maxlen = len(words)
        for word in words:
            word_freqs[word] += 1
        num_recs += 1
MAX_FEATURES = 2000
MAX_SENTENCE_LENGTH = 40
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
word2index = {x[0]: i + 2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word2index["PAD"] = 0
word2index["UNK"] = 1
index2word = {v: k for k, v in word2index.items()}
X = np.empty(num_recs, dtype=list)
y = np.zeros(num_recs)
i = 0

EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 10


def split(path):
    global word2index, X, y, i
    with open(path, 'r+') as f:
        for line in f:
            sentence, label = line.strip().split("\t")
            words = nltk.word_tokenize(sentence.lower())
            seqs = []
            for word in words:
                if word in word2index:
                    seqs.append(word2index[word])
                else:
                    seqs.append(word2index["UNK"])
            X[i] = seqs
            y[i] = int(label)
            i += 1
    X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)
    ## 数据划分
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)
    return Xtrain, Xtest, ytrain, ytest


def rnn_model():
    global EMBEDDING_SIZE, HIDDEN_LAYER_SIZE, vocab_size, MAX_SENTENCE_LENGTH
    model = Sequential()
    model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=MAX_SENTENCE_LENGTH))
    model.add(SimpleRNN(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1))

    model.add(Activation("sigmoid"))
    #model.add(Activation("tanh"))
    #model.add(Activation("relu"))
    #model.add(Activation("hard_sigmoid"))

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model

def lstm_model():
    global EMBEDDING_SIZE, HIDDEN_LAYER_SIZE, vocab_size, MAX_SENTENCE_LENGTH
    model = Sequential()
    model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=MAX_SENTENCE_LENGTH))
    model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1))

    model.add(Activation("sigmoid"))
    #model.add(Activation("tanh"))
    #model.add(Activation("relu"))
    #model.add(Activation("hard_sigmoid"))

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def train(model, Xtrain, ytrain):
    global BATCH_SIZE, NUM_EPOCHS
    model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS)
    return model


def accuracy_score(model, Xtest, ytest):
    score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
    print("\nTest accuracy score: %.3f" % score)


def accuracy(model, Xtest, ytest):
    score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
    return round(acc,3)
    #print("\nTest accuracy : %.3f" % acc)
    '''
    print('{}   {}      {}'.format('预测', '真实', '句子'))
    for i in range(10):
        idx = np.random.randint(len(Xtest))
        xtest = Xtest[idx].reshape(1, 40)
        ylabel = ytest[idx]
        ypred = model.predict(xtest)[0][0]
        sent = " ".join([index2word[x] for x in xtest[0] if x != 0])
        print(' {}      {}     {}'.format(int(round(ypred)), int(ylabel), sent))
    '''


def predict(model, sen):
    global word2index, MAX_SENTENCE_LENGTH
    INPUT_SENTENCES = []
    INPUT_SENTENCES.append(sen)
    XX = np.empty(len(INPUT_SENTENCES), dtype=list)
    i = 0
    for sentence in INPUT_SENTENCES:
        words = nltk.word_tokenize(sentence.lower())
        seq = []
        for word in words:
            if word in word2index:
                seq.append(word2index[word])
            else:
                seq.append(word2index['UNK'])
        XX[i] = seq
        i += 1

    XX = sequence.pad_sequences(XX, maxlen=MAX_SENTENCE_LENGTH)
    labels = [int(round(x[0])) for x in model.predict(XX)]
    label2word = {1: '积极', 0: '消极'}
    for i in range(len(INPUT_SENTENCES)):
        result = '{}   {}'.format(INPUT_SENTENCES[i], label2word[labels[i]])
    return result
