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

    def getLeftEndpoint(self):
        return self.leftPoint
  
    def getRightEndpoint(self):
        return self.rightPoint
        
    def getEndpoints(self):
        return (self.leftPoint, self.rightPoint)

    def getCurrentY(self, x):
        return
        
    def getSlope(self):
        x1, y1 = self.leftPoint.coords()
        x2, y2 = self.rightPoint.coords()
        num = y2 - y1
        denom = x2 - x1
        return num / denom

    def getYIntercept(self):
        x, y = self.leftPoint.coords()
        m = self.getSlope()
        b = y - (m * x)
        return b