from src.AVLTree import AVLTree
from src.Segment import Segment


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

