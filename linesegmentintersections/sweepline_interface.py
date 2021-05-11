import numpy as np
import copy
from .Segment import intersects

# Find the y value of the line segment at the given x value
# Assumes that the x value is found on the line
def affine_interp(seg, x):
    # TODO: What do we do in the case of vertical lines?
    # Answer: We return the lowest point in the vertical line
    # This function should only be run in the case of adding a segment to a line,
    # In which case we want a vertical segment to be added to the bottom
    # HOWEVER, this will not work in the case of a segment's left endpoint laying
    # on a completely vertical segment. 
    # At this point, I think we should just assume that input has 
    # "No 3 points colinear".
    if seg.rightPoint.x - seg.leftPoint.x == 0:
        return seg.leftPoint.y
    x_ratio = (x - seg.leftPoint.x) / (seg.rightPoint.x - seg.leftPoint.x)
    y_point = (1 - x_ratio) * seg.leftPoint.y + (x_ratio) * seg.rightPoint.y
    return y_point

class sweepline:
    def __init__(self, debug=False, log=True):
        self.sl = []
        self.debug = debug
        self.log = log
        self.actionlog = []
        self.intersection_list = []
    
    def __len__(self):
        return len(self.sl)

    def __getitem__(self, idx):
        return self.sl[idx]

    def inOrder(self):
        return copy.deepcopy(self.sl)

    # Insert a segment into the list based on y position at the x value of the left endpoint of the new segment.
    # Return any intersections formed by this segment and its neighboring segments.
    # Input:
    #   seg     - A segment to add to the list
    def add(self, seg):
        if self.debug:
            print("Adding {}".format(seg))
        if self.log:
            self.actionlog.append({"event":"add", "seg":seg, "point":(seg.leftPoint.x, seg.leftPoint.y)})

        # Add segment to sweepline and sort it based on y value of each segment at the given left endpoint
        # If the y-values are equal, sort based on the y value at the segment's right endpoint
        self.sl.append(seg)
        self.sl = sorted(self.sl, key=lambda x: [affine_interp(x, seg.leftPoint.x), affine_interp(x, seg.rightPoint.x)])

        # Check for intersections
        return self.check_for_intersections(seg, above=True, below=True)

    # Remove a segment from the sweepline.
    # Returns any intersections formed by the segment immediately above and immediately below the 
    # removed segment.
    def remove(self, seg):
        if self.debug:
            print("Removing {}".format(seg))
        if self.log:
            self.actionlog.append({"event":"remove", "seg":seg, "point":(seg.rightPoint.x, seg.rightPoint.y)})

        idx = self.sl.index(seg)
        self.sl.remove(seg)

        return_list = []
        if idx > 0 and idx < len(self.sl):
            return_list.extend(self.check_for_intersections(self.sl[idx], above=False, below=True))
        return return_list

    # Add the intersection to the sweepline's intersection list,
    # Then swap the two given segments,
    # Then check for more intersections
    def handle_intersection(self, i):
        if self.debug:
            print("Swapping {}, {}".format(i.seg1, i.seg2))
        if self.log:
            self.actionlog.append({"event":"intersection", "int":i, "point":(i.x, i.y)})

        # Add to the intersection list
        self.intersection_list.append(i)

        # Swap the segments
        idx1 = self.sl.index(i.seg1)
        idx2 = self.sl.index(i.seg2)
        self.sl[idx1] = i.seg2
        self.sl[idx2] = i.seg1

        # Check for new intersections
        return_list = []
        if idx2 > 0:
            return_list.extend(self.check_for_intersections(i.seg1, above=False, below=True))
        if idx1 < len(self.sl) - 1:
            return_list.extend(self.check_for_intersections(i.seg2, above=True, below=False))

        return return_list


    # Given a segment, check for intersections. Return any intersections that need to be added to the event queue.
    def check_for_intersections(self, seg, above=True, below=True):
        idx = self.sl.index(seg)
        intersections = []

        # Only check for intersections if we're supposed to, and we're able to
        if below and idx > 0:
            intersections.append(intersects(seg, self.sl[idx - 1]))
            if self.log:
                self.actionlog.append({"event":"check", "seg1":seg, "seg2":self.sl[idx - 1], "result":intersections[-1]})
        if above and idx < len(self.sl) - 1:
            intersections.append(intersects(seg, self.sl[idx + 1]))
            if self.log:
                self.actionlog.append({"event":"check", "seg1":seg, "seg2":self.sl[idx + 1], "result":intersections[-1]})

        # Filter out and handle any intersections that deal with endpoints, or any segments that didn't result in intersections.
        rl = []
        for i in intersections:
            # This is the case that there was no intersection
            if i is None:
                continue
            else: 
                # We don't want to place repeat intersections in the priority queue
                if i in self.intersection_list:
                    continue
                # If the intersection point is at an endpoint, we will add it to our intersections list but not to our sweepline.
                elif i.seg1.is_endpoint((i.x, i.y)) or i.seg2.is_endpoint((i.x, i.y)):
                    self.intersection_list.append(i)
                    continue
                else:
                    rl.append(i)
        return rl
