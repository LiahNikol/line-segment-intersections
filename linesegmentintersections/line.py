import numpy as np
import pyglet
from pyglet import shapes
from .button import button

endpoint_radius = 10
line_width = 6

class line():
    def __init__(self, p1, p2, color):
        self.batch = pyglet.graphics.Batch()
        self.r = endpoint_radius
        self.p1 = shapes.Circle(p1[0], p1[1], endpoint_radius, color=color, batch=self.batch)
        self.p2 = shapes.Circle(p2[0], p2[1], endpoint_radius, color=color, batch=self.batch)
        self.segment = shapes.Line(p1[0], p1[1], p2[0], p2[1], width=line_width, color=color, batch=self.batch)
        self.shapes = [self.p1, self.p2, self.segment]

        self.endpoint1 = Location(p1[0], p1[1], self)
        self.endpoint2 = Location(p2[0], p2[1], self)


    def draw(self):
        self.batch.draw()

    def set_color(self, c):
        for o in self.shapes:
            o.color = c

    def move_endpoint(self, p, p1=False):
        if p1:
            self.p1.x = p[0]
            self.p1.y = p[1]
            self.segment.x = p[0]
            self.segment.y = p[1]
            self.endpoint1.x = p[0]
            self.endpoint1.y = p[1]
        else:
            self.p2.x = p[0]
            self.p2.y = p[1]
            self.segment.x2 = p[0]
            self.segment.y2 = p[1]
            self.endpoint2.x = p[0]
            self.endpoint2.y = p[1]

    def reset_endpoints(self):
        self.endpoint1.x = self.p1.x
        self.endpoint1.y = self.p1.y

        self.endpoint2.x = self.p2.x
        self.endpoint2.y = self.p2.y

    def ordered(self):
        if self.endpoint1 < self.endpoint2:
            return ((self.endpoint1.x, self.endpoint1.y), (self.endpoint2.x, self.endpoint2.y))
        else:
            return ((self.endpoint2.x, self.endpoint2.y), (self.endpoint1.x, self.endpoint1.y))

# This is needed because of the wonky way I'm drawing the Intersections' PriorityQueue Cards
class Location():
    def __init__(self, x, y, data=None):
        self.x = x
        self.y = y
        self.data = data
    
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        else:
            return self.x > other.x

    def __le__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        else:
            return self.x <= other.x

    def __ge__(self, other):
        if self.x == other.x:
            return self.y >= other.y
        else:
            return self.x >= other.x
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y