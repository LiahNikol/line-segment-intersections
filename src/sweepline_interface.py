import numpy as np
import copy

# Find the y value of the line segment at the given x value
# Assumes that the x value is found on the line
def affine_interp(seg, x):
    x_ratio = (x - seg.leftPoint.x) / (seg.rightPoint.x - seg.leftPoint.x)
    y_point = (1 - x_ratio) * seg.leftPoint.y + (x_ratio) * seg.rightPoint.y
    return y_point

class sweepline:
    def __init__(self):
        self.sl = []
    
    def __len__(self):
        return len(self.sl)

    def inOrder(self):
        return copy.deepcopy(self.sl)

    # Insert a segment into the list based on y position at the x value of the left endpoint of the new segment
    # Input:
    #   seg     - A segment to add to the list
    def add(self, seg):
        # Assume we're only adding points at left endpoint
        x = seg.leftPoint.x
        y = seg.leftPoint.y
        # Compare against each point in the sweepline linearly (temporary, inefficient solution)
        for i in range(len(self.sl)):
            # Get the y value of the given line segment at the given x-value
            compare_y = affine_interp(self.sl[i], x)

            # Sweepline is implemented in order of decreasing y values
            # If the new segment's y value is above one in the list, it should be inserted at that point
            if y > compare_y:
                self.sl.insert(i, seg)
                return i

            # If the new segment has the exact same y value as the one in the list, it should be inserted based
            # on the y position of the right endpoints
            elif y == compare_y:
                # we have to compare y points at a common x value
                new_right_x = seg.rightPoint.x
                old_right_x = self.sl[i].rightPoint.x
                x_compare = min(new_right_x, old_right_x)

                # Find the y values that we're going to compare
                new_right_y = affine_interp(seg.rightPoint.y, x_compare)
                old_right_y = affine_interp(self.sl[i].rightPoint.y, x_compare)

                # If the new line is above the old line, insert the new line above
                if new_right_y > old_right_y:
                    self.sl.insert(i, seg)
                    return i
                # Otherwise, insert the new line below
                else:
                    self.sl.insert(i + 1, seg)
                    return i + 1
            else:
                continue
        # If we make it to the very end without inserting, insert the new segment at the bottom of the sweepline
        self.sl.append(seg)
        return len(self.sl) - 1
        

    def remove(self, seg):
        # Just use the list's methods
        try:
            self.sl.remove(seg)
        except:
            raise Exception("Segment is not in sweepline")

    def findAbove(self, seg):
        try:
            idx = self.sl.index(seg)
        except:
            raise Exception("Segment is not in sweepline")

        # If there is no segment above the given one, return None
        if idx <= 0:
            return None
        # Otherwise, return the segment above the given one
        else:
            return self.sl[idx - 1]
    
    def findBelow(self, seg):
        try:
            idx = self.sl.index(seg)
        except:
            raise Exception("Segment is not in sweepline")

        # If there is no segment below the given one, return None
        if idx >= len(self.sl):
            return None
        # Otherwise, return the segment below the given one
        else:
            return self.sl[idx + 1]

    def swap(self, seg1, seg2):
        try:
            idx1 = self.sl.index(seg1)
            idx2 = self.sl.index(seg2)
        except:
            raise Exception("Segment is not in sweepline")

        # If the given segments aren't next to each other, don't swap them
        if abs(idx1 - idx2) != 1:
            raise Exception("Segments cannot be swapped, they are not next to each other")
        # Otherwise, swap the two segments
        else:
            self.sl[idx1] = seg2
            self.sl[idx2] = seg1
