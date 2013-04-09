# This is for codeskulptor, an online implementation of python in JS
# Codeskulptor is free and can be found at www.codeskulptor.org
# This will not run in a standard python compiler


# Import relevant modules
import simplegui
import math

# Initialize environment variables
message = "00:00.0"
ms = 0
s = 0
m = 0
t = 0
interval = 100
win_counter = 0
total_counter = 0

# Event Handlers for buttons

# Click to start
def start():
    global t
    global message
    timer.start()

#Click to stop
def stop():
    global message
    global t
    global total_counter
    global win_counter
    timer.stop()
    total_counter += 1
    if ms = 0:
        win_counter += 1

#Click to Reset
def reset():
    global message
    global m
    global s
    global ms
    global t
    global win_counter
    global total_counter
    ms = 0
    m = 0
    s = 0
    t = 0
    win_counter = 0
    total_counter = 0
    timer.stop()
    message = "00:00.0"

# Event handler for timer
def time():
    global message
    global t
    t += 1
    time_calc()

# Time unit calculations, calculates minutes, seconds and tenths of seconds from
# tenths of second time() iteration
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
    
    '''calls message format function'''
    format_message()

# Formatting time unit functions to draw on canvas
def format_message():
    global message
    global m
    global s
    global ms

    '''string formatting for minutes'''
    if m < 10:
        minute_format = '0' + str(m)
    else: 
        minute_format = str (m)
    
    '''string formatting for seconds'''    
    if s < 10:
        second_format = '0' + str(s)
    else:
        second_format = str(s)

    '''string formatting for tenths of seconds'''
    milisecond_format = str(ms)

    '''concatenate for draw message'''
    message = minute_format + ':' + second_format + '.' + milisecond_format

# Create timer
timer = simplegui.create_timer(interval, time)

# Draw Handler
def draw(canvas):
    canvas.draw_text(message, [100,112], 48, "White")
    canvas.draw_text(counter_text, [0,0], 30, "Red")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()                                                                                                                                                   
# Stopwatch game component
def counter_text():
    global win_counter
    global total_counter
    global counter_text
    win_counter_text = str(win_counter)
    total_counter_text = str(total_counter)
    counter_text = win_counter_text + " / " + total_counter_text 
    


