import numpy as np
import time
import threading
import copy

import pyglet
from pyglet import shapes
from pyglet.window import mouse, key

from line import line, Location
from button import button

from BentleyOttmann import bentley_ottman

# GLOBAL VARIABLES 
# configurations for the whole program. Best not to mess with them too much. 
is_fullscreen = False
window_size = (800, 600)
background_color = (1, 1, 1)
old_color = (0, 0, 0)
new_color = (100, 200, 150)
border_size = 100
pqCardSize = (60,60)
mode = "draw"

whiteText = (255, 255, 255, 255)
blackText = (0, 0, 0, 255)

# List of drawn segments
segs = []
alg_objs = []
intersectionLocations = []
pqCardLocations = []
pqCardLeftColor = ( 191, 244, 98 )
pqCardRightColor = ( 244, 198, 98 )
pqCardIntersectColor = ( 234, 151, 207 )
pqCard = button("1L", x=0, y=0, width=pqCardSize[0] - 10, height=pqCardSize[1] - 10, buttonColor=(150, 150, 150), textColor=whiteText, font_size=12)
endpoint = shapes.Circle(0, 1, 10, color=(0,0,0))

# Generate the buttons
clearButton = button("CLEAR", x=70, y=30, width=140, height=60, buttonColor=(232, 229, 140), textColor=(255, 255, 255, 255), statechange=None)
algButton = button("RUN", x=190, y=30, width=100, height=60, buttonColor=(140, 232, 165), textColor=(255, 255, 255, 255), statechange=None)
ex1Button = button("Ex. 1", x=300, y=30, width=120, height=60, buttonColor=(243, 124, 68), textColor=(255, 255, 255, 255), statechange=None)
ex2Button = button("Ex. 2", x=420, y=30, width=120, height=60, buttonColor=(243, 177, 68), textColor=(255, 255, 255, 255), statechange=None)
drawingBox = button("", x=window_size[0] / 2.0, y=window_size[1] / 2.0, width=window_size[0] - border_size * 2, height=window_size[1] - border_size * 2, buttonColor=(230, 230, 230), textColor=(255, 255, 255, 255), statechange=None)

# Algorithm Labels
pqBackground = shapes.Rectangle(x=0, y=window_size[1] - border_size + 15, width=window_size[0], height=border_size - 30, color=(200, 200, 200))
pqText = pyglet.text.Label(text="Priority\nQueue", x=border_size * 0.5, y=window_size[1] - border_size * 0.5, align='center', anchor_x='center', anchor_y='center', font_name="Helvetica", font_size=12, bold=True, color=(0,0,0,255), multiline=True, width=border_size)
slBackground = shapes.Rectangle(x=window_size[0] - border_size + 15, y=0, width=border_size - 30, height=window_size[1] - border_size, color=(200, 200, 200))
slText = pyglet.text.Label(text="Sweep\nLine", x=window_size[0] - border_size * 0.5, y=window_size[1] - border_size - 30, align='center', anchor_x='center', anchor_y='center', font_name="Helvetica", font_size=12, bold=True, color=(0,0,0,255), multiline=True, width=border_size)

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
    global mode, segs, second_endpoint, ex1_segs, ex2_segs
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
            if isinstance(anim["obj"], button):
                anim["obj"].move(anim["Pf"][0], anim["Pf"][1])
            else: 
                anim["obj"].x = anim["Pf"][0]
                anim["obj"].y = anim["Pf"][1]
            animation_list.remove(anim)
        else:
            if isinstance(anim["obj"], button):
                anim["obj"].move(anim["Pi"][0] * (1.0 - ratio) + anim["Pf"][0] * ratio, anim["Pi"][1] * (1.0 - ratio) + anim["Pf"][1] * ratio)
            else:
                anim["obj"].x = anim["Pi"][0] * (1.0 - ratio) + anim["Pf"][0] * ratio
                anim["obj"].y = anim["Pi"][1] * (1.0 - ratio) + anim["Pf"][1] * ratio

