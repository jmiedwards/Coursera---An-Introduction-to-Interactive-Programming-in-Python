# This is for codeskulptor, an online implementation of python in JS
# Codeskulptor is free and can be found at www.codeskulptor.org
# This will not run in a standard python compiler


# Import relevant modules
import simplegui
import math

# Initialize environment variables
message = "00:00.0"
t = 0
win_count = 0
game_count = 0
is_going = 0

# Event Handlers for buttons

# Click to start
def start():
    global is_going
    is_going = 1
    timer.start()

#Click to stop
def stop():
    global game_count, win_count, is_going
    timer.stop()
    game_count = game_count + is_going
    if message[-1] == '0' and is_going:
        win_count += 1
    is_going = 0

#Click to Reset
def reset():
    global t, message, game_count, win_count, is_going
    game_count = 0
    win_count = 0
    is_going = 0
    timer.stop()
    t = 0
    format(t)

# Event handler for timer
def time():
    global t
    t += 1
    format(t)

# Time unit calculations, calculates minutes, seconds and tenths of seconds from
# tenths of second time() iteration
def format(t):
    global message

    '''milisecond calc'''
    ms_calc = str(t)
    ms = ms_calc[-1]
    
    '''second calc'''
    s_calc = math.floor((t % 600)/10)
    if s_calc <= 59:
        s = s_calc
    else:
        s = 0
    
    '''minute calc'''
    m = math.floor(t/600)

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
    tenth_s_format = str(ms)

    '''concatenate for draw message'''
    message = minute_format + ':' + second_format + '.' + tenth_s_format

# Create timer
timer = simplegui.create_timer(100, time)

# Draw Handler
def draw(canvas):
    canvas.draw_text(message, [100,112], 48, "White")
    canvas.draw_text(str(win_count) + " / " + str(game_count), (250, 20), 20, "Green")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()                                                                                                                                                   
    


