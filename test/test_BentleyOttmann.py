from src.BentleyOttmann import bentley_ottman
from src.Intersection import Intersection

def test_bentley_ottman():
    rv = bentley_ottman(([[0, 0], [4, 4]], [[1, 3],[3, 1]]))
    print(rv)
    assert(rv != None)