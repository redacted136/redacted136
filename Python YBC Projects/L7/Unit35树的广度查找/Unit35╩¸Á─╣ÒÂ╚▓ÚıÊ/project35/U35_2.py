from queue import Queue
from node import Node

node_10 = Node(10)
node_20 = Node(20)
node_30 = Node(30)
node_40 = Node(40)
node_50 = Node(50)
node_60 = Node(60)
node_70 = Node(70)

node_10.add_leftchild(node_20)
node_10.add_rightchild(node_30)
node_20.add_leftchild(node_40)
node_20.add_rightchild(node_50)
node_30.add_leftchild(node_60)
node_30.add_rightchild(node_70)


#--------------------------广度优先搜索--------------------------#


def bfs(node):

    # 创建队列
    q = Queue()

    # 将根节点加入队列
    q.put(node)

    # 如果队列不为空
    while q.qsize() != 0:

        # 获取节点（出队）
        node = q.get()

        # 存储查找到的节点
        print(node.value)

        # 如果当前节点值等于目标节点值:
        ?
            # 退出bfs()函数
            ?

        # 如果有左子节点，入队
        if node.left_child:
            q.put(node.left_child)

        # 如果有右子节点，入队
        if node.right_child:
            q.put(node.right_child)


bfs(node_10)


