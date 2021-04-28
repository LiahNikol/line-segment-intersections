# Class responsible for constructing segment objects
from endpoint import Endpoint

class Segment:
  def __init__(self, left, right):
    # assumes client provides points in corrent left-right order
    self.leftPoint = Endpoint(left[0], left[1], True, self)
    self.rightPoint = Endpoint(right[0], right[1], False, self)
  
  def getLeftEndpoint(self):
    return self.leftPoint
  
  def getRightEndpoint(self):
    return self.rightPoint

  def endpoints(self):
    return [self.getLeftEndpoint().coords(), self.getRightEndpoint().coords()]