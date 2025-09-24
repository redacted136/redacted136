from node_new import Node

# 实例化节点
node_10 = Node(10)
node_20 = Node(20)
node_30 = Node(30)
node_40 = Node(40)
node_31 = Node(31)
node_32 = Node(32)
node_33 = Node(33)

# 添加node_10节点的子节点
node_10.add_leftchild(node_20)
node_10.add_midchild(node_30)
node_10.add_rightchild(node_40)
# 添加node_30节点的左子节点
node_30.add_leftchild(node_31)
# 添加node_30节点的中子节点
node_30.add_midchild(node_32)
# 添加node_30节点的右子节点
node_30.add_rightchild(node_33)



