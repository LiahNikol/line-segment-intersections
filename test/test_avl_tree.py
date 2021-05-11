from linesegmentintersections.AVLTree import AVLTree
from linesegmentintersections.Segment import Segment

def test_add():
    s0 = Segment((0, 0), (10, 0))
    s1 = Segment((1, 1), (10, 1))
    s2 = Segment((2, 2), (10, 2))
    s3 = Segment((3, 3), (10, 3))
    s4 = Segment((4, 4), (10, 4))
    s5 = Segment((5, 5), (10, 5))
    s6 = Segment((6, 6), (10, 6))
    s7 = Segment((7, 7), (10, 7))
    s8 = Segment((8, 8), (10, 8))
    s9 = Segment((9, 9), (10, 9))

    tree = AVLTree()
    tree.add(s3)
    tree.add(s4)
    tree.add(s5)
    tree.add(s6)
    tree.add(s7)
    
    # tree.inOrder()
    assert tree.root.value == s4
    assert tree.root.left.value == s3
    assert tree.root.right.value == s6
    assert tree.root.right.parent == tree.root
    assert tree.root.left.parent == tree.root
    assert tree.root.parent == None
    assert tree.root.balance_factor == 3



    tree = AVLTree()
    tree.add(s5)
    tree.add(s3)
    tree.add(s7)
    tree.add(s4)
    tree.add(s6)
    tree.add(s2)
    tree.add(s8)

    assert tree.root.value == s5
    assert tree.root.balance_factor == 3



    tree = AVLTree()
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    tree.add(s5)
    tree.add(s6)
    tree.add(s7)
    tree.add(s8)

    assert tree.root.value == s5
    assert tree.root.balance_factor == 3
    assert tree.root.left.value == s3
    assert tree.root.left.balance_factor == 2
    assert tree.root.left.left.value == s2
    assert tree.root.left.left.balance_factor == 1
    assert tree.root.left.left.left == None
    assert tree.root.left.left.right == None
    assert tree.root.left.right.value == s4
    assert tree.root.left.right.balance_factor == 1
    assert tree.root.left.right.left == None
    assert tree.root.left.right.right == None
    assert tree.root.right.value == s7
    assert tree.root.right.balance_factor == 2
    assert tree.root.right.left.value == s6
    assert tree.root.right.left.balance_factor == 1
    assert tree.root.right.left.left == None
    assert tree.root.right.left.right == None
    assert tree.root.right.right.value == s8
    assert tree.root.right.right.balance_factor == 1
    assert tree.root.right.right.left == None
    assert tree.root.right.right.right == None



    tree = AVLTree()
    tree.add(s2)
    tree.add(s4)
    tree.add(s3)

    assert tree.root.value == s3
    assert tree.root.left.value == s2
    assert tree.root.right.value == s4
    assert tree.root.balance_factor == 2



    tree = AVLTree()
    tree.add(s2)
    tree.add(s8)
    tree.add(s3)
    tree.add(s7)
    tree.add(s4)
    tree.add(s5)
    tree.add(s6)

    assert tree.root.value == s4
    assert tree.root.balance_factor == 4
    assert tree.root.left.value == s3
    assert tree.root.left.balance_factor == 2
    assert tree.root.left.left.value == s2
    assert tree.root.left.left.balance_factor == 1
    assert tree.root.left.left.left == None
    assert tree.root.left.left.right == None
    assert tree.root.left.right == None
    assert tree.root.right.value == s7
    assert tree.root.right.balance_factor == 3
    assert tree.root.right.left.value == s5
    assert tree.root.right.left.balance_factor == 2
    assert tree.root.right.left.left == None
    assert tree.root.right.left.right.value == s6
    assert tree.root.right.left.right.left == None
    assert tree.root.right.left.right.right == None
    assert tree.root.right.right.value == s8
    assert tree.root.right.right.balance_factor == 1
    assert tree.root.right.right.left == None
    assert tree.root.right.right.right == None

    

    tree = AVLTree()
    tree.add(s0)
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    tree.add(s5)
    tree.add(s6)
    tree.add(s7)
    tree.add(s8)
    tree.add(s9)

    assert tree.size == 10
    assert tree.root.balance_factor == 4



    tree = AVLTree()
    tree.add(s3)
    tree.add(s0)
    tree.add(s8)
    tree.add(s5)
    tree.add(s9)
    tree.add(s6)
    
    assert tree.size == 6
    assert tree.root.value == s5
    assert tree.root.left.value == s3
    assert tree.root.left.left.value == s0
    assert tree.root.right.value == s8
    assert tree.root.right.left.value == s6
    assert tree.root.right.right.value == s9

    tree = AVLTree()
    tree.add(s3)
    tree.add(s0)
    tree.add(s8)
    tree.add(s5)
    tree.add(s9)
    tree.add(s4)
    
    assert tree.size == 6
    assert tree.root.value == s5
    assert tree.root.left.value == s3
    assert tree.root.left.left.value == s0
    assert tree.root.left.right.value == s4
    assert tree.root.right.value == s8
    assert tree.root.right.right.value == s9


