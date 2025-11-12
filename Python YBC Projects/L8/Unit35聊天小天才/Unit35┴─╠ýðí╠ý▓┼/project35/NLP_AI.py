import numpy as np
import pickle, os, re, operator
import jieba
import requests
import matplotlib.pyplot as plt
import matplotlib
from keras.layers import Embedding
from keras.layers import Input, Dense, LSTM, TimeDistributed, Bidirectional, Dropout, Concatenate, RepeatVector, Activation, Dot
from keras.layers import concatenate, dot
from keras.models import Model
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.initializers import TruncatedNormal
from keras.preprocessing import sequence

with open('pad_word_to_index.pkl', 'rb') as f:
    word_to_index = pickle.load(f)

with open('pad_index_to_word.pkl', 'rb') as f:
    index_to_word = pickle.load(f)

vocab_size = len(word_to_index) + 1
maxLen = 20


def load_model(parameters):
    truncatednormal = TruncatedNormal(mean=0.0, stddev=0.05)
    embed_layer = Embedding(input_dim=vocab_size,
                            output_dim=100,
                            mask_zero=True,
                            input_length=None,
                            embeddings_initializer=truncatednormal)
    LSTM_encoder = LSTM(512,
                        return_sequences=True,
                        return_state=True,
                        kernel_initializer='lecun_uniform',
                        name='encoder_lstm'
                        )
    LSTM_decoder = LSTM(512,
                        return_sequences=True,
                        return_state=True,
                        kernel_initializer='lecun_uniform',
                        name='decoder_lstm'
                        )

    # encoder输入 与 decoder输入
    input_question = Input(shape=(None,), dtype='int32', name='input_question')
    input_answer = Input(shape=(None,), dtype='int32', name='input_answer')

    input_question_embed = embed_layer(input_question)
    input_answer_embed = embed_layer(input_answer)

    encoder_lstm, question_h, question_c = LSTM_encoder(input_question_embed)

    decoder_lstm, _, _ = LSTM_decoder(input_answer_embed,
                                      initial_state=[question_h, question_c])

    attention = dot([decoder_lstm, encoder_lstm], axes=[2, 2])
    attention = Activation('softmax')(attention)
    context = dot([attention, encoder_lstm], axes=[2, 1])
    decoder_combined_context = concatenate([context, decoder_lstm])

    # Has another weight + tanh layer as described in equation (5) of the paper
    decoder_dense1 = TimeDistributed(Dense(256, activation="tanh"))
    decoder_dense2 = TimeDistributed(Dense(vocab_size, activation="softmax"))
    output = decoder_dense1(decoder_combined_context)  # equation (5) of the paper
    output = decoder_dense2(output)  # equation (6) of the paper

    model = Model([input_question, input_answer], output)

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

    model.load_weights(parameters)

    question_model = Model(input_question, [encoder_lstm, question_h, question_c])
    answer_h = Input(shape=(512,))
    answer_c = Input(shape=(512,))
    encoder_lstm = Input(shape=(maxLen, 512))
    target, h, c = LSTM_decoder(input_answer_embed, initial_state=[answer_h, answer_c])
    attention = dot([target, encoder_lstm], axes=[2, 2])
    attention_ = Activation('softmax')(attention)
    context = dot([attention_, encoder_lstm], axes=[2, 1])
    decoder_combined_context = concatenate([context, target])
    output = decoder_dense1(decoder_combined_context)  # equation (5) of the paper
    output = decoder_dense2(output)  # equation (6) of the paper
    answer_model = Model([input_answer, answer_h, answer_c, encoder_lstm], [output, h, c, attention_])
    model_set = (model, question_model, answer_model)
    return model_set

def input_question(seq):
    seq = jieba.lcut(seq.strip(), cut_all=False)
    sentence = seq
    try:
        seq = np.array([word_to_index[w] for w in seq])
    except KeyError:
        seq = np.array([36874, 165, 14625])
    seq = sequence.pad_sequences([seq], maxlen=maxLen,
                                          padding='post', truncating='post')
    return seq, sentence

def decode_greedy(question_model, answer_model, seq, sentence):
    question = seq
    answer = np.zeros((1, 1))
    attention_plot = np.zeros((20, 20))
    answer[0, 0] = word_to_index['BOS']
    i = 1
    answer_ = []
    flag = 0
    encoder_lstm_, question_h, question_c = question_model.predict(x=question)

    while flag != 1:
        prediction, prediction_h, prediction_c, attention = answer_model.predict([
            answer, question_h, question_c, encoder_lstm_
        ])
        attention_weights = attention.reshape(-1, )
        attention_plot[i] = attention_weights
        word_arg = np.argmax(prediction[0, -1, :])#
        answer_.append(index_to_word[word_arg])
        if word_arg == word_to_index['EOS'] or i > 18:
            flag = 1
        answer = np.zeros((1, 1))
        answer[0, 0] = word_arg
        question_h = prediction_h
        question_c = prediction_c
        i += 1
    result = ' '.join(answer_)
    attention_plot = attention_plot[:len(result.split(' ')), :len(sentence)]
    return ''.join(answer_[:-1])

def predict(model, sen):
    seq, sentence = input_question(sen)
    answer = decode_greedy(model[1], model[2], seq, sentence)
    #re = '回答: '+answer
    re = answer
    return re

