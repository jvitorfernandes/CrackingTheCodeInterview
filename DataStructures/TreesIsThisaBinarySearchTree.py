""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
later = []
def checkBST(root, min=-1, max=10001):
    
    if root is None:
        return True
    
    elif(root.data < min or root.data > max):
        return False
    
    return checkBST(root.left, min, root.data-1) and checkBST(root.right, root.data+1, max)