from queue import Queue


family = ['壮猿爸爸', '壮猿爷爷', '壮猿奶奶', '壮猿妈妈', '猿小妹', '壮猿']

# 创建一个数据量为6的安检队列
q1 = Queue(6)
# 遍历family列表，使壮猿一家入队
for f in family:
    q1.put(f)

# 循环出队知道安检队列中没有元素
while q1.qsize() >0:
    print('滴！安检完成！')
    print(q1.get() + '，请出队！')
