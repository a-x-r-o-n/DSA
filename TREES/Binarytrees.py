class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None
if __name__ == '__main__':
    t = Tree()
    t.root = TreeNode(1)
    t.root.left = TreeNode(2)
    t.root.right = TreeNode(3)
