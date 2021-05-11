# line-segment-intersections
GitHub repo for Spring 2021 Computational Geometry project

This project will implement a python visualization of the sweepline algorithm using the pyglet graphics library. It will take a set of line segments as input. As a part of our visualization, we will include a visual representation of the data structures used to carry out this algorithm. This visualization will output the number of intersections found as well as their location. 

## Visualization
Our project includes a visualization of the sweepline algorithm at work. It can be run with the command 

    py visualization.py
    
In the visualization, you can draw line segments within the grey square. The drawing area can be cleared with the 'CLEAR' button, and examples can be loaded with the 'Ex.1' or 'Ex.2' buttons.

If you press 'RUN', the algorithm will be visualized on the drawn line segments. If you just want to compute the output of the algorithm, you can toggle the visualization mode by pressing the 'a' key.

You can quit the visualization by pressing the 'q' key.

## Algorithm Details
We implemented the Bentley-Ottman algorithm, which uses a sweepline to add and remove line segments from a balanced tree data structure. Segments only check for intersections with other segments immediately above or below the given segment in the balanced tree. Upon reaching an intersection point, segments are switched in the tree. We keep track of the segment beginnings, ends, and intersections using a priority queue, which simulates our sweepline. For our balanced tree we implemented an AVL Tree.
