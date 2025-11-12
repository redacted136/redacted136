from queue import Queue
import random


students = ['壮猿', '大象', '马', '猫', '狐狸', '狗', '熊猫', '猪']
# 游戏队伍：创建一个数据量最大为8的队列
game_q = Queue(8)
# 按顺序入队
for s in students:
    game_q.put(s)
# 在1~8中随机抽取一个游戏数字
num = random.randint(1, 8)
print('如果报数为' + str(num) + '，则离开游戏队伍')