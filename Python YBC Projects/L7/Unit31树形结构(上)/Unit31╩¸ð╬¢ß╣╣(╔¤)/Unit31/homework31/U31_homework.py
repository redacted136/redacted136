from node import Node

#创建3个节点，值分别为30、10、20，请补充值为20的节点
node_30 = Node(30)
node_10 = Node(10)
node_20 = Node(20)
#给30添加左子节点10和右子节点20
node_30.add_rightchild(node_20)

