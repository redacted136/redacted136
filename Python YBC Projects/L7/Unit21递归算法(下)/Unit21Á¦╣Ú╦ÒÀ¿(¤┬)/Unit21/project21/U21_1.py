# 小猿位于一个3*7的网格左上角，每次只能向下后者向右移动一步
# 如果小猿想要走到网格的右下角来获得星星，那么总共有多少条路径
# 定义函数计算起点到位置(i,j)的路径数
def chess(i,j):
    if i == 1 or j == 1:
        return
    res = chess(i-1,j) + chess(i,j-1)
    return res

print(chess(3,7))