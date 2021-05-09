from src.AVLTree import AVLTree
from src.Segment import Segment

def test_add():
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
