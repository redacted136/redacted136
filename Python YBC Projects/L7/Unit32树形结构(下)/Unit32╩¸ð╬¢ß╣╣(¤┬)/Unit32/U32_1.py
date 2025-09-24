from node import Node

node_10 = Node(10)
node_20 = Node(20)
node_30 = Node(30)
node_40 = Node(40)
node_50 = Node(50)
node_60 = Node(60)
node_70 = Node(70)

node_40.add_leftchild(node_20)
node_40.add_rightchild(node_60)
node_20.add_leftchild(node_10)
node_20.add_rightchild(node_30)
node_60.add_leftchild(node_50)
node_60.add_rightchild(node_70)

#-------------------------------------搜索二叉排序树------------------------------------------#
def search(goal, start):

    if goal == start.value:
        print('已找到值为'+str(goal)+'的节点。')
        return

    if start.left_child is None and start.right_child is None:
        print('树中没有值为'+str(goal)+'的节点。')
        return

    if goal < start.value:
        # 将起始节点的左子节点作为新的起始节点进行搜索
        search(goal,start.left_child)

    if goal > start.value:
        # 将起始节点的右子节点作为新的起始节点进行搜索
        search(goal.start.right_child)

search(80, node_40)








