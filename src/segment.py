import numpy as np
import pyglet
from pyglet import shapes

endpoint_radius = 10
line_width = 6

class segment():
    def __init__(self, p1, p2, color):
        self.batch = pyglet.graphics.Batch()
        self.p1 = shapes.Circle(p1[0], p1[1], endpoint_radius, color=color, batch=self.batch)
        self.p2 = shapes.Circle(p2[0], p2[1], endpoint_radius, color=color, batch=self.batch)
        self.segment = shapes.Line(p1[0], p1[1], p2[0], p2[1], width=line_width, color=color, batch=self.batch)
        self.shapes = [self.p1, self.p2, self.segment]

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
        else:
            self.p2.x = p[0]
            self.p2.y = p[1]
            self.segment.x2 = p[0]
            self.segment.y2 = p[1]