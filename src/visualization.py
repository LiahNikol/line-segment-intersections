import numpy as np
import time
import threading
import copy

import pyglet
from pyglet import shapes
from pyglet.window import mouse, key

from line import line
from button import button

# GLOBAL VARIABLES 
# configurations for the whole program. Best not to mess with them too much. 
is_fullscreen = False
window_size = (800, 600)
background_color = (1, 1, 1)
old_color = (0, 0, 0)
new_color = (100, 200, 150)
border_size = 250
mode = "draw"
draw_flag = True

# List of drawn segments
segs = []
alg_objs = []

# Generate the buttons
clearButton = button("CLEAR", x=70, y=30, width=140, height=60, buttonColor=(232, 229, 140), textColor=(255, 255, 255, 255), statechange=None)
algButton = button("RUN", x=190, y=30, width=100, height=60, buttonColor=(140, 232, 165), textColor=(255, 255, 255, 255), statechange=None)
ex1Button = button("Ex. 1", x=300, y=30, width=120, height=60, buttonColor=(243, 124, 68), textColor=(255, 255, 255, 255), statechange=None)
ex2Button = button("Ex. 2", x=420, y=30, width=120, height=60, buttonColor=(243, 177, 68), textColor=(255, 255, 255, 255), statechange=None)
drawingBox = button("", x=window_size[0] / 2.0, y=window_size[1] / 2.0, width=window_size[0] - border_size, height=window_size[1] - border_size, buttonColor=(230, 230, 230), textColor=(255, 255, 255, 255), statechange=None)

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
    global mode, segs, second_endpoint
    # We should only be responding to button clicks if the program is in draw mode
    if mode == "draw":
        # Only draw lines when clicking in the drawing window
        if drawingBox.isClicked(x, y):
            if not second_endpoint:
                segs.append(line((x, y), (x, y), color=old_color))
                second_endpoint = True
            else:
                second_endpoint = False
        # Remove all drawn lines if the clear button is clicked
        if clearButton.isClicked(x, y):
            if second_endpoint:
                second_endpoint = False
                segs.pop()
            segs = []
            return
        # Run the algorithm once the 'run' button is clicked
        if algButton.isClicked(x, y):
            if second_endpoint:
                second_endpoint = False
                segs.pop()
            mode = "alg"
            threading.Thread(target=run_algorithm, daemon=True).start()
            return
    return

# Handle moving the mouse around
@window.event
def on_mouse_motion(x, y, dx, dy):
    global segs, second_endpoint
    if second_endpoint:
        segs[-1].move_endpoint((x, y))

# Entries in animation_list should be a dictionary with the following:
#   obj => object whose position is being updated (with obj.x = and obj.y =)
#   Pi  => Initial position (x, y)
#   Pf  => Final position (x, y)
#   time => length of time (in seconds) for the animation to play)
#   startTime => start time in milliseconds (from time.time() * 1000.0)
animation_list = []
def update_animations():
    global animation_list
    for anim in animation_list:
        current_time = round(time.time() * 1000.0)
        ratio = (current_time - anim["startTime"]) / (anim["time"] * 1000.0)
        if ratio >= 1.0:
            anim["obj"].x = anim["Pf"][0]
            anim["obj"].y = anim["Pf"][1]
            animation_list.remove(anim)
        else:
            anim["obj"].x = anim["Pi"][0] * (1.0 - ratio) + anim["Pf"][0] * ratio
            anim["obj"].y = anim["Pi"][1] * (1.0 - ratio) + anim["Pf"][1] * ratio

def run_algorithm():
    global mode, alg_objs, drawingBox, animation_list, draw_flag
    alg_objs = []

    for l in segs:
        alg_objs.append(l.endpoint1)
        alg_objs.append(l.endpoint2)
    alg_objs = sorted(alg_objs, key=lambda o: (o.x, o.y))
    target_xs = np.linspace(drawingBox.x - 0.5 * drawingBox.width, drawingBox.x + 0.5 * drawingBox.width, len(alg_objs))
    for o in range(len(alg_objs)):
        animation_list.append({"obj":alg_objs[o], "Pi":(alg_objs[o].x, alg_objs[o].y), "Pf":(target_xs[o], drawingBox.y + 0.5 * drawingBox.height), "time":2.5, "startTime":(time.time() * 1000)})
    time.sleep(5)
    for o in segs:
        o.reset_endpoints()
    alg_objs = []
    mode = "draw"
    return

# Drawing to the screen
@window.event
def on_draw():
    global segs, mode, alg_objs
    window.clear()

    if mode == "draw":
        clearButton.draw()
        algButton.draw()
        ex1Button.draw()
        ex2Button.draw()
        drawingBox.draw()
            
        for s in segs:
            s.draw()
    elif mode == "alg":
        drawingBox.draw()

        update_animations()
        if draw_flag:
            for o in alg_objs:
                o.draw()

# I need this wrapper so that we can schedule the draw function to trigger consistently
def on_draw_wrapper(dt):
    on_draw()
    return

# Run the whole thing
pyglet.clock.schedule_interval(on_draw_wrapper, 0.05)
pyglet.app.run()