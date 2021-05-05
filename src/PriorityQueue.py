# Priority Queue data structure used for the event queue in the B-O algorithm
# Utilizes heapq functions to maintain O(logn) complexity
from heapq import heapify, heappush, heappop
from Intersection import Intersection

class PriorityQueue:
    def __init__(self):
        self.queue = []
        heapify(self.queue)
        
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        return str(list(self.queue))
        
    def add(self, event):
        heappush(self.queue, event)

    # This is a convenience method for adding multiple intersections to the event queue
    # (some operations will add multiple intersections, some will add none).
    # This method should check to make sure there are actually events in 'events' 
    # and make sure they don't already exist in the event queue. 
    # This should utilize the containsEvent method.
    # events = None
    # events = [i1]
    # events = [i1, i2]
    def add_each(self, events):
        # TODO
        return None
        
    def remove_min(self):
        return heappop(self.queue) # heappop removes the "smallest" element in the heap
        
    def containsEvent(self, event):
        for element in self.queue:
            if element == event:
                return True
        return False
        
    # This function should take all segments as a list like 
    # [((x11, y11), (x12, y12)), ((x21, y21), (x22, y22)), ...]
    # Then, it will convert these points into Segment objects and 
    # add the endpoints to the given event queue
    def initialize_event_queue(self, segments):
        # TODO
        return None