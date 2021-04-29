# Class for defining an endpoint belonging to a line segment
class Endpoint:
  def __init__(self, x, y, left, segment):
    self.x = x # x coordinate of this point
    self.y = y # y coordinate of this point
    self.left = left # is this tne left endpoint or the right endpoint?
    self.segment = segment # segment that this endpoint belongs to
    
  def isLeft(self):
    return self.left
    
  def isRight(self):
    return not self.left
    
  def coords(self):
    return (self.x, self.y)

  def getSegment(self):
    return self.segment
