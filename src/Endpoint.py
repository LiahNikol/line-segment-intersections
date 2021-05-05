# Class for defining an endpoint belonging to a line segment
# Inherits Event type
from Event import Event

class Endpoint(Event):
    def __init__(self, x, y, is_left, my_segment):
        super().__init__(x, y)
        self.is_left = is_left # is this the left endpoint or the right endpoint?
        self.my_segment = my_segment # pointer to segment object that this endpoint belongs to

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.is_left == o.is_left

    # This function should perform all the stuff that needs to happen once an endpoint is removed
    # from the event queue. 
    # It should just call the associated methods in the sweepline,
    # and then return the intersections returned by the sweepline call.
    def perform(self, sl):
        # TODO
        return None
