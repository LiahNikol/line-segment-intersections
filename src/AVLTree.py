# Class represents a balanced binary tree for the sweepline structure in the B-O algorithm
# Advantageous because operations should maintain o(logn) time
from .Node import Node
from .sweepline_interface import affine_interp
from .Intersection import Intersection

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
        # Base case, when we've reached a leaf (None)
        if root == None:
            # Grow the size of the tree and create the new node
            self.size += 1
            newNode = Node(segment) 
            segment.node = newNode # every segment keeps track of its own node
            return newNode
        
        # Obtain the y values to compare upon entry
        segX, segY = segment.leftPoint.coords()
        rootY = affine_interp(root.value, segX)
        
        # If the y values are the same, we'll compare at the right endpoint
        if segY == rootY:
            # We also want to keep track of this endpoint intersection
            self.intersections.append(Intersection(segX, rootY, root.value, segment))
            segX, segY = segment.rightPoint.coords()
            rootY = affine_interp(root.value, segX)
        
        if segY < rootY:
            root.left = self.addRecursive(root.left, segment)
            root.left.parent = root
        elif segY > rootY:
            root.right = self.addRecursive(root.right, segment)
            root.right.parent = root
            
        # balancing logic 
        newroot = self.restructure(root)
        if newroot != None:
            return newroot
        else:
            # update current root's height
            self.updateBalanceFactor(root)
            return root
    
    def restructure(self, root):
        # Check to see if we need to perform a rebalancing
        balanceLeft = 0 if root.left == None else root.left.balance_factor
        balanceRight = 0 if root.right == None else root.right.balance_factor
        if abs(balanceLeft - balanceRight) <= 1:
            return None
            
        # Instantiate the nodes we're going to restructure
        z = root
        zLeftChild = False
        y = None
        yLeftChild = False
        x = None
        
        # Selecting our second-from-the-top node
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
                
        # Selecting our bottommost node
        if y.right != None and y.left == None:
            x = y.right
            yLeftChild = False
        elif y.left != None and y.right == None:
            x = y.left
            yLeftChild = True
        else:
            if y.left.balance_factor > y.right.balance_factor:
                x = y.left
                yLeftChild = True
            else:
                x = y.right
                yLeftChild = False
        
        # Rebalancing a dog-legged set of nodes
        if zLeftChild != yLeftChild:
            # On the left side
            if zLeftChild:
                y.right = x.left
                x.left = y 
                if y.right != None:
                    y.right.parent  = y
                y.parent = x
                x.parent = z
                z.left = x
            # On the right side
            else:
                y.left = x.right
                x.right = y
                if y.left != None:
                    y.left.parent = y
                y.parent = x
                x.parent = z
                z.right = x
            # Update our node pointers so the in-order restructuring will work
            temp = x
            x = y
            y = temp
        
        # Rebalancing in-order set of nodes
        # Going to the left
        if zLeftChild:
            z.left = y.right
            if z.left != None:
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
                self.root = y
        # Going to the right
        else:
            z.right = y.left
            if z.right != None:
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
            else:
                self.root = y
        
        # Update all of our balance factors
        self.updateBalanceFactor(x)
        self.updateBalanceFactor(z)
        self.updateBalanceFactor(y)

        # Return the topmost node
        return y
        
    # This method updates the balance factor for a node,
    # by setting its balance factor to 1 + the maximum balance factor
    # of its children
    # Children that == None count as a balance factor of 0
    def updateBalanceFactor(self, node):
        balanceLeft = 0 if node.left == None else node.left.balance_factor
        balanceRight = 0 if node.right == None else node.right.balance_factor
        node.balance_factor = max(balanceLeft, balanceRight) + 1
        
    # Remove a segment from the tree
    # Assumes that the segment is in the tree
    def remove(self, segment):
        # Take care of minor housekeeping details
        restructureStart = None
        self.size -= 1
        node = self.get(segment)
        segment.node = None

        # Perform removal of the node
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
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                self.root = node.left
            # balance
            restructureStart = node.parent
        elif node.left == Node: # only right child present
            node.right.parent = node.parent
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right
            # balance
            restructureStart = node.parent
        else: # both children present
            # We have to replace the node with the in-order successor
            replacementNode = node.right
            while replacementNode.left != None:
                replacementNode = replacementNode.left
            restructureStart = replacementNode.parent
            # We have to handle things differently if the replacement node is the right child,
            # or a left child of the right child
            if replacementNode.parent == node:
                # Slide over the replacement value, and skip the 
                # replacement node
                node.right = replacementNode.right
                if node.right != None:
                    node.right.parent = node
            else:
                # If we're replacing with a left child of the node's right child
                replacementNode.parent.left = replacementNode.right
                if replacementNode.right != None:
                    replacementNode.right.parent = replacementNode.parent
            # Update the connection between the replacement segment and its new node
            node.value = replacementNode.value
            node.value.node = node
        
        # Perform restructuring starting from the indicated first affected node
        while restructureStart != None:
            self.restructure(restructureStart)
            self.updateBalanceFactor(restructureStart)
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
            if node.parent == None:
                return None
            else:
                aboveNode = node.parent
                previousNode = node
                while (aboveNode.right == previousNode):
                    if aboveNode.parent == None:
                        return None
                    previousNode = aboveNode
                    aboveNode = aboveNode.parent
                return aboveNode.value
            
        aboveNode = node.right
        while aboveNode.left != None:
            aboveNode = aboveNode.left
    
        return aboveNode.value
    
    def findBelow(self, segment):
        # rightmost child of the right subtree
        node = self.get(segment)
        if node.left == None:
            if node.parent == None:
                return None
            else:
                belowNode = node.parent
                previousNode = node
                while (belowNode.left == previousNode):
                    if belowNode.parent == None:
                        return None
                    previousNode = belowNode
                    belowNode = belowNode.parent
                return belowNode.value
            
        belowNode = node.left
        while belowNode.right != None:
            belowNode = belowNode.right
    
        return belowNode.value
    
