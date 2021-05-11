from linesegmentintersections.sweepline_interface import sweepline
from linesegmentintersections.Segment import Segment

# Build test segments
segs = []
segs.append(Segment(( 0, 10), (10, 10))) # 0
segs.append(Segment(( 0,  9), (10,  8))) # 1
segs.append(Segment(( 0,  8), (10,  9))) # 2
segs.append(Segment(( 5,  7), (10,  7))) # 3
segs.append(Segment(( 0,  6), (10,  6))) # 4
segs.append(Segment(( 0,  5), (10,  5))) # 5


