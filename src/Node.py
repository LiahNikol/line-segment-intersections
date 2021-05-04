# Class representing node in a balanced tree structure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
