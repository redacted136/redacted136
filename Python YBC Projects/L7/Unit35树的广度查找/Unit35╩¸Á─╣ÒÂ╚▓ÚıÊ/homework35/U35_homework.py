from queue import Queue
from node import Node

#------------------创建二叉树------------------#
node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')
node_G = Node('G')
node_H = Node('H')
node_I = Node('I')

node_A.add_leftchild(node_B)
node_A.add_rightchild(node_C)

node_B.add_leftchild(node_D)
node_B.add_rightchild(node_E)

node_C.add_leftchild(node_F)
node_C.add_rightchild(node_G)

node_E.add_leftchild(node_H)
node_E.add_rightchild(node_I)

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
        if node.value == "H":
            # 退出bfs()函数
            return

        # 如果有左子节点，入队
        if node.left_child:
            q.put(node.left_child)

        # 如果有右子节点，入队
        if node.right_child:
            q.put(node.right_child)

# 调用广度优先搜索函数，从节点A(node_A)开始搜索。
bfs(node_A)



