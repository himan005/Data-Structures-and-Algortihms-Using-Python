class BinaryTree:

    def __init__(self, root, left = None, right = None):

        self.key = root
        self.left = left
        self.right = right

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):



