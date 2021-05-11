# Class implements the Bentley Ottmann algorithm where output is an ordered list 
# of intersections found within in a set of segments
from .PriorityQueue import PriorityQueue
# from .AVLTree import AVLTree
from .sweepline import sweepline
from .Segment import Segment
from .Endpoint import Endpoint
from .Intersection import Intersection

from .helper import checkIntersect, isValidPos

def bentley_ottman(segments, debug=False, log=False): # [[(x_1, y_1), (x_2, y_2), ...]]
    if debug:
        print("-----bentley-ottman-start-----")
    # Our basic data structures
    eq = PriorityQueue()
    sl = sweepline(debug=debug, log=log)

    eq.initialize_event_queue(segments)

    while len(eq) > 0:
        event = eq.remove_min()
        rv = event.perform(sl)
        eq.add_each(rv)
        if debug:
            print("\tIntersections added: {}".format(rv))

    if debug:
        print("Final Intersections: {}".format(sl.intersection_list))
        print("-----bentley-ottman-end-----")

    if log:
        return sl.intersection_list, sl.actionlog
    else:
        return sl.intersection_list
