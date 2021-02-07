'''
Caitlin J. Corbin
2020.07.27
19.2
Intro to Python
'''

# Binary tree function
def isFullBinaryTree(self):
    return CheckFullBinaryTree(self.root);


# Checks whether a binary tree is full or empty
def checkFullBinaryTree(self, root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (CheckFullBinaryTree(root.left) and CheckFullBinaryTree(root.right))
    return False