def test_remove():
    s0 = Segment((0, 0), (10, 0))
    s1 = Segment((1, 1), (10, 1))
    s2 = Segment((2, 2), (10, 2))
    s3 = Segment((3, 3), (10, 3))
    s4 = Segment((4, 4), (10, 4))
    s5 = Segment((5, 5), (10, 5))
    s6 = Segment((6, 6), (10, 6))
    s7 = Segment((7, 7), (10, 7))
    s8 = Segment((8, 8), (10, 8))
    s9 = Segment((9, 9), (10, 9))

    tree = AVLTree()
    tree.add(s0)
    assert tree.size == 1
    assert tree.root.value == s0
    tree.remove(s0)
    assert tree.size == 0
    assert tree.root == None



    tree = AVLTree()
    tree.add(s0)
    tree.add(s1)
    assert tree.size == 2
    assert tree.root.value == s0
    tree.remove(s1)
    assert tree.size == 1
    assert tree.root.value == s0

    tree = AVLTree()
    tree.add(s0)
    tree.add(s1)
    assert tree.size == 2
    assert tree.root.value == s0
    tree.remove(s0)
    assert tree.size == 1
    assert tree.root.value == s1

    tree = AVLTree()
    tree.add(s1)
    tree.add(s0)
    assert tree.size == 2
    assert tree.root.value == s1
    tree.remove(s0)
    assert tree.size == 1
    assert tree.root.value == s1

    tree = AVLTree()
    tree.add(s1)
    tree.add(s0)
    assert tree.size == 2
    assert tree.root.value == s1
    tree.remove(s1)
    assert tree.size == 1
    assert tree.root.value == s0



    tree = AVLTree()    
    tree.add(s0)
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    tree.add(s5)
    tree.add(s6)
    tree.add(s7)
    tree.add(s8)
    tree.add(s9)
    assert tree.size == 10
    assert tree.root.value == s3
    assert tree.root.balance_factor == 4
    tree.remove(s2)
    assert tree.size == 9
    assert tree.root.value == s3
    assert tree.root.balance_factor == 4
    tree.remove(s7)
    assert tree.size == 8
    assert tree.root.balance_factor == 4
    assert tree.root.value == s3
    assert tree.root.left.value == s1
    assert tree.root.left.left.value == s0
    assert tree.root.right.value == s8
    assert tree.root.right.left.value == s5
    assert tree.root.right.left.left.value == s4
    assert tree.root.right.left.right.value == s6
    assert tree.root.right.right.value == s9

    tree.remove(s1)
    assert tree.size == 7
    assert tree.root.balance_factor == 3
    assert tree.root.value == s5
    assert tree.root.left.value == s3
    assert tree.root.right.value == s8
    
