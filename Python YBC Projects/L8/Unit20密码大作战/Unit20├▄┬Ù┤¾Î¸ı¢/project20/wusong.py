#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import ImageTk, Image
import tkinter as tk  # 使用Tkinter前需要先导入
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as TTS
import numpy as np

window = tk.Tk()
window.title('武松')
window.geometry('500x250')


l1 = tk.Label(window, text='《武松喝了什么酒》', width=50, font=('Arial', 20))
l1.pack()
l2 = tk.Label(window, fg='black', width=20, text='输入隐藏层参数：')
l2.pack()
e = tk.Entry(window, show = None)
e.pack()
l = tk.Label(window, fg='black', width=20, text='empty')
l.pack()
iter = 0
def print_selection(v):
    l.config(text='选择的迭代次数是' + v)
    global iter
    iter = v
s = tk.Scale(window, label='拖动滑块确定max_iter：', from_=0, to=2000, orient=tk.HORIZONTAL, length=400, showvalue=0,tickinterval=200, resolution=1, command=print_selection)
s.pack()
acc = 0

l1 = tk.Label(window, fg='black', width=20, text='预测准确率是:')
l1.pack(side='bottom')


def get_settings():
    hidden = e.get()
    res = []
    for i in hidden.split(","):
        a = i.replace(' ', '')
        res.append(int(a))
    iters = iter
    Data = load_wine()
    train_data, test_data, train_label, test_label = TTS(Data.data, Data.target, test_size=0.3, random_state=0)
    model = MLPClassifier(hidden_layer_sizes=(res), max_iter=int(iters), random_state=0)
    model.fit(train_data, train_label)
    predict = model.predict(test_data)
    acc = accuracy_score(predict, test_label)
    acc = '%.4f' % acc
    l1.config(text='预测准确率是:' + str(acc))


b1 = tk.Button(window, text='确认参数', width=10,
               height=0, command=get_settings)
b1.pack()


def print_selection(acc):
    l1.config(text='预测准确率是' + str(acc))

img_gif = tk.PhotoImage(file = 'wusong.gif')
label_img = tk.Label(window, image = img_gif)
label_img.pack()


window.mainloop()
