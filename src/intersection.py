class Intersection:
  def __init__(self, x, y, segAbove, segBelow):
    self.x = x # x coordinate of the intersection
    self.y = y # y coordinate of the intersection
    self.segAbove = segAbove # segment that was above segBelow when approaching intersection from the left
    self.segBelow = segBelow # segment that was below segAbove when approaching intersection from the left
  
  def getSegAbove(self):
    return self.segAbove
    
  def getSegBelow(self):
    return self.segBelow