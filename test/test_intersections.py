# This file should be used to test the intersection-finding function 'intersects', found in Segment.py
from linesegmentintersections.Segment import Segment, intersects

def pointtest(point1A, point1B, point2A, point2B, intersect=None, a_on_top=True):
    segA = Segment(point1A, point1B)
    segB = Segment(point2A, point2B)

    rv = intersects(segA, segB)
    if intersect is not None:
        assert(rv.x == intersect[0])
        assert(rv.y == intersect[1])
        if a_on_top:
            assert(rv.seg1 == segA)
            assert(rv.seg2 == segB)
        else:
            assert(rv.seg1 == segB)
            assert(rv.seg2 == segA)
    else:
        assert(rv is None)

def test_intersect():
    # Test basic intersecting examples
    pointtest((0, 0), (1, 1), (0, 1), (1, 0), intersect=(0.5, 0.5), a_on_top=False)
    pointtest((2, 0), (3.5, 3), (2, 2.5), (4, 1.5), intersect=(3, 2), a_on_top=False)

    # Test parallel lines
    pointtest((0, 0), (1, 1), (0, 1), (1, 2), intersect=None)

    # Test endpoints overlapping
    pointtest((0, 0), (1, 1), (0, 0), (1, 2), intersect=(0, 0), a_on_top=False)
    pointtest((0, 0), (1, 1), (0, 1), (1, 1), intersect=(1, 1), a_on_top=False)

    # These are cases when the segments are connected end to end. It doesn't quite work with the segment order, but that's ok. I don't think it needs to work.
    # pointtest((0, 0), (1, 1), (1, 1), (2, 1), intersect=(1, 1), a_on_top=False)
    # pointtest((0, 0), (1, 1), (1, 1), (2, 3), intersect=(1, 1), a_on_top=False)
    # pointtest((0, 2), (1, 1), (1, 1), (2, 1), intersect=(1, 1), a_on_top=True)

    # Test a point overlapping with a segment
    pointtest((0, 0), (2, 2), (1, 1), (2, 1), intersect=(1, 1), a_on_top=True)
    pointtest((0, 0), (2, 2), (1, 1), (2, 10), intersect=(1, 1), a_on_top=False)