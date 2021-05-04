# Test class for testing the priority queue data structure used in B-O sweepline algorithm
from src.PriorityQueue import PriorityQueue
from src.Segment import Segment
from src.Intersection import Intersection


def test_add_endpoints():
    pq = PriorityQueue()
    s1 = Segment((2, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    for i in range(0, len(segments)):
        seg = segments[i]
        for endpoint in seg.getEndpoints():
            pq.add(endpoint)
    assert len(pq) == 6, "Length of priority queue was " + len(pq)
    print(pq)
    
def test_add_intersections():
    pq = PriorityQueue()
    i1 = Intersection(7, 5)
    i2 = Intersection(9, 7)
    i3 = Intersection(3, 5)
    intersections = [i1, i2, i3]
    for intersection in intersections:
        pq.add(intersection)
    assert len(pq) == 3, "Length of priority queue was " + len(pq)
    print(pq)

# Test that both types of events are ordered correctly in the priority queue
def test_add_events():
    pq = PriorityQueue()
    s1 = Segment((1, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    for i in range(0, len(segments)):
        seg = segments[i]
        for endpoint in seg.getEndpoints():
            pq.add(endpoint)
            
    i1 = Intersection(7, 5)
    i2 = Intersection(9, 7)
    i3 = Intersection(3, 5)
    intersections = [i1, i2, i3]
    for intersection in intersections:
        pq.add(intersection)
            
    assert len(pq) == 9, "Length of priority queue was " + len(pq)
    print(pq)

def test_remove_min():
    pq = PriorityQueue()
    s1 = Segment((1, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    for i in range(0, len(segments)):
        seg = segments[i]
        for endpoint in seg.getEndpoints():
            pq.add(endpoint)
            
    i1 = Intersection(7, 5)
    i2 = Intersection(2, 4)
    i3 = Intersection(3, 5)
    intersections = [i1, i2, i3]
    for intersection in intersections:
        pq.add(intersection)
    
    assert len(pq) == 9, "Length of priority queue was " + len(pq)
    print(pq)
    
    min = pq.remove_min()
    assert min == s1.getEndpoints()[0]
    min = pq.remove_min()
    assert min == i2
    min = pq.remove_min()
    assert min == s2.getEndpoints()[0]
    min = pq.remove_min()
    assert min == i3
    min = pq.remove_min()
    assert min == s3.getEndpoints()[0]
    min = pq.remove_min()
    assert min == s1.getEndpoints()[1]
    min = pq.remove_min()
    assert min == s2.getEndpoints()[1]
    min = pq.remove_min()
    assert min == s3.getEndpoints()[1]
    min = pq.remove_min()
    assert min == i1
    assert len(pq) == 0, "Length of priority queue was " + len(pq)
    print(pq)
    
def test_contains_intersection():
    pq = PriorityQueue()
    i1 = Intersection(7, 5)
    i2 = Intersection(9, 7)
    i3 = Intersection(3, 5)
    intersections = [i1, i2, i3]
    for intersection in intersections:
        pq.add(intersection)
            
    i4 = Intersection(7, 5)        
    assert pq.containsIntersection(i4) == True
    print(pq)