# AVL tree implementation in Python
# Modified from https://www.programiz.com/dsa/avl-tree

import sys

# Create a tree node
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.size = 0
  
    def getSize(self):
        return self.size

    # Function to insert a node
    def insert_node(self, root, key, debug):
        if debug == True:
            print("current key: " + str(key.coords()[0]) + "," + str(key.coords()[1]))
        # Find the correct location and insert the node
        if not root:
            if debug == True:
               print("adding " + str(key.coords()[0]) + "," + str(key.coords()[1]) + " node") 
            self.size += 1    
            return Node(key)
        
        # sorting customization
        targetX, targetY = key.coords()
        currX, currY = root.key.coords()
        
        if targetX != currX:
            if targetX < currX:
                root.left = self.insert_node(root.left, key, True)
            else:
                root.right = self.insert_node(root.right, key, True)
        else:
            if targetY < currY:
                root.left = self.insert_node(root.left, key, True)
            else:
                root.right = self.insert_node(root.right, key, True)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            leftX, leftY = root.left.key.coords()
            if targetX != leftX:
                if targetX < leftX:
                    return self.rightRotate(root)
                else: 
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
            else:
                if targetY < leftY:
                    return self.rightRotate(root)
                else:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)

        if balanceFactor < -1:
            rightX, rightY = root.right.key.coords()
            if targetX != rightX:
                if targetX > rightX:
                    return self.leftRotate(root)
                else: 
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
            else:
                if targetY > rightY:
                    return self.leftRotate(root)
                else:
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
          
        targetX, targetY = key.coords()
        currX, currY = root.key.coords()
        if not (targetX == currX and targetY == currY):
            if targetX != currX:
                if targetX < currX:
                    root.left = self.delete_node(root.left, key)
                elif targetX > currX:
                    root.right = self.delete_node(root.right, key)
            else:
                if targetY < currY:
                    root.left = self.delete_node(root.left, key)
                elif targetY > currY: 
                    root.right = self.delete_node(root.right, key)
        else: # same key
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)  
        print("{0} ".format(root.key.coords()), end="")
        self.inOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(str(currPtr.key.coords()))
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)