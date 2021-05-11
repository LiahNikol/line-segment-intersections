from linesegmentintersections.BentleyOttmann import bentley_ottman
from linesegmentintersections.Intersection import Intersection

def test_bentley_ottman():
    rv = bentley_ottman(([[0, 0], [4, 4]], [[1, 3],[3, 1]]))
    assert(len(rv) == 1)
    assert(rv[0].x == 2)
    assert(rv[0].y == 2)