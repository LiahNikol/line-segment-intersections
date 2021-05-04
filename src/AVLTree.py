# Class represents a balanced binary tree for the sweepline structure in the B-O algorithm
# Advantageous because operations should maintain o(logn) time
from Node import Node

class AVLTree:
    def __init__(self):
        self.size = 0
        self.root = None
        
    def __len__(self):
        return self.size
    
    def inOrder(self):
        inOrderRecursive(self.root)
    
    def inOrderRecursive(self, node)
        if node == None:
            return 
        self.inOrderRecursive(node.getLeft())
        print(node.getValue(), end=" ")
        self.inOrderRecursive(node.getRight())
        
    def add(self, segment):
        addRecursive(self.root, segment)
    
    def addRecursive(self, root, segment):
        if root == None:
            self.size += 1
            return Node(segment)
        
        segX, segY = segment.getLeftEndpoint().coords()
        rootY = root.getValue().getCurrentY(segX)
        if segY < rootY:
            root.left = self.addRecursive(root.left, segment)
        elif segY > rootY:
            root.right = self.addRecursive(root.right, segment)
        else:
            # then this is an intersection
        
        # balancing logic 
        
    def remove(self, segment):
        return removeRecursive(self.root, segment)
        
    def removeRecursive(self, root, segment):    
        segX, segY = segment.getEndpoints()
        if root == None:
            
        
    def swap(self):
        
    def findAbove(self, segment):
    
    def findBelow(self, segment):
    
   
  