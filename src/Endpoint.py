# Class for defining an endpoint belonging to a line segment
# Inherits Event type
from .Event import Event

class Endpoint(Event):
    def __init__(self, x, y, is_left, my_segment):
        super().__init__(x, y)
        self.is_left = is_left # is this the left endpoint or the right endpoint?
        self.my_segment = my_segment # pointer to segment object that this endpoint belongs to

    def isLeft(self):
        return self.is_left
    
    def isRight(self):
        return not self.is_left

    def mySegment(self):
        return self.my_segment
