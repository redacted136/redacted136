import nltk
from nltk.tag import hmm
from nltk.corpus import treebank
from util import convert

#实例化隐马尔科夫模型
model = hmm.HiddenMarkovModelTrainer()

#使用treebank数据训练，升级模型
train_data = treebank.tagged_sents()
model2 = model.train_supervised(train_data)

#将待标注句子划分成单词形式
word_list = nltk.word_tokenize('Tom will meet Will')

#进行词性标注并打印结果
result = model2.tag(word_list)
print(result)

#使用转换函数将英文标注转换成中文
new_result =
print(new_result)

