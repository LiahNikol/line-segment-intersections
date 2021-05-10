from src.AVLTree import AVLTree
from src.Segment import Segment

def test_add():
    tree = AVLTree()
    # s0 = Segment((0, 0), (10, 0))
    # s1 = Segment((1, 1), (10, 1))
    # s2 = Segment((2, 2), (10, 2))
    s3 = Segment((3, 3), (10, 3))
    s4 = Segment((4, 4), (10, 4))
    s5 = Segment((5, 5), (10, 5))
    s6 = Segment((6, 6), (10, 6))
    s7 = Segment((7, 7), (10, 7))
    # s8 = Segment((8, 8), (10, 8))
    # s9 = Segment((9, 9), (10, 9))

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
    