def test_add_simple():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, -1), (4, 1))
    s3 = Segment((2, 1), (3, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    

def test_remove_simple():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, -1), (4, 1))
    s3 = Segment((2, 1), (3, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    
    tree.inOrder()
    print()
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    
    tree.remove(s1)
    tree.inOrder()
    print()
    assert tree.root.value == s3
    assert tree.root.left.value == s2
    assert tree.root.right is None
    assert len(tree) == 2
    
    tree.remove(s3)
    tree.inOrder()
    print()
    assert tree.root.value == s2
    assert tree.root.left == None
    assert tree.root.right == None
    assert len(tree) == 1
    
    tree.remove(s2)
    tree.inOrder()
    assert tree.root == None
    assert len(tree) == 0
    
def test_swap_simple():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, -1), (4, 1))
    s3 = Segment((2, 1), (3, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    
    tree.swap(s1, s2)
    tree.inOrder()
    assert tree.root.value == s2
    assert tree.root.left.value == s1
    assert tree.root.right.value == s3
    assert len(tree) == 3

def test_findAbove_simple():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, -1), (4, 1))
    s3 = Segment((2, 1), (3, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    
    above = tree.findAbove(s1)
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert above == s3
    
    above = tree.findAbove(s2)
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert above == s1
    
    above = tree.findAbove(s3)
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert above == None

def test_findBelow_simple():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, -1), (4, 1))
    s3 = Segment((2, 1), (3, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    
    below = tree.findBelow(s1)
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert below == s2
    
    below = tree.findBelow(s2)
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert below == None
    
    below = tree.findBelow(s3)
    assert tree.root.value == s1
    assert tree.root.left.value == s2
    assert tree.root.right.value == s3
    assert len(tree) == 3
    assert below == s1
    
def test_findAbove_leftbent():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, 2), (5, -1))
    s3 = Segment((2, -2), (6, 0))
    s4 = Segment((3, -1), (6, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s3
    assert tree.root.right.value == s2
    assert tree.root.left.right.value == s4
    assert len(tree) == 4
    
    above = tree.findAbove(s1)
    assert above == s2
    
    above = tree.findAbove(s2)
    assert above == None
    
    above = tree.findAbove(s3)
    assert above == s4
    
    above = tree.findAbove(s4)
    assert above == s1
    
    print()
    tree.inOrder()
    
def test_findBelow_leftbent():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, 2), (5, -1))
    s3 = Segment((2, -2), (6, 0))
    s4 = Segment((3, -1), (6, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s3
    assert tree.root.right.value == s2
    assert tree.root.left.right.value == s4
    assert len(tree) == 4
    
    below = tree.findBelow(s1)
    assert below == s4
    
    below = tree.findBelow(s2)
    assert below == s1
    
    below = tree.findBelow(s3)
    assert below == None
    
    below = tree.findBelow(s4)
    assert below == s3
    
    print()
    tree.inOrder()
    
def test_findAbove_rightbent():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, 5), (5, -1))
    s3 = Segment((2, -2), (6, 0))
    s4 = Segment((3, 1), (6, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s3
    assert tree.root.right.value == s2
    assert tree.root.right.left.value == s4
    assert len(tree) == 4
    
    above = tree.findAbove(s1)
    assert above == s4
    
    above = tree.findAbove(s2)
    assert above == None
    
    above = tree.findAbove(s3)
    assert above == s1
    
    above = tree.findAbove(s4)
    assert above == s2
    
    print()
    tree.inOrder()
    
def test_findBelow_rightbent():
    tree = AVLTree()
    s1 = Segment((0, 0), (5, 0))
    s2 = Segment((1, 5), (5, -1))
    s3 = Segment((2, -2), (6, 0))
    s4 = Segment((3, 1), (6, 1))
    tree.add(s1)
    tree.add(s2)
    tree.add(s3)
    tree.add(s4)
    
    tree.inOrder()
    assert tree.root.value == s1
    assert tree.root.left.value == s3
    assert tree.root.right.value == s2
    assert tree.root.right.left.value == s4
    assert len(tree) == 4
    
    below = tree.findBelow(s1)
    assert below == s3
    
    below = tree.findBelow(s2)
    assert below == s4
    
    below = tree.findBelow(s3)
    assert below == None
    
    below = tree.findBelow(s4)
    assert below == s1
    
    print()
    tree.inOrder()    


