import numpy as np
import pyglet
from pyglet import shapes
from pyglet.window import mouse, key
from segment import segment

# GLOBAL VARIABLES 
# configurations for the whole program. Best not to mess with them too much. 
is_fullscreen = False
window_size = (800, 600)
background_color = (1, 1, 1)
old_color = (0, 0, 0)
new_color = (100, 200, 150)

segs = [segment((50, 50), (300, 300), color=old_color)]


# Generate the Pyglet Window with important configurations
if is_fullscreen:
    window = pyglet.window.Window(fullscreen=is_fullscreen)
else:
    window = pyglet.window.Window(width=window_size[0], height=window_size[1])
pyglet.gl.glClearColor(background_color[0], background_color[1], background_color[2], 1)

# Handle mouse pressings
second_endpoint = False
@window.event
def on_mouse_press(x, y, button, modifiers):
    global segs, second_endpoint
    if not second_endpoint:
        segs.append(segment((x, y), (x, y), color=old_color))
        second_endpoint = True
    else:
        second_endpoint = False

# Handle moving the mouse around
@window.event
def on_mouse_motion(x, y, dx, dy):
    global segs, second_endpoint
    if second_endpoint:
        segs[-1].move_endpoint((x, y))

# Handle pressing a key on the keyboard
@window.event
def on_key_press(symbol, modifiers):
    global segs
    if symbol == key.C:
        segs = []
    
# Drawing to the screen
@window.event
def on_draw():
    global segs
    window.clear()
        
    for s in segs:
        s.draw()

# Run the whole thing
pyglet.app.run()