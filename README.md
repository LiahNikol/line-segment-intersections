# line-segment-intersections

An implementation of the Bentley-Ottman algorithm.

## Requirements

    numpy >= 1.19.0

## Usage

To use the algorithm, you can import it using 

    from linesegmentintersections import bentley_ottman
    
    segments = [[[0, 0], [4, 4]], [[1, 3], [3, 1]]]
    intersections = bentley_ottman(segments)
    
This algorithm takes a list of pairs of (x, y) coordinates. It will output a list of Intersection objects, from which you can get the coordinates using 

    x_coordinate = intersections[0].x
    y_coordinate = intersections[0].y

### Important Assumptions

***No endpoints lie on another segment.*** This implementation will work on most cases with colinear endpoints, but there are a few edge cases which will not work, such as 2 or more endpoints lying on a vertical segment. It will simply be missing intersections in the final output.

***No 3 line segments intersect at the same location.*** This may cause the algorithm to report a fewer quantity of intersections than are truly there, but will still report the correct locations of intersections.

***No segments share endpoints.*** This will cause the algorithm to throw an error.

## Algorithm Details

We implemented the Bentley-Ottman algorithm, which uses a sweepline to add and remove line segments from a balanced tree data structure. Segments only check for intersections with other segments immediately above or below the given segment in the balanced tree. Upon reaching an intersection point, segments are switched in the tree. We keep track of the segment beginnings, ends, and intersections using a priority queue, which simulates our sweepline. For our balanced tree we implemented an AVL Tree.
