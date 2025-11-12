from queue import Queue
q = Queue()

#补全代码，让所有人按顺序入队
q.put('爸爸')
q.put('爷爷')
q.put('奶奶')
q.put('壮猿')
q.put('妹妹')
q.put('妈妈')

a=q.get()
print(a)
a=q.get()
print(a)
a=q.get()
print(a)
a=q.get()




#通过出队操作，让壮猿排在第一位
