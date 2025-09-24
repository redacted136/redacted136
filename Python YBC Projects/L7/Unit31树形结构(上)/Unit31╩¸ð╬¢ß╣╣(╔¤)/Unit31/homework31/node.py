class Node():
    # 初始化节点，需设定节点的值，左右子节点不需要设置，默认为空
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None
    # 增加左子节点
    def add_leftchild(self, node):
        self.left_child = node
    # 增加右子节点
    def add_rightchild(self, node):
        self.right_child = node
    # 删除左子节点
    def delete_leftchild(self):
        self.left_child = None
    # 删除右子节点
    def delete_rightchild(self):
        self.right_child = None
