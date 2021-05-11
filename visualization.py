import numpy as np
import time
import threading
import copy

import pyglet
from pyglet import shapes
from pyglet.window import mouse, key

from linesegmentintersections.line import line, Location
from linesegmentintersections.button import button

from linesegmentintersections import bentley_ottman

# GLOBAL VARIABLES 
# configurations for the whole program. Best not to mess with them too much. 
is_fullscreen = False
window_size = (800, 600)
background_color = (1, 1, 1)
old_color = (0, 0, 0)
new_color = (100, 200, 150)
border_size = 100
mode = "draw"
show_algorithm = True
alg_button_color_show = (140, 232, 165)
alg_button_color_fast =  (128, 193, 229)

whiteText = (255, 255, 255, 255)
blackText = (0, 0, 0, 255)

# List of drawn segments
segs = []
# List of drawn segments during algorithm runtime
alg_title = pyglet.text.Label(text="Testing", x=window_size[0] / 2, y=window_size[1] - 0.5 * border_size, align='center', anchor_x='center', anchor_y='center', font_name="Helvetica", font_size=32, bold=True, color=blackText)
title_text = ""
alg_segs = []
alg_segs_highlight = []
alg_intersection_highlight = None
color_black = (0, 0, 0)
color_blue  = ( 86, 177, 229 )
color_green = ( 135, 215, 147 )
color_red   = ( 221, 113, 79 )
color_purple= ( 227, 181, 236 )
alg_segment = line((0, 0), (1, 1), color=old_color)
sweepline_line = shapes.Line(0, 0, 1, 1, width = 2, color=old_color)
intersectionLocations = []
intersectionPoint = shapes.Circle(0, 0, 8, color=(200, 50, 50))

# Generate the buttons
clearButton = button("CLEAR", x=70, y=30, width=140, height=60, buttonColor=(232, 229, 140), textColor=(255, 255, 255, 255), statechange=None)
algButton = button("RUN", x=190, y=30, width=100, height=60, buttonColor=alg_button_color_show, textColor=(255, 255, 255, 255), statechange=None)
ex1Button = button("Ex. 1", x=300, y=30, width=120, height=60, buttonColor=(243, 124, 68), textColor=(255, 255, 255, 255), statechange=None)
ex2Button = button("Ex. 2", x=420, y=30, width=120, height=60, buttonColor=(243, 177, 68), textColor=(255, 255, 255, 255), statechange=None)
drawingBox = button("", x=window_size[0] / 2.0, y=window_size[1] / 2.0, width=window_size[0] - border_size * 2, height=window_size[1] - border_size * 2, buttonColor=(230, 230, 230), textColor=(255, 255, 255, 255), statechange=None)

# Example segments
ex1_points = [(185, 285), (420, 454), (353, 169), (624, 364), (185, 388), (458, 161), (507, 371), (649, 259)]
ex1_segs = []
for i in range(int(len(ex1_points) / 2)):
    ex1_segs.append(line(ex1_points[2 * i], ex1_points[2 * i + 1], color=old_color))
ex2_points = [(188, 465), (189, 245), (160, 413), (643, 413), (154, 367), (466, 371), (506, 470), (653, 240), (622, 480), (433, 213),
                (572, 234), (137, 308), (281, 473), (599, 170), (135, 280), (669, 198)]
ex2_segs = []
for i in range(int(len(ex2_points) / 2)):
    ex2_segs.append(line(ex2_points[2 * i], ex2_points[2 * i + 1], color=old_color))

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
    global mode, segs, second_endpoint, ex1_segs, ex2_segs, intersectionLocations
    # Upon clicking anywhere, we want the previous intersections to disappear
    intersectionLocations = []
    # We should only be responding to button clicks if the program is in draw mode
    if mode == "draw":
        # Only draw lines when clicking in the drawing window
        if drawingBox.isClicked(x, y):
            # print("({}, {})".format(x, y))
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
        if ex1Button.isClicked(x, y):
            if second_endpoint:
                second_endpoint = False
                segs.pop()
            segs = []
            segs = list(ex1_segs)
            return
        if ex2Button.isClicked(x, y):
            if second_endpoint:
                second_endpoint = False
                segs.pop()
            segs = []
            segs = list(ex2_segs)
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

