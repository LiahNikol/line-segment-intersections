# Class implements the Bentley Ottmann algorithm where output is an ordered list 
# of intersections found within in a set of segments
from PriorityQueue import PriorityQueue, initialize_event_queue
# from .AVLTree import AVLTree
from sweepline_interface import sweepline
from Segment import Segment
from Endpoint import Endpoint
from Intersection import Intersection

from helper import checkIntersect, isValidPos

def bentley_ottman(segments, debug=False): # [[(x_1, y_1), (x_2, y_2), ...]]
    # Our basic data structures
    eq = PriorityQueue()
    sl = sweepline()

    eq.initialize_event_queue(segments)

    while len(eq) > 0:
        event = eq.get_min()
        rv = event.perform(sl)
        eq.add_each(rv)

    return sl.get_intersections()
