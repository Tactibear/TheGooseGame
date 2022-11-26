###############            CL2               ################
screen moviegamescreen():
    ##move character
    key "a" action Return("a")  
    key "d" action Return("d")
    key "w" action Return("w")
    key "s" action Return("s")
    ##collect coin
    key "f" action Return("f")
    ##drop coin
    key "g" action Return("g")

    ##bases
    add "movinggoosebgc.jpg" zoom 4.1
    add "nest.png" pos(xnestpos,ynestpos) zoom 0.3
    add "standard ms goose" anchor (1.0, 0.0) pos (xmove, ymove) zoom 0.1 
    add "angerenemy" anchor (1,1) pos (xbot1,ybot1) zoom 0.3 
    add "coin.png" pos(xcoinpos,ycoinpos) zoom 0.02
    text "Score [score]" size 100 xpos 0.7 ypos 0.1 
    
    ## face directions based on user input 
    # image standardmsgoose = ConditionSwitch(
    #     last_pressed="a", "standard ms goose.png",
    #     last_pressed="d", "standard ms goose right facing.png"
    # )
            
    if timerstate==True: 
        
        timer 0.1 repeat True action If(recordedtime > 0, SetVariable('recordedtime', recordedtime-0.1), false=Jump(recordedtimer_ends))
        timer 1 repeat True action If(recordedtime > 0, true=SetVariable('recordedtime', recordedtime-1), false=Jump(recordedtimer_ends))
        ## if the time is less than 3s, we colour the text red
        if recordedtime <= 20:
            text str(recordedtime) xpos .82 ypos .07 color "#FF0000" 
        ## otherwise it should stay green
        else:
            text str(recordedtime) xpos .82 ypos .07 color '#00ff00'
##
##
##
##
## CODE FOR DISPLAY LIVES WILL COME LATER/IF I FEEL LIKE IT

init python:
    import random
    import pygame
    ## starting time (s)
    recordedtime = 100
    ogtime=recordedtime
    ## check if the timer_ends variable has been called, and if it has, assign a string that will send us back to script file
    recordedtimer_ends = 'timerendedlol'
    lives=3
label firstcoinmovingspritegame:
    N "game start"
    $ coin_exist=True
    $ coin_collected=False
    $ score=0
    $ xmove = 500
    $ ymove = 20
    $ xbot1 = 1000
    $ ybot1 = 600
# label coinrespawn:
#     if score==0:
#         pass
#     else:

label beforemovingspritegame:
    if coin_exist==True:
        $xcoinpos=renpy.random.randint(100,1800)
        $ycoinpos=renpy.random.randint(100,900)
    else:
        $xcoinpos=-100  
        $ycoinpos=-100
label movingspritegame:
    
    $ timerstate=False
    $ xnestpos=100
    $ ynestpos=100

    show screen moviegamescreen
    $ timerstate=True
    label game_loop:
        if lives==0:
            jump lostlives
        if xmove>xbot1:
            $xbot1+=3
        else:
            $xbot1-=3
        if ymove>ybot1:
            $ybot1+=3
        else:
            $ybot1-=3
        $absenxdist=abs(xmove-xbot1-250)
        $absenydist=abs(ymove-ybot1)
        if absenxdist<200 and absenydist<150:
            jump gettouchedlol
        
        # if xbot1>1800:
        #     $xbot1==1790


        # $ybot1
        # if ybot1>900:
        #     $ybot1==900
       
        $ res = ui.interact()
        if score==10:
            $timerstate==False
            hide moviegamescreen
            jump gobacktomain
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
        $absdistx=abs(xcoinpos-xmove)
        $absdisty=abs(ycoinpos-ymove)

        if res=="f" and absdistx<200 and absdisty<200:
            $ last_pressed = "f"
            $ coin_collected=True
            
        if coin_collected==True:
            $xcoinpos=xmove-100
            $ycoinpos=ymove+70

        $absdistx=abs(xnestpos+80-xmove)
        $absdisty=abs(ynestpos+80-ymove)

        if coin_collected==True and res=="g" and absdistx<200 and absdisty<100:
            $coin_collected=False
            $ score+=1
            $xcoinpos=xnestpos+40+(score*5)
            $ycoinpos=ynestpos+20+(score*5)
            #jump coinrespawn
            jump beforemovingspritegame
            
        jump game_loop
label gettouchedlol:
    $xbot1=xmove+200
    $lives-=1
    N "Got hit"
    jump game_loop
label timerendedlol:
    $timerstate==False
    N "You ran out of time."
    jump returnlostlives
label lostlives:
    $timerstate==False
    N "You suck at dodging."
    jump returnlostlives
label gobacktomain:
    $timerstate==False
    hide moviegamescreen
    jump day2continue
############## ADDD SOUND EFFECTS AND BETTER BGC AFTER
