# Class representing node in a balanced tree structure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor = 1
