# Class defining an intersection of two line segments 
# Inherits Event type
from .Event import Event

class Intersection(Event):
    def __init__(self, x, y, seg1, seg2):
        super().__init__(x, y)
        self.seg1 = seg1
        self.seg2 = seg2

    # Function to perform once this event is removed from the event queue. 
    # It should add the intersection to the sweepline's intersection_list
    # and then perform the swap of the intersection's two segments. 
    # It should return any new intersections returned by the sweepline's swap.
    def perform(self, sl):
        return sl.handle_intersection(self)