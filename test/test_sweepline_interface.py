from src.sweepline_interface import sweepline
from src.Segment import Segment

# Build test segments
segs = []
segs.append(Segment(( 0, 10), (10, 10))) # 0
segs.append(Segment(( 0,  9), (10,  9))) # 1
segs.append(Segment(( 0,  8), (10,  8))) # 2
segs.append(Segment(( 5,  7), (10,  7))) # 3
segs.append(Segment(( 0,  6), (10,  6))) # 4
segs.append(Segment(( 0,  5), (10,  5))) # 5

sl = sweepline()

# Test addition
def test_add():
    rv = sl.add(segs[0])
    assert(rv == 0)
    assert(len(sl) == 1)

    rv = sl.add(segs[5])
    assert(rv == 1)
    assert(len(sl) == 2)

    rv = sl.add(segs[2])
    assert(rv == 1)
    assert(len(sl) == 3)

    rv = sl.add(segs[3])
    assert(rv == 2)
    assert(len(sl) == 4)



# Test removal

# Test findAbove and findBelow

# Test swap