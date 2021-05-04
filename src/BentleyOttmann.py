# Class implements the Bentley Ottmann algorithm where output is an ordered list 
# of intersections found within in a set of segments
from .PriorityQueue import PriorityQueue
from .AVLTree import AVLTree
from .Segment import Segment
from .Endpoint import Endpoint
from .Intersection import Intersection

from .helper import checkIntersect, isValidPos
            
def main(segments, debug): # [[(x_1, y_1), (x_2, y_2), ...]]
    # initializing data structures
    eq = PriorityQueue()
    sl = AVLTree()
    output = []
    for segment in segments:
        newSeg = Segment(segment[0], segment[1])
        eq.add(newSeg.getLeftEndpoint())
        eq.add(newSeg.getRightEndpoint())
    
    # main algorithm
    while len(eq) > 0:
        event = eq.remove_min()
        if debug:
            print(event)
            
        if isinstance(event, Endpoint) and event.isLeft(): # event is a left endpoint
            seg = event.mySegment()
            segPos = sl.insert_node(seg) # add this segment to the active list
            aPos = segPos + 1
            bPos = segPos - 1
            if isValidPos(aPos, sl):
                aCoords = checkIntersect(aPos, seg, sl)
                if len(aCoords) > 0:
                    eq.add(aCoords)
            if isValidPos(bPos, sl): 
                bIntersection = checkIntersect(bPos, seg, sl)
                if len(bCoords) > 0:
                    eq.add(bCoords)
            
        elif isinstance(event, Endpoint) and event.isRight(): # event is a right endpoint
            seg = event.mySegment()
            segPos = sl.remove(seg)
            aPos = segPosition
            bPos = segPosition - 1
            if isValidPos(aPos, sl) and isValidPos(bPos, sl):
                bSeg = sl.get(bPos)
                coords = checkIntersect(aPos, bSeg, sl)
                if len(coords) > 0 and not eq.containsIntersection(coords):
                    eq.add(coords)
                
        elif isinstance(event, Intersection): # event is an intersection
            output.append(event)
            segAbove = event.getSegAbove()
            segBelow = event.getSegBelow()
            newPos1, newPos2 = sl.swap(segAbove, segBelow) # segAbove is now below segBelow and segBelow is now above segAbove...
            aPos = segBelow + 1
            bPos = segAbove - 1
            if isValidPos(aPos, sl):
                aCoords = checkIntersect(aPos, segBelow, sl)
                if len(aCoords) > 0 and not eq.containsIntersection(aCoords):
                    eq.add(aCoords)
            if isValidPos(bPos, sl): 
                bCoords = checkIntersect(bPos, segAbove, sl)
                if len(bCoords) > 0 and not eq.containsIntersection(bCoords):
                    eq.add(bCoords)
    return output
