class Node():

    # 初始化节点
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None
        self.up_child = None
        self.down_child = None

    # 增加左子节点
    def add_leftchild(self, node):
        self.left_child = node

    # 增加右子节点
    def add_rightchild(self, node):
        self.right_child = node

    # 增加上子节点
    def add_upchild(self, node):
        self.up_child = node

    # 增加右子节点
    def add_downchild(self, node):
        self.down_child = node
