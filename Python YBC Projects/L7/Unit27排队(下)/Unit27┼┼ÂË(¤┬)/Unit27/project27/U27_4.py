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

# 记录报数（初始值为0）
count = 0
# 依次报数，直到游戏队伍剩余1人。
while game_q.qsize() > 1 :

    # 定义一个变量，记录当前出队的同学
    stu = game_q.get()
    # 报数
    count = count +1
    # 如果报数为num，则离开队伍，报数重新开始
    # 否则，回到队尾继续等待报数
    if count == num:
        count = 0
    else:
        game_q.put(stu)

print(game_q.get())