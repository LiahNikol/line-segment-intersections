# Priority Queue data structure used for the event queue in the B-O algorithm
# Utilizes heapq functions to maintain O(logn) complexity
from heapq import heapify, heappush, heappop
from .Intersection import Intersection

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
        
    def remove_min(self):
        return heappop(self.queue) # heappop removes the "smallest" element in the heap
        
    # log(n) ?
    def containsIntersection(self, event):
        x, y = event.coords()
        for element in self.queue:
            if isinstance(element, Intersection) and isinstance(event, Intersection):
                if element.coords()[0] == x and element.coords()[1] == y:
                    return True
        return False
