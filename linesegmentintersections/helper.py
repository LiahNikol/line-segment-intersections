# Class contains auxiliary methods
from numpy import array
from numpy.linalg import det
from .Intersection import Intersection


def isValidPos(oPos, sl):
  if oPos < 0 or oPos >= len(sl):
    return False
  return True

# credit to Dr. Sheehy for provinding orientation class code
def orientation(*points):
  d = array(det(points))
  if d > 0:
    return 1 # ccw
  elif d < 0:
    return -1 # cw
  else:
    return 0 # colinear
  
def checkIntersect(oPos, seg, sl):
  # check for intersection
  oSeg = sl.get(oPos)
  coords = intersects(seg, oSeg)
  if len(coords) > 0:
    return coords # return a tuple of the intersection coordinates
  return ()

def intersects(seg1, seg2):
  l1, r1 = seg1.endpoints() # extract endpoints from each segment
  l2, r2 = seg2.endpoints()
  
  ret1 = orientation(l1, r1, l2)
  ret2 = orientation(l1, r1, r2)
  
  ret3 = orientation(l2, r2, l1)
  ret4 = orientation(l2, r2, r1)
  
  if ret1 * ret2 < 0 and ret3 * ret4 < 0: # determinants have same sign so these 2 segments cannot intersect
      # calculate coords 
      xNum = seg2.getYIntercept() - seg1.getYIntercept()
      xDenom = seg1.getSlope() - seg2.getSlope()
      x = xNum / xDenom
      y = seg1.getSlope() * x + seg1.getYIntercept()
      
      # determine which segment is "above" and which "below"
      l3 = seg1.getLeftEndpoint().coords()
      l4 = seg2.getLeftEndpoint().coords()
      intersection = (x, y)
      if orientation(l3, intersection, l4) > 0: # ccw
        return Intersection(x, y, seg2, seg1)
      elif orientation(l3, intersection, l4) < 0: # cw
        return Intersection(x, y, seg1, seg2)
  return ()
    
    