# Test class for testing the priority queue data structure used in B-O sweepline algorithm
from linesegmentintersections.PriorityQueue import PriorityQueue
from linesegmentintersections.Segment import Segment
from linesegmentintersections.Intersection import Intersection
from linesegmentintersections.Endpoint import Endpoint
    
def test_add_each_endpoints():
    pq = PriorityQueue()
    s1 = Segment((2, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    
    for i in range(0, len(segments)):
        seg = segments[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)
        
    print(pq)
    assert len(pq) == 6, "Length of priority queue was " + str(len(pq))
    
def test_add_each_intersections():
    pq = PriorityQueue()
    s1 = Segment((0, 2), (2, 0))
    s2 = Segment((0, 0), (2, 2))
    s3 = Segment((3, 2), (7, 6))
    s4 = Segment((3, 6), (7, 2))
    i1 = Intersection(1, 1, s1, s2)
    i2 = Intersection(5, 4, s3, s4)
    intersections = [i1, i2]
    
    pq.add_each(intersections)
    
    assert len(pq) == 2, "Length of priority queue was " + str(len(pq))
    
    # try to add a singular intersection
    # This shouldn't work because there's already an intersection for these segments in the pq
    i3 = Intersection(4, 6, s1, s2)
    i4 = Intersection(4, 6, s2, s1)
    pq.add_each([i3, i4])
    
    print(pq)
    assert len(pq) == 2, "Length of priority queue was " + str(len(pq))

# Test that both types of events are ordered correctly in the priority queue
def test_add_each_events():
    pq = PriorityQueue()
    s1 = Segment((1, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    for i in range(0, len(segments)):
        seg = segments[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)

    s4 = Segment((0, 2), (2, 0))
    s5 = Segment((0, 0), (2, 2))
    s6 = Segment((3, 2), (7, 6))
    s7 = Segment((3, 6), (7, 2))
    i1 = Intersection(1, 1, s4, s5)
    i2 = Intersection(5, 4, s6, s7)
    intersections = [i1, i2]
    pq.add_each(intersections)
            
    print(pq)
    assert len(pq) == 8, "Length of priority queue was " + str(len(pq))

def test_remove_min():
    pq = PriorityQueue()
    s1 = Segment((1, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    for i in range(0, len(segments)):
        seg = segments[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)
            
    s4 = Segment((0, 2), (2, 0))
    s5 = Segment((0, 0), (2, 2))
    s6 = Segment((3, 2), (7, 6))
    s7 = Segment((3, 6), (7, 2))
    i1 = Intersection(1, 1, s4, s5)
    i2 = Intersection(5, 4, s6, s7)
    intersections = [i1, i2]
    pq.add_each(intersections)
    
    print(pq)
    assert len(pq) == 8, "Length of priority queue was " + str(len(pq))
    
    # check that queue is sorted 
    
    min = pq.remove_min()
    assert min == i1
    min = pq.remove_min()
    assert min == s1.getEndpoints()[0]
    min = pq.remove_min()
    assert min == s2.getEndpoints()[0]
    min = pq.remove_min()
    assert min == s3.getEndpoints()[0]
    min = pq.remove_min()
    assert min == s1.getEndpoints()[1]
    min = pq.remove_min()
    assert min == i2
    min = pq.remove_min()
    assert min == s2.getEndpoints()[1]
    min = pq.remove_min()
    assert min == s3.getEndpoints()[1]
    
    print(pq)
    assert len(pq) == 0, "Length of priority queue was " + str(len(pq))

def test_initialize_event_queue():
    eq = PriorityQueue()
    s1 = Segment((2, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    eq.initialize_event_queue([((2, 4), (4, 6)), ((2, 6), (5, 5)), ((3, 7), (6, 8))])
    
    assert len(eq) == 6, "Length of priority queue was " + str(len(eq))
    
    # check that queue is sorted
    
    min = eq.remove_min()
    assert min == s1.getEndpoints()[0]
    min = eq.remove_min()
    assert min == s2.getEndpoints()[0]
    min = eq.remove_min()
    assert min == s3.getEndpoints()[0]
    min = eq.remove_min()
    assert min == s1.getEndpoints()[1]
    min = eq.remove_min()
    assert min == s2.getEndpoints()[1]
    min = eq.remove_min()
    assert min == s3.getEndpoints()[1]
    
    print(eq)
    assert len(eq) == 0, "Length of priority queue was " + str(len(eq))
    
def test_contains_event():
    pq = PriorityQueue()
    s1 = Segment((2, 4), (4, 6))
    s2 = Segment((2, 6), (5, 5))
    s3 = Segment((3, 7), (6, 8))
    segments = [s1, s2, s3]
    
    for i in range(0, len(segments)):
        seg = segments[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)
    
    s4 = Segment((0, 2), (2, 0))
    s5 = Segment((0, 0), (2, 2))
    s6 = Segment((3, 2), (7, 6))
    s7 = Segment((3, 6), (7, 2))
    i1 = Intersection(1, 1, s4, s5)
    i2 = Intersection(5, 4, s6, s7)
    intersections = [i1, i2]
    pq.add_each(intersections)
    
    print(pq)
    assert len(pq) == 8, "Length of priority queue was " + str(len(pq))
    
    assert pq.containsEvent(s1.getEndpoints()[0]) == True, "Priority queue did not contain (2, 4)"
    assert pq.containsEvent(s1.getEndpoints()[1]) == True, "Priority queue did not contain (4, 6)"
    assert pq.containsEvent(s2.getEndpoints()[0]) == True, "Priority queue did not contain (2, 6)"
    assert pq.containsEvent(s2.getEndpoints()[1]) == True, "Priority queue did not contain (5, 5)"
    assert pq.containsEvent(s3.getEndpoints()[0]) == True, "Priority queue did not contain (3, 7)"
    assert pq.containsEvent(s3.getEndpoints()[1]) == True, "Priority queue did not contain (6, 8)"
    assert pq.containsEvent(i1) == True, "Priority queue did not contain (1, 1)"
    assert pq.containsEvent(i2) == True, "Priority queue did not contain (5, 4)"
    print(pq)
    
    # Test events that are not contained in the list, including segments with swapped endpoints
    
    s8 = Segment((1, 2), (3, 4))
    s9 = Segment((4, 6), (2, 4)) 
    i3 = Intersection(4, 5, s8, s9)
    i4 = Intersection(5, 7, s8, s9)
    
    assert pq.containsEvent(s8.getEndpoints()[0]) == False, "Priority queue did contain (1, 2)"
    assert pq.containsEvent(s8.getEndpoints()[1]) == False, "Priority queue did contain (3, 4)"
    # assert pq.containsEvent(s9.getEndpoints()[0]) == False, "Priority queue did contain (4, 6)"
    # assert pq.containsEvent(s9.getEndpoints()[1]) == False, "Priority queue did contain (2, 4)"
    assert pq.containsEvent(i3) == False, "Priority queue did contain (4, 5)"
    assert pq.containsEvent(i4) == False, "Priority queue did contain (5, 7)"
    print(pq)
    
    # Try to add duplicates
    s10 = Segment((2, 4), (4, 6))
    s11 = Segment((2, 6), (5, 5))
    s12 = Segment((3, 7), (6, 8))
    segments2 = [s10, s11, s12]
    
    for i in range(0, len(segments)):
        seg = segments[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)
        
    for i in range(0, len(segments2)):
        seg = segments2[i]
        endpointsTup = seg.getEndpoints()
        pq.add_each(endpointsTup)
    
    i5 = Intersection(1, 1, s4, s5)
    i6 = Intersection(5, 4, s6, s7)
    intersections2 = [i5, i6]
    pq.add_each(intersections)
    pq.add_each(intersections2)
    
    assert len(pq) == 8, "Length of priority queue was " + str(len(pq))
    print(pq)