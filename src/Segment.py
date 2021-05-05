# Class responsible for constructing segment objects
from Endpoint import Endpoint

class Segment:
    def __init__(self, left, right):
        # assumes client provides points in corrent left-right order
        self.leftPoint = Endpoint(left[0], left[1], True, self)
        self.rightPoint = Endpoint(right[0], right[1], False, self)
  
    def __str__(self):
        return "{" + self.leftPoint + ", " + self.rightPoint + "}" 

    def __eq__(self, o):
        return self.leftPoint == o.leftPoint and self.rightPoint == o.rightPoint

    def __repr__(self):
        return "{" + self.leftPoint + ", " + self.rightPoint + "}" 
        
    def getEndpoints(self):
        return (self.leftPoint, self.rightPoint)


# I think the intersection code should be here. 
# Check for an intersection between segments A and B.
# If there is no intersection, then return None
def intersects(segA, segB):
    # TODO
    return None