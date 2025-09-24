from node import Node

#创建5个节点，值分别为31、11、20、5、6
node_31 = Node(31)
node_11 = Node(11)
node_20 = Node(20)
node_5 = Node(5)
node_6 = Node(6)
#给31添加左子节点11和右子节点20
node_31.add_leftchild(node_11)
node_31.add_rightchild(node_20)
#给11添加左子节点5和右子节点6
node_11.add_leftchild(node_5)

#删除11的右子节点6
node_11.add_rightchild(node_6)
node_11.delete_rightchild()
