import pygame
import cv2
import numpy as np
from os import listdir
from sklearn.neighbors import KNeighborsClassifier as KNN

color_white = pygame.Color(255, 255, 255)
color_black = pygame.Color(0, 0, 0)
color_green = pygame.Color(0, 255, 0)
color_red = pygame.Color(255, 0, 0)


def showImg1(img,tokens,filename,path):

    pic = img
    # 输出字符画的宽度
    WIDTH = 32
    # 输出字符画的高度
    HEIGHT = 32
    pic = cv2.resize(pic, (WIDTH, HEIGHT))
    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            # txt += get_char(*im.getpixel((j,i)))
            txt += get_char(pic[i][j][0], pic[i][j][1], pic[i][j][2], tokens)
        # 遍历完一行后需要增加换行符
        txt += '\n'
    print(txt)
    with open(path+'/'+filename, 'w') as f:
        f.write(txt)


def get_char(r,g,b,tokens):   #灰度转换  图片转字符
    # ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    # ascii_char = list("10")
    ascii_char = list(tokens)
    # 判断 alpha 值
    if tokens == '':
        return ' '

    # 获取字符集的长度，这里为 70
    length = len(ascii_char)

    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-256
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length
    # 可以理解为 每个长度 存放 多少个灰度值

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]
	# gray这个灰度值，需要多少个长度。然后索引取出字符。

def convert(img, tokens, filename, path):
    showImg1(img, tokens, filename, path)


"""
函数说明:将32x32的二进制图像转换为1x1024向量
"""
def img2vector(filename):
    #创建1x1024零向量
    returnVect = np.zeros((1, 1024))
    #打开文件
    fr = open(filename)
    #按行读取
    for i in range(32):
        #读一行数据
        lineStr = fr.readline()
        #每一行的前32个元素依次添加到returnVect中
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    #返回转换后的1x1024向量
    return returnVect



"""
函数说明:获取数据集
"""
def get_train_data(path):
    #训练集的Labels
    hwLabels = []
    #返回trainingDigits目录下的文件名
    trainingFileList = listdir(path)
    if '.DS_Store' in trainingFileList:
        trainingFileList.remove('.DS_Store')
    #返回文件夹下文件的个数
    m = len(trainingFileList)
    #初始化训练的Mat矩阵,训练集
    trainingMat = np.zeros((m, 1024))
    #从文件名中解析出训练集的类别
    for i in range(m):
        #获得文件的名字
        fileNameStr = trainingFileList[i]
        #获得分类的数字
        if fileNameStr == '.DS_Store': continue
        classNumber = int(fileNameStr.split('_')[0])
        #将获得的类别添加到hwLabels中
        hwLabels.append(classNumber)
        #将每一个文件的1x1024数据存储到trainingMat矩阵中
        trainingMat[i,:] = img2vector('trainingData/%s' % (fileNameStr))

    return trainingMat,hwLabels

"""
函数说明:手写数字分类测试
"""
# def get_model():
#     #训练集的Labels
#     hwLabels = []
#     #返回trainingDigits目录下的文件名
#     trainingFileList = listdir('trainingDigits')
#     #返回文件夹下文件的个数
#     m = len(trainingFileList)
#     #初始化训练的Mat矩阵,训练集
#     trainingMat = np.zeros((m, 1024))
#     #从文件名中解析出训练集的类别
#     for i in range(m):
#         #获得文件的名字
#         fileNameStr = trainingFileList[i]
#         #获得分类的数字
#         if fileNameStr == '.DS_Store': continue
#         classNumber = int(fileNameStr.split('_')[0])
#         #将获得的类别添加到hwLabels中
#         hwLabels.append(classNumber)
#         #将每一个文件的1x1024数据存储到trainingMat矩阵中
#         trainingMat[i,:] = img2vector('trainingDigits/%s' % (fileNameStr))
#     #构建kNN分类器
#     neigh =KNN(n_neighbors = 3, algorithm = 'auto')
#     #拟合模型, trainingMat为训练矩阵,hwLabels为对应的标签
#     neigh.fit(trainingMat, hwLabels)
#     return neigh
    # clf = SVC(C=200, kernel='rbf')
    # clf.fit(trainingMat, hwLabels)


def get_test_data(path):
    vectorUnderTest = img2vector(path+'/output.txt')
    return vectorUnderTest

def get_result(model,path):
    #返回testDigits目录下的文件列表
    # testFileList = listdir('testDigits')
    #错误检测计数
    # errorCount = 0.0
    #测试数据的数量
    # mTest = len(testFileList)
    #从文件中解析出测试集的类别并进行 分类 测试
    # print(mTest)
    # for i in range(mTest):
        #获得文件的名字
        # fileNameStr = testFileList[i]
        #获得分类的数字
        # if fileNameStr == '.DS_Store' : continue
        # print(fileNameStr)
        #classNumber = int(fileNameStr.split('_')[0])
        #获得测试集的1x1024向量,用于训练
        vectorUnderTest = img2vector(path)
        print(vectorUnderTest)
        #获得预测结果
        classifierResult = model.predict(vectorUnderTest)
        # print("分类返回结果为%d\t真实结果为%d" % (classifierResult, classNumber))
        print("分类返回结果为%d" % (classifierResult))


