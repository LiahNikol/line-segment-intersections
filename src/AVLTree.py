# Class represents a balanced binary tree for the sweepline structure in the B-O algorithm
# Advantageous because operations should maintain o(logn) time
from .Node import Node
from .sweepline_interface import affine_interp

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
        restructure(root)
        
        # update current root's height
        updateBalanceFactor(root)
        
        return root
    
    def restructure(self, root):
        balanceLeft = 0 if root.left == None else root.left.balance_factor
        balanceRight = 0 if root.right == None else root.right.balance_factor
        if Math.abs(balanceLeft - balanceRight) <= 1:
            return
            
        z = root
        zLeftChild = False
        y = None
        
        if root.right != None and root.left == None:
            y = root.right
            zLeftChild = False
        elif root.left != None and root.right == None:
            y = root.left
            zLeftChild = True
        else:
            if root.left.balance_factor > root.right.balance_factor:
                y = root.left
                zLeftChild = True
            else:
                y = root.right
                zLeftChild = False
                
        x = None
        yLeftChild = False
        
        if y.right != None and y.left == None:
            x = root.right
            yLeftChild = False
        elif y.left != None and y.right == None:
            x = root.left
            yLeftChild = True
        else:
            if y.left.balance_factor > y.right.balance_factor:
                x = root.left
                yLeftChild = True
            else:
                x = y.right
                yLeftChild = False
        
        # rebalancing
        if zLeftChild != yLeftChild:
            # bent
            if zLeftChild:
                y.right = x.left
                x.left = y 
                y.right.parent  = y
                y.parent = x
                x.parent = z
                z.left = x
            else:
                y.left = x.right
                x.right = y
                y.left.parent = y
                y.parent = x
                x.parent = z
                z.right = x
            temp = x
            x = y
            y = temp
        
        # in line
        if zLeftChild:
            z.left = y.right
            z.left.parent = z
            tempParent = z.parent
            z.parent = y
            y.right = z
            y.parent = tempParent
            if tempParent != None:
                if tempParent.left == z:
                    tempParent.left = y
                else:
                    tempParent.right = y
        else:
            z.right = y.left
            z.right.parent = z
            tempParent = z.parent
            z.parent = y
            y.left = z
            y.parent = tempParent
            if tempParent != None:
                if tempParent.left == z:
                    tempParent.left = y
                else:
                    tempParent.right = y
        
        updateBalanceFactor(x)
        updateBalanceFactor(z)
        updateBalanceFactor(y)
        
    def updateBalanceFactor(self, node):
        balanceLeft = 0 if root.left == None else root.left.balance_factor
        balanceRight = 0 if root.right == None else root.right.balance_factor
        node.balance_factor = Math.max(balanceLeft, balanceRight) 
        
    def remove(self, segment):
        restructureStart = None
        self.size -= 1
        node = self.get(segment)
        segment.node = None
        if node.left == None and node.right == None: # no children
            if node.parent != None:
                if node.parent.left == node: # determine whether removal node is left or right child
                    node.parent.left = None
                else:
                    node.parent.right = None
                # balance
                restructureStart = node.parent
            else:
                self.root = None
        elif node.right == None: # only left child present
            node.left.parent = node.parent # connecting present child to node's parent
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            # balance
            restructureStart = node.parent
        elif node.left == Node: # only right child present
            node.right.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            # balance
            restructureStart = node.parent
        else: # both children present
            replacementNode = node.right
            while replacementNode.left != None:
                replacementNode = replacementNode.left
            # balance
            restructureStart = replacementNode.parent
            node.value = replacementNode.value
            replacementNode.parent.left = replacementNode.right
            replacementNode.right.parent = replacementNode.parent
            node.value.node = node
        
        while restructureStart != None:
            restructure(restructureStart)
            updateBalanceFactor(restructureStart)
            restructureStart = restructureStart.parent
            
        return
        
    def swap(self, seg1, seg2):
        seg1.node.value = seg2
        seg2.node.value = seg1
        temp = seg1.node
        seg1.node = seg2.node
        seg2.node = temp
        return
        
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
    
