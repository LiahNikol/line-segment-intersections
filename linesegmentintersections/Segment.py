# Class responsible for constructing segment objects
import numpy as np
from .Endpoint import Endpoint
from .Intersection import Intersection
from .helper import orientation

class Segment:
    def __init__(self, left, right):
        self.node = None
        if left < right:
            self.leftPoint = Endpoint(left[0], left[1], True, self)
            self.rightPoint = Endpoint(right[0], right[1], False, self)
        else:
            self.leftPoint = Endpoint(right[0], right[1], True, self)
            self.rightPoint = Endpoint(left[0], left[1], False, self)
  
    def __str__(self):
        return "{{{}, {}}}".format(self.leftPoint, self.rightPoint) 

    def __eq__(self, o):
        return self.leftPoint == o.leftPoint and self.rightPoint == o.rightPoint

    def __ne__(self, o):
        return o == None or (not self == o)

    def __repr__(self):
        return "{{{}, {}}}".format(self.leftPoint, self.rightPoint) 
        
    def getEndpoints(self):
        return (self.leftPoint, self.rightPoint)

    # Just tells us if the given point is one of the endpoints 
    def is_endpoint(self, pt):
        left = self.leftPoint.x == pt[0] and self.leftPoint.y == pt[1]
        right = self.rightPoint.x == pt[0] and self.rightPoint.y == pt[1]

        return left or right


# I think the intersection code should be here. 
# Check for an intersection between segments A and B.
# If there is no intersection, then return None
def intersects(segA, segB):
    # Put endpoints in a useable format
    a_left  = np.array([segA.leftPoint.x,  segA.leftPoint.y,  1])
    a_right = np.array([segA.rightPoint.x, segA.rightPoint.y, 1])
    b_left  = np.array([segB.leftPoint.x,  segB.leftPoint.y,  1])
    b_right = np.array([segB.rightPoint.x, segB.rightPoint.y, 1])

    # Perform orientation tests
    o1 = orientation(a_left, a_right, b_left)
    o2 = orientation(a_left, a_right, b_right)
    o3 = orientation(b_left, b_right, a_left)
    o4 = orientation(b_left, b_right, a_right)

    if o1 != o2 and o3 != o4:
        # Handling the cases when you have a completely vertical line
        if a_right[0] - a_left[0] == 0:
            slopeB = (b_right[1] - b_left[1]) / (b_right[0] - b_left[0])
            yi_B = b_left[1] - slopeB * b_left[0]
            x_coord = a_left[0]
            y_coord = slopeB * x_coord + yi_B
        elif b_right[0] - b_left[0] == 0:
            slopeA = (a_right[1] - a_left[1]) / (a_right[0] - a_left[0])
            yi_A = a_left[1] - slopeA * a_left[0]
            x_coord = b_left[0]
            y_coord = slopeA * x_coord + yi_A
        else:
            # Find intersection point
            # Code is from Liah's earlier code in helper.py
            # First calculate slopes of each line segment
            slopeA = (a_right[1] - a_left[1]) / (a_right[0] - a_left[0])
            slopeB = (b_right[1] - b_left[1]) / (b_right[0] - b_left[0])
            # Calculate y-intercept of each line segment
            yi_A = a_left[1] - slopeA * a_left[0]
            yi_B = b_left[1] - slopeB * b_left[0]

            # Calculate intersection point
            x_coord = (yi_B - yi_A) / (slopeA - slopeB)
            y_coord = slopeA * x_coord + yi_A

        intersection_orientation = orientation(a_left, b_left, [x_coord, y_coord, 1])
        # If a left endpoint is the intersection point, then this orientation test is 0.
        # So, we perform the other orientation test to see which is the top segment
        if intersection_orientation == 0:
            intersection_orientation = - orientation(a_right, b_right, [x_coord, y_coord, 1])

        if intersection_orientation > 0:
            return Intersection(x_coord, y_coord, segA, segB)
        else:
            return Intersection(x_coord, y_coord, segB, segA)

    return None
    