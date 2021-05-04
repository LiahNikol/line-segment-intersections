from src.sweepline_interface import sweepline
from src.Segment import Segment

# Build test segments
segs = []
segs.append(Segment(( 0, 10), (10, 10))) # 0
segs.append(Segment(( 0,  9), (10,  8))) # 1
segs.append(Segment(( 0,  8), (10,  9))) # 2
segs.append(Segment(( 5,  7), (10,  7))) # 3
segs.append(Segment(( 0,  6), (10,  6))) # 4
segs.append(Segment(( 0,  5), (10,  5))) # 5

# Test addition
def test_add():
    sl = sweepline()

    rv = sl.add(segs[0])
    assert(rv == 0)
    assert(len(sl) == 1)

    rv = sl.add(segs[5])
    assert(rv == 1)
    assert(len(sl) == 2)

    rv = sl.add(segs[3])
    assert(rv == 1)
    assert(len(sl) == 3)

    rv = sl.add(segs[4])
    assert(rv == 2)
    assert(len(sl) == 4)

    rv = sl.add(segs[1])
    assert(rv == 1)
    assert(len(sl) == 5)

    rv = sl.add(segs[2])
    assert(rv == 2)
    assert(len(sl) == 6)

# Test removal
def test_remove():
    sl = sweepline()
    for s in segs:
        sl.add(s)

    sl.remove(segs[0])
    assert(len(sl) == 5)

    try:
        sl.remove(segs[0])
        assert(False)
    except:
        assert(len(sl) == 5)

    sl.remove(segs[1])
    assert(len(sl) == 4)

    sl.remove(segs[2])
    assert(len(sl) == 3)

    sl.remove(segs[3])
    assert(len(sl) == 2)

    sl.remove(segs[4])
    assert(len(sl) == 1)

    sl.remove(segs[5])
    assert(len(sl) == 0)

# Test findAbove and findBelow
def test_find_above():
    sl = sweepline()
    for s in segs:
        sl.add(s)

    s = sl.findAbove(segs[0])
    assert(s == None)

    s = sl.findAbove(segs[1])
    assert(s == segs[0])

    s = sl.findAbove(segs[2])
    assert(s == segs[1])

    s = sl.findAbove(segs[3])
    assert(s == segs[2])

    s = sl.findAbove(segs[4])
    assert(s == segs[3])

    s = sl.findAbove(segs[5])
    assert(s == segs[4])

def test_find_below():
    sl = sweepline()
    for s in segs:
        sl.add(s)

    s = sl.findBelow(segs[0])
    assert(s == segs[1])

    s = sl.findBelow(segs[1])
    assert(s == segs[2])

    s = sl.findBelow(segs[2])
    assert(s == segs[3])

    s = sl.findBelow(segs[3])
    assert(s == segs[4])

    s = sl.findBelow(segs[4])
    assert(s == segs[5])

    s = sl.findBelow(segs[5])
    assert(s == None)


# Test swap
def test_swap():
    sl = sweepline()
    sl.add(segs[4])
    sl.add(segs[5])

    sl.swap(segs[4], segs[5])
    assert(len(sl) == 2)
    elements = sl.inOrder()
    assert(elements[0] == segs[5])
    assert(elements[1] == segs[4])

    sl.add(segs[0])
    assert(len(sl) == 3)
    try:
        sl.swap(segs[4], segs[0])
        assert(False)
    except:
        assert(True)
        elements = sl.inOrder()
        assert(elements[0] == segs[0])
        assert(elements[1] == segs[5])
        assert(elements[2] == segs[4])
