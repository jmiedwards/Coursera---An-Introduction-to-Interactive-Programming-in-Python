# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import math

message = "00:00.0"
ms = 0
s = 0
m = 0
t = 0
interval = 100

# Click to start
def start():
    global t
    global message
    timer.start()

#Click to stop
def stop():
    global message
    global t
    timer.stop()

#Click to Reset
def reset():
    global message
    global m
    global s
    global ms
    global t
    ms = 0
    m = 0
    s = 0
    t = 0
    timer.stop()
    message = "00:00.0"

# Handler for time
def time():
    global message
    global t
    t += 1
    time_calc()

# Time unit calculations
def time_calc():
    global m
    global s
    global ms
    global t

    '''milisecond calc'''
    ms_calc = str(t)
    ms = ms_calc[-1]
    '''second calc'''
    s_calc = round((t % 600)/10)
    if s_calc <= 59:
        s = s_calc
    else:
        s = 0
        '''minute calc'''
        m = math.floor(t/600)
        format_message()

# Formatting functions
def format_message():
    global message
    global m
    global s
    global ms
    '''string conditionals for minutes'''
    if m < 10:
        minute_format = '0' + str(m)
    else: 
        minute_format = str (m)
        '''string conditionals for seconds'''    
    if s < 10:
        second_format = '0' + str(s)
    else:
        second_format = str(s)

    '''string function for miliseconds'''
    milisecond_format = str(ms)

    '''concatenate for draw message'''
    message = minute_format + ':' + second_format + '.' + milisecond_format

# Create timer
timer = simplegui.create_timer(interval, time)

# Draw Handler
def draw(canvas):
    canvas.draw_text(message, [100,112], 48, "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()                                                                                                                                                   

