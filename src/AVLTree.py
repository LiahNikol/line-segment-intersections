# Class represents a balanced binary tree for the sweepline structure in the B-O algorithm
# Advantageous because operations should maintain o(logn) time
from Node import Node
from sweepline_interface import affine_interp

class AVLTree:
    def __init__(self):
        self.size = 0
        self.root = None
        self.intersections = []
        
    def __len__(self):
        return self.size
    
    def inOrder(self):
        self.inOrderRecursive(self.root)
    
    def inOrderRecursive(self, node):
        if node == None:
            return 
        self.inOrderRecursive(node.left)
        print(node.value, end=" ")
        self.inOrderRecursive(node.right)
        
    def get(self, segment):
        return segment.node
        
    def add(self, segment):
        self.root = self.addRecursive(self.root, segment)
    
    def addRecursive(self, root, segment):
        if root == None:
            self.size += 1
            newNode = Node(segment) 
            segment.node = newNode # every segment keeps track of its own node
            return newNode
        
        segX, segY = segment.leftPoint.coords()
        rootY = affine_interp(root.value, segX)
        
        if segY == rootY:
            self.intersections.append(Intersections(segX, rootY, root.value, segment))
            segX, segY = segment.rightPoint.coords()
            rootY = affine_interp(root.value, segX)
        
        if segY < rootY:
            root.left = self.addRecursive(root.left, segment)
            root.left.parent = root
        elif segY > rootY:
            root.right = self.addRecursive(root.right, segment)
            root.right.parent = root
            
        # balancing logic 
        
        return root
        
    def remove(self, segment):
        self.size -= 1
        node = self.get(segment)
        segment.node = None
        if node.left == None and node.right == None: # no children
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        elif node.right == None:
            node.left.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.left == Node:
            node.right.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else: 
            replacementNode = node.right
            while replacementNode.left != None:
                replacementNode = replacementNode.left
            node.value = replacementNode.value
            replacementNode.parent.left = replacementNode.right
            replacementNode.right.parent = replacementNode.parent
            node.value.node = node
            
    def swap(self):
        return #Just so this compiles for now
        
    def findAbove(self, segment):
        # leftmost child of the right subtree
        node = self.get(segment)
        if node.right == None:
            if node.parent == None or node.parent.right == node:
                return None
            else:
                return node.parent.value
            
        aboveNode = node.right
        while aboveNode.left != None:
            aboveNode = aboveNode.left
    
        return aboveNode.value
    
    def findBelow(self, segment):
        # rightmost child of the right subtree
        node = self.get(segment)
        if node.left == None:
            if node.parent == None or node.parent.left == node:
                return None
            else:
                return node.parent.value
            
        belowNode = node.left
        while belowNode.right != None:
            belowNode = belowNode.right
    
        return belowNode.value
  
