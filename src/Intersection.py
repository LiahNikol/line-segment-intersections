# Class defining an intersection of two line segments 
# Inherits Event type
from Event import Event

class Intersection(Event):
    def __init__(self, x, y, seg1, seg2):
        super().__init__(x, y)
        self.seg1 = seg1
        self.seg2 = seg2