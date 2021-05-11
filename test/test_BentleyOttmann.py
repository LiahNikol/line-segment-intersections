from linesegmentintersections.BentleyOttmann import bentley_ottman
from linesegmentintersections.Intersection import Intersection
from linesegmentintersections.Segment import Segment, intersects


# Take in a list of segments, and compare the output of the bentley-ottman algorithm with an exhaustive search
# of the intersections between all given line segments
def run_test(segs):
    bo_ints = bentley_ottman(segs)
    bo_ints = [x.coords() for x in bo_ints]
    bo_ints = sorted(bo_ints)

    segments = []
    for pair in segs:
        segments.append(Segment(pair[0], pair[1]))
    full_ints = []
    for i in range(1, len(segments)):
        for j in range(0, i):
            rv = intersects(segments[i], segments[j])
            print(rv)
            if rv != None:
                full_ints.append(rv)
    full_ints = [x.coords() for x in full_ints]
    full_ints = sorted(full_ints)

    assert len(full_ints) == len(bo_ints)
    for i in range(len(full_ints)):
        assert round(full_ints[i][0], 6) == round(bo_ints[i][0], 6)
        assert round(full_ints[i][1], 6) == round(bo_ints[i][1], 6)
    


def test_bentley_ottman():
    points = [[[0, 0], [4, 4]], [[1, 3],[3, 1]]]
    run_test(points)

    points = [[(185, 285), (420, 454)], [(353, 169), (624, 364)], [(185, 388), (458, 161)], [(507, 371), (649, 259)]]
    run_test(points)

    points = [[(188, 465), (189, 245)], [(160, 413), (643, 413)], [(154, 367), (466, 371)], [(506, 470), (653, 240)], [(622, 480), (433, 213)],
                [(572, 234), (137, 308)], [(281, 473), (599, 170)], [(135, 280), (669, 198)]]
    run_test(points)

    points = [((188, 182), (562, 453)), ((260, 463), (596, 177)), ((135, 399), (669, 400))]
    run_test(points)

    points = [((188, 182), (562, 453)), ((260, 463), (596, 177)), ((135, 399), (669, 400)), ((216, 283), (476, 299)), ((364, 213), (365, 472)), ((474, 227), (634, 472)), ((429, 473), (588, 312)), ((185, 371), (397, 240))]
    run_test(points)

    points = [((383, 121), (383, 490)), ((153, 194), (624, 455)), ((281, 447), (662, 150))]
    run_test(points)

    # The following illustrate cases with overlapping intersections. The first works, but the second doesn't.
    # This is functionality we're describing as outside the scope of this project
    # points = [((0, 0), (5, 5)), ((0, 2), (5, 3)),  ((0, 4), (5, 1))]
    # run_test(points)
    # points = [((0, 0), (5, 5)), ((0, 1), (5, 4)), ((0, 2), (5, 3)), ((0, 3), (5, 2)), ((0, 4), (5, 1)), ((0, 5), (5, 0))]
    # run_test(points)