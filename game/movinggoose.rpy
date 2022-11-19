##CL2
screen moviegamescreen():
    ##move character
    key "a" action Return("a")  
    key "d" action Return("d")
    key "w" action Return("w")
    key "s" action Return("s")
    key "f" action Return("collect")

    ##bases
    add "qnc basement.jpg" 
    add "square.png" anchor (1.0, 0.0) pos (xmove, ymove)
    if timerstate==True:
        timer 0.1 repeat True action If(movietime > 0, SetVariable('movietime', movietime-0.1), false=Jump(movietimer_ends))
        timer 1 repeat True action If(movietime > 0, true=SetVariable('movietime', movietime-1), false=Jump(movietimer_ends))
        ## if the time is less than 3s, we colour the text red
        if movietime <= 3:
            text str(movietime) xpos .1 ypos .1 color "#FF0000" 
        ## otherwise it should stay green
        else:
            text str(movietime) xpos .1 ypos .1 color '#00ff00'

init python:
    import random
    import pygame
    ## starting time (s)
    movietime = 100000
    ## check if the timer_ends variable has been called, and if it has, assign a string that will send us back to script file
    movietimer_ends = 'movieoutoftime'

label movingspritegame:
    $ timerstate=False

    $ xmove = 200
    $ ymove = 200

   
    N "..."
   
    N "game start"
    window hide
    show screen moviegamescreen
    $ timerstate=True
    label game_loop:
        $ res = ui.interact()

        if res == "a" :
            $ last_pressed = "a"
            $ xmove -= 69 
        if res == "d" :
            $ last_pressed = "d"
            $ xmove += 69 
        if res == "w" :
            $ last_pressed = "w"
            $ ymove -= 69 
        if res == "s" :
            $ last_pressed = "s"
            $ ymove += 69    
        jump game_loop