def run_sample_algorithm():
    global mode, alg_objs, drawingBox, animation_list, pqCardSize, intersectionLocations

    # Draw only the endpoints
    alg_objs = []
    for l in segs:
        alg_objs.append(l.endpoint1)
        alg_objs.append(l.endpoint2)
    # Sort all the endpoints and move them to the PriorityQueue area
    alg_objs = sorted(alg_objs, key=lambda o: (o.x, o.y))
    target_xs = [drawingBox.x - 0.5 * drawingBox.width + 0.5 * pqCardSize[0] + pqCardSize[0] * x for x in range(len(alg_objs))]
    for o in range(len(alg_objs)):
        animation_list.append({"obj":alg_objs[o], "Pi":(alg_objs[o].x, alg_objs[o].y), "Pf":(target_xs[o], window_size[1] - 0.5 * border_size), "time":2.5, "startTime":(time.time() * 1000)})
    time.sleep(5)
    # Replacing all the endpoints with INTERSECTION PQ Cards
    for o in segs:
        intersectionLocations.append(Location(o.endpoint1.x, o.endpoint1.y))
        intersectionLocations.append(Location(o.endpoint2.x, o.endpoint2.y))
        o.reset_endpoints()
    alg_objs = []
    time.sleep(5)
    # Sliding all those PQ cards off the screen
    for o in intersectionLocations:
        animation_list.append({"obj":o, "Pi":(o.x, o.y), "Pf":(window_size[0] + o.x, window_size[1] - 0.5 * border_size), "time":2.5, "startTime":(time.time() * 1000)})
    time.sleep(5)
    intersectionLocations = []
    mode = "draw"
    return

def run_algorithm():
    global mode, alg_objs, drawingBox, animation_list, pqCardSize, intersectionLocations

    # Format all the segments
    bo_segments = []
    for s in segs:
        bo_segments.append(s.ordered())
    print(bo_segments)
    bentley_ottman(bo_segments, debug=True)


#     # First, we want to sort all the endpoints and move them into the priority queue.
#     alg_objs = []
#     for l in segs:
#         alg_objs.append(l.endpoint1)
#         alg_objs.append(l.endpoint2)
#     # Sort all the endpoints and move them to the PriorityQueue area
#     alg_objs = sorted(alg_objs, key=lambda o: (o.x, o.y))
#     target_xs = [drawingBox.x - 0.5 * drawingBox.width + 0.5 * pqCardSize[0] + pqCardSize[0] * x for x in range(len(alg_objs))]
#     for o in range(len(alg_objs)):
#         animation_list.append({"obj":alg_objs[o], "Pi":(alg_objs[o].x, alg_objs[o].y), "Pf":(target_xs[o], window_size[1] - 0.5 * border_size), "time":2.5, "startTime":(time.time() * 1000)})
#     time.sleep(5)
#     alg_objs = []
#     # bo = bentley_ottman_test()
#     while (True):
#         # instruction = next(bo)
#         if instruction["type"] == "PQ":
#             # Load PQ info
#             continue
#         elif instruction["type"] == "Left":
#             # Handle left endpoint from PQ
#             continue
#         elif instruction["type"] == "Intersection":
#             # Handle an intersection from the PQ
#             continue
#         elif instruction["type"] == "Right":
#             # Handle right endpoint from PQ
#             continue
#         elif instruction["type"] == "Done":
#             # Display final segments and intersections
#             break

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

        pqBackground.draw()
        pqText.draw()
        slBackground.draw()
        slText.draw()

        pqCard.text.text = "INT"
        pqCard.btn.color = pqCardIntersectColor
        pqCard.text.color = whiteText
        for p in intersectionLocations:
            pqCard.move(p.x, p.y)
            pqCard.draw()

        pqCard.text.color = blackText
        for p in pqCardLocations:
            if p.data["LR"] == "L":
                pqCard.btn.color = pqCardLeftColor
            else:
                pqCard.btn.color = pqCardRightColor
            pqCard.text.text = "{}{}".format(p.data["num"], p.data["LR"])
            pqCard.move(p.x, p.y)
            pqCard.draw()
        
        for o in alg_objs:
            endpoint.x = o.x
            endpoint.y = o.y
            endpoint.draw()

# I need this wrapper so that we can schedule the draw function to trigger consistently
def on_draw_wrapper(dt):
    on_draw()
    return

# Run the whole thing
pyglet.clock.schedule_interval(on_draw_wrapper, 0.05)
pyglet.app.run()