@window.event
def on_key_press(symbol, modifiers):
    global show_algorithm, window
    if symbol == pyglet.window.key.A:
        show_algorithm = not show_algorithm
        if show_algorithm:
            algButton.btn.color = alg_button_color_show
        else:
            algButton.btn.color = alg_button_color_fast
    if symbol == pyglet.window.key.Q:
        window.close()
    

def run_algorithm():
    global mode, drawingBox, intersectionLocations, show_algorithm, alg_segs_highlight, alg_intersection_highlight, title_text

    # Format all the segments
    bo_segments = []
    for s in segs:
        bo_segments.append(s.ordered())
    # print(bo_segments)
    intersectionLocations, log = bentley_ottman(bo_segments, debug=True, log=True)

    if show_algorithm:
        for action in log:
            title_text = ""
            alg_segs_highlight = []
            alg_intersection_highlight = None
            if "point" in action:
                sweepline_line.x = action["point"][0]
                sweepline_line.y = drawingBox.btn.y
                sweepline_line.x2= action["point"][0] 
                sweepline_line.y2= drawingBox.btn.y + drawingBox.btn.height
            time.sleep(0.5)
            if action["event"] == "add":
                title_text = "Adding Segment"
                alg_segs.append(action["seg"])
                alg_segs_highlight.append({"seg":action["seg"], "color":color_green})
            elif action["event"] == "remove":
                title_text = "Removing Segment"
                alg_segs.remove(action["seg"])
                alg_segs_highlight.append({"seg":action["seg"], "color":color_red})
            elif action["event"] == "intersection":
                title_text = "Swapping Segments"
                alg_segs_highlight.append({"seg":action["int"].seg1, "color":color_purple})
                alg_segs_highlight.append({"seg":action["int"].seg2, "color":color_purple})
                time.sleep(0.5)
            else:
                title_text = "Checking for Intersection"
                alg_segs_highlight.append({"seg":action["seg1"], "color":color_blue})
                alg_segs_highlight.append({"seg":action["seg2"], "color":color_blue})
                time.sleep(1.5)
                if action["result"] is None:
                    title_text = "No Intersection Found"
                    alg_segs_highlight = []
                    alg_segs_highlight.append({"seg":action["seg1"], "color":color_red})
                    alg_segs_highlight.append({"seg":action["seg2"], "color":color_red})
                else:
                    title_text = "Intersection Found"
                    alg_segs_highlight = []
                    alg_segs_highlight.append({"seg":action["seg1"], "color":color_green})
                    alg_segs_highlight.append({"seg":action["seg2"], "color":color_green})
                    alg_intersection_highlight = (action["result"].x, action["result"].y)
                time.sleep(0.5)
            time.sleep(1.5)
        title_text = ""
        alg_segs_highlight = []
        alg_intersection_highlight = None
        time.sleep(0.5)

    mode = "draw"
    return
    

# Drawing to the screen
@window.event
def on_draw():
    global segs, mode, alg_segment, alg_intersection_highlight, alg_segs_highlight, alg_segs, alg_title
    window.clear()

    if mode == "draw":
        clearButton.draw()
        algButton.draw()
        ex1Button.draw()
        ex2Button.draw()
        drawingBox.draw()
            
        for s in segs:
            s.draw()
        for i in intersectionLocations:
            intersectionPoint.x = i.x
            intersectionPoint.y = i.y
            intersectionPoint.draw()
    elif mode == "alg":
        drawingBox.draw()

        alg_title.text = title_text
        alg_title.draw()

        alg_segment.set_color(color_black)
        for o in alg_segs:
            alg_segment.move_endpoint((o.leftPoint.x, o.leftPoint.y), p1=True)
            alg_segment.move_endpoint((o.rightPoint.x, o.rightPoint.y))
            alg_segment.draw()
        for o in alg_segs_highlight:
            alg_segment.set_color(o["color"])
            alg_segment.move_endpoint((o["seg"].leftPoint.x, o["seg"].leftPoint.y), p1=True)
            alg_segment.move_endpoint((o["seg"].rightPoint.x, o["seg"].rightPoint.y))
            alg_segment.draw()
        if alg_intersection_highlight != None:
            intersectionPoint.x = alg_intersection_highlight[0]
            intersectionPoint.y = alg_intersection_highlight[1]
            intersectionPoint.draw()

        sweepline_line.draw()

# I need this wrapper so that we can schedule the draw function to trigger consistently
def on_draw_wrapper(dt):
    on_draw()
    return

# Run the whole thing
pyglet.clock.schedule_interval(on_draw_wrapper, 0.05)
pyglet.app.run()