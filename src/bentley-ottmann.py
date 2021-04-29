# Class implements the Bentley Ottmann intersections for a set of segments algoriths
from endpoint import Endpoint
from segment import Segment
from intersection import Intersection
#from avltree import AVLTree
from helper import checkIntersect, isValidPos
from ExampleAVL import AVLTree
            
def main(segments, debug): # [[(x_1, y_1), (x_2, y_2), ...]]
    # initializing data structures
    eq = AVLTree() # event queue implemented as a binaryTree containing all endpoints sorted by increasing x and y
    eqRoot = None
    sl = AVLTree()
    slRoot = None
    output = []
    for segment in segments:
        newSeg = Segment(segment[0], segment[1])
        eqRoot = eq.insert_node(eqRoot, newSeg.getLeftEndpoint(), debug)
        eqRoot = eq.insert_node(eqRoot, newSeg.getRightEndpoint(), debug)
    
    if debug == True:
        print("current q: ", end="") 
        eq.inOrder(eqRoot)
        print()
        eq.printHelper(eqRoot, "", True)
        print()
        print("size: " + str(eq.getSize()))
    
    # main algorithm
    while eq.size() > 0:
        event = eq.getMinValueNode(eqRoot)
        if isinstance(event, Endpoint) and event.isLeft(): # event is a left endpoint
            seg = event.getSegment()
            segPos = sl.add(seg) # add this segment to the active list
            aPos = segPos + 1
            bPos = segPos - 1
            if isValidPos(aPos, sl):
                aCoords = checkIntersect(aPos, seg, sl)
                if len(aCoords) > 0:
                    eq.insert(aCoords)
            if isValidPos(bPos, sl): 
                bIntersection = checkIntersect(bPos, seg, sl)
                if len(bCoords) > 0:
                    eq.insert(bCoords)
            
        elif isinstance(event, Endpoint) and event.isRight(): # event is a right endpoint
            seg = event.getSegment()
            segPos = sl.remove(seg)
            aPos = segPosition
            bPos = segPosition - 1
            if isValidPos(aPos, sl) and isValidPos(bPos, sl):
                bSeg = sl.get(bPos)
                coords = checkIntersect(aPos, bSeg, sl)
                if len(coords) > 0 and not eq.contains(coords):
                    eq.insert(coords)
                
        elif isinstance(event, Intersection): # event is an intersection
            output.append(event)
            segAbove = event.getSegAbove()
            segBelow = event.getSegBelow()
            newPos1, newPos2 = sl.swap(segAbove, segBelow) # segAbove is now below segBelow and segBelow is now above segAbove...
            aPos = segBelow + 1
            bPos = segAbove - 1
            if isValidPos(aPos, sl):
                aCoords = checkIntersect(aPos, segBelow, sl)
                if len(aCoords) > 0 and not eq.contains(aCoords):
                    eq.insert(aCoords)
            if isValidPos(bPos, sl): 
                bCoords = checkIntersect(bPos, segAbove, sl)
                if len(bCoords) > 0 and not eq.contains(bCoords):
                    eq.insert(bCoords)
        eq.delete_node(eqRoot, event.coords())
    return output
