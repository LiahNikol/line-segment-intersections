import numpy as np

# Class implements the Bentley Ottmann intersections for a set of segments algoriths
from bst import BST

class BentleyOttmannAlgo:
  def main(segments): # {([x_1, y_1], [x_2, y_2]), ...}
    # initializing data structures
    eq = BST() # event queue implemented as a binaryTree containing all endpoints sorted by increasing x and y
    sl = # activeList sorted by increasing y of leftendpoints
    output = []
    for segment in segments:
      newSeg = Segment(segment[0], segment[1])
      eq.add(newSeg.getLeftEndpoint)
      eq.add(newSeg.getRightEndpoint)

    # main algorithm
    while eq.size() > 0:
      event = eq.removeNext()
      if isinstance(event, Endpoint) && event.isLeft():
        seg = event.getSegment()
        segPosition = sweepLine.add(seg) # add this segment to the active list
        belowIdx = segPosition - 1; # check for intersections against active segment
        if belowIdx >= 0:
          belowSeg = sweepLine.get(belowIdx)
          intersection = intersects(seg, belowSeg)
          if intersection != -1: eventQueue.add(intersection)
          
        aboveIdx = segPosition + 1
        if aboveIdx < sweepLine.size():
          aboveSeg = sweepLine.get(aboveIdx)
          intersection = intersects(seg, aboveSeg)
          if intersection != -1: eventQueue.add(intersection)
      elif isinstance(currentEvent, Endpoint) && currentEvent.isRight():
        seg = currentEvent.getSegment()
        segPosition = sweepLine.remove(seg)
        belowIdx = segPosition - 1
        aboveIdx = segPosition
        if belowIdx >= 0 && aboveIdx < sweepLine.size():
          belowSeg = sweepLine.get(belowIdx)
          aboveSeg = sweepLine.get(aboveIdx)
          intersection = intersects(belowSeg, aboveSeg)
          if intersection != -1: eventQueue.add(intersection) # make sure intersection isn't already in there though
      elif isinstance(currentEvent, Intersection): # currentEvent is an intersection
        output.add(currentEvent)
        segAbove = currentEvent.getSegAbove()
        segBelow = currentEvent.getSegBelow()
        sweepline.swap(segAbove, segBelow)
        segAboveAbove = sweepLine.above(segBelow)
        segBelowBelow = sweepLine.below()
        # add intersections to eq if they don't already exist
  return output
