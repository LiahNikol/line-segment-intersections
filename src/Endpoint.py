# Class for defining an endpoint belonging to a line segment
# Inherits Event type
from .Event import Event

class Endpoint(Event):
    def __init__(self, x, y, is_left, my_segment):
        super().__init__(x, y)
        self.is_left = is_left # is this the left endpoint or the right endpoint?
        self.my_segment = my_segment # pointer to segment object that this endpoint belongs to

    def __eq__(self, o):
        return isinstance(o, type(self)) and self.x == o.x and self.y == o.y and self.is_left == o.is_left

    def __repr__(self):
        return "({}, {}):{}".format(self.x, self.y, "left" if self.is_left else "right")

    # This function should perform all the stuff that needs to happen once an endpoint is removed
    # from the event queue. 
    # It should just call the associated methods in the sweepline,
    # and then return the intersections returned by the sweepline call.
    def perform(self, sl):
        if self.is_left:
            return sl.add(self.my_segment)
        else:
            return sl.remove(self.my_segment)
