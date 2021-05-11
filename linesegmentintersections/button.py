import numpy as np
import pyglet
from pyglet import shapes

class button():
    def __init__(self, text, x, y, width, height, buttonColor, textColor, statechange=None, font_size=24):
        self.selected = False
        self.batch = pyglet.graphics.Batch()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = buttonColor
        self.selectedColor = list((max(i - 40, 0) for i in buttonColor))
        self.statechange = statechange
        self.text = pyglet.text.Label(text=text, x=x, y=y, align='center', anchor_x='center', anchor_y='center', font_name="Helvetica", font_size=font_size, bold=True, color=textColor, batch=self.batch, group=pyglet.graphics.OrderedGroup(1))
        self.btn = shapes.Rectangle(x - 0.5 * width, y - 0.5 * height, width, height, color=buttonColor, batch=self.batch, group=pyglet.graphics.OrderedGroup(0))
    
    def draw(self):
        self.batch.draw()

    def isClicked(self, x, y):
        if abs(x - self.x) <= 0.5 * self.width and abs(y - self.y) <= 0.5 * self.height:
            return True
        else:
            return False

    def click(self):
        if self.selected:
            self.btn.color = self.color
        else: 
            self.btn.color = self.selectedColor
        self.selected = not self.selected

    def move(self, x, y):
        self.x = x
        self.y = y
        self.text.x = x
        self.text.y = y
        self.btn.x = x - 0.5 * self.width
        self.btn.y = y - 0.5 * self.height