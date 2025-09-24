class Node():

    # 初始化节点
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.mid_child = None
        self.right_child = None

    # 增加左子节点
    def add_leftchild(self, node):
        self.left_child = node

    # 增加中子节点
    def add_midchild(self, node):
        self.mid_child = node

    # 增加右子节点
    def add_rightchild(self, node):
        self.right_child = node

    # 删除左子节点
    def delete_leftchild(self):
        self.left_child = None

    # 删除中子节点
    def delete_midchild(self):
        self.mid_child = None

    # 删除右子节点
    def delete_rightchild(self):
        self.right_child = None