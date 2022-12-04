###############            CL,CL2               ################
screen goosechase():
    $ timerstate=True
    layer 'master'
    ##move character
    key "a" action Return("a")  
    key "d" action Return("d")
    key "w" action Return("w")
    key "s" action Return("s")
    ##collect coin
    key "f" action Return("f")
    ##drop coin
    key "g" action Return("g")

    ##base images to be printed on the screen, that will be static
    add "movinggoosebgc.jpg" zoom 4.1
    add "nest.png" pos(xnestpos,ynestpos) zoom 0.3
    #add "standard ms goose.png" pos(xpmove,ypmove) zoom 0.1
    #add "angerenemy" anchor (1,1) pos (xbot1,ybot1) zoom 0.3 
    add "coin.png" pos(xcoinpos,ycoinpos) zoom 0.02 
    text "Score [score]" size 100 xpos 0.7 ypos 0.1 
    text "Lives: [lives]" size 50 xpos 0.7 ypos 0.06
    text "WASD to move\nF to pickup\nG to drop" size 30 xpos 0.87
    

    if msgmove==True:
        add "standard ms goose.png" pos(xpmove,ypmove) zoom 0.1

    ## if game is running, timer is also running, so
    if timerstate==True: 
        ## keep checking if user goes outside screen borders, if yes, block them
        ## easter egg portal game hoohoohoo
        timer 0.1 repeat True action If(xpmove>1900, SetVariable('xpmove', xpmove==1900))
        timer 0.1 repeat True action If(xpmove<0, SetVariable('xpmove', xpmove==0))
        timer 0.1 repeat True action If(ypmove>1000, SetVariable('ypmove', ypmove==1000))
        timer 0.1 repeat True action If(ypmove<0, SetVariable('ypmove', ypmove==0))
        
        ##check bot locations relative to user, and move towards user accordingly
        timer 0.1 repeat True action If(xpmove-210>xbot1, SetVariable('xbot1', xbot1+3))
        timer 0.1 repeat True action If(xpmove-210<xbot1, SetVariable('xbot1', xbot1-3))
        timer 0.1 repeat True action If(ypmove-40>ybot1, SetVariable('ybot1', ybot1+3))
        timer 0.1 repeat True action If(ypmove-40<ybot1, SetVariable('ybot1', ybot1-3))
        # if xpmove-210>xbot1:
        #     $xbot1+=3
        # else:
        #     $xbot1-=3
        # if ypmove-40>ybot1:
        #     $ybot1+=3
        # else:
        #     $ybot1-=3


        ## calculate the distance between user and bot
        $absenxdist=abs(xpmove-xbot1)
        $absenydist=abs(ypmove-ybot1)
        ##keep checking if the two entities are touching
        timer 0.1 repeat True action If(absenxdist<100 and absenydist<100, true=Jump('gettouchedlol'))

        ## timer once again, see buttonmashergame file 
        #timer 0.1 repeat True action If(recordedtime > 0, SetVariable('recordedtime', recordedtime-0.1), false=Jump(recordedtimer_ends))
        timer 1 repeat True action If(recordedtime > 0, true=SetVariable('recordedtime', recordedtime-1), false=Jump(recordedtimer_ends))
        ## if the time is less than 3s, we colour the text red
        if recordedtime <= 20:
            text str(recordedtime) xpos .82 ypos .07 color "#FF0000" size 40
        ## otherwise it should stay green
        else:
            text str(recordedtime) xpos .82 ypos .07 color '#00ff00' size 40
##
##
##
##
## CODE FOR DISPLAY LIVES WILL COME LATER/IF I FEEL LIKE IT
init:
    ## define the layers stuff can be displayed on
    ## master is the default layer for images, and z order sorts items on the same layer
    ## shifting the screen back to master, from the screen layer, so our character sprites aren't covered by the screen.
    ## without the characters being on the screen, we can update their positions constantly based on user inputs, 
    ## without needing to keep calling the screen
    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'ontop' ]

init python:
    import random
    import pygame ## rip bozo, failure, couldn't do it in time
    ##setting up variables 
    msgmove=False
    xcoinpos=-50
    ycoinpos=-50
    xnestpos=100
    ynestpos=100
    ## starting time (s)
    recordedtime = 100
    ogtime=recordedtime
    ## check if the timer_ends variable has been called, and if it has, assign a string that will send us back to script file
    recordedtimer_ends = 'timerendedlol'
    lives=3
label firstcoinmovingspritegame:
    hide screen bars
    $ renpy.block_rollback()
    $ coin_exist=True
    $ coin_collected=False
    $ score=0
    $ xpmove = 500
    $ ypmove = 20
    $ xbot1 = 1000
    $ ybot1 = 600
    $ last_pressed='a'
    show screen goosechase
    $ timerstate=False

    

# label coinrespawn:
#     if score==0:
#         pass
#     else:

label beforemovingspritegame:
    $ timerstate=True
    if coin_exist==True:
        $xcoinpos=renpy.random.randint(100,1800)
        $ycoinpos=renpy.random.randint(100,900)
    else:
        $xcoinpos=-100  
        $ycoinpos=-100
    
label movingspritegame:
    $ xnestpos=100
    $ ynestpos=100
    image standardmsgoose = ConditionSwitch(
        "last_pressed=='a'", "standard ms goose.png",
        "last_pressed=='d'", "standard ms goose right facing.png",
        "last_pressed=='s'", "standard ms goose.png",
        "last_pressed=='w'", "standard ms goose right facing.png",
        "last_pressed=='f'", "standard ms goose.png",
        "True", "standard ms goose right facing.png"
    )
    hide angerenemy
    image angerenemy = ConditionSwitch(
        "xpmove-210>xbot1", "angerenemyright.png",
        "True", "angerenemy.png",
        )
    show angerenemy
    $ timerstate=True
    
    label game_loop:
        hide standardmsgoose
        show standardmsgoose:
            xpos xpmove
            ypos ypmove
            zoom 0.1 
        image standardmsgoose = ConditionSwitch(
        "last_pressed=='a'", "standard ms goose.png",
        "last_pressed=='d'", "standard ms goose right facing.png",
        "last_pressed=='s'", "standard ms goose.png",
        "last_pressed=='w'", "standard ms goose right facing.png",
        "last_pressed=='f'", "standard ms goose.png",
        "True", "standard ms goose right facing.png"
        )
        hide angerenemy 
        show angerenemy:
            xpos xbot1
            ypos ybot1
            zoom 0.3 
        image angerenemy = ConditionSwitch(
            "xpmove-210>xbot1", "angerenemyright.png",
            "True", "angerenemy.png",
            )


        if lives==0:
            jump lostlives
       
        $ res = ui.interact()
        if score==10:
            $timerstate==False
            hide goosechase
            jump gobacktomain
        if res == "a" :
            $ last_pressed = "a"
            play sound "audio/buttonhovereffect.mp3"
            $ xpmove -= 69 
        if res == "d" :
            $ last_pressed = "d"
            play sound "audio/buttonhovereffect.mp3"
            $ xpmove += 69 
        if res == "w" :
            play sound "audio/buttonhovereffect.mp3"
            $ last_pressed = "w"
            $ ypmove -= 69 
        if res == "s" :
            play sound "audio/buttonhovereffect.mp3"
            $ last_pressed = "s"
            $ ypmove += 69  
        $absdistx=abs(xcoinpos-xpmove)
        $absdisty=abs(ycoinpos-ypmove)

        if res=="f" and absdistx<200 and absdisty<200:
            play sound "audio/coinping.mp3"
            $ last_pressed = "f"
            $ coin_collected=True
            
        if coin_collected==True:
            $xcoinpos=xpmove+100
            $ycoinpos=ypmove+60

        $absdistx=abs(xnestpos+80-xpmove)
        $absdisty=abs(ynestpos+80-ypmove)

        if coin_collected==True and res=="g" and absdistx<200 and absdisty<200:
            play sound "audio/coinping.mp3"
            $coin_collected=False
            $ score+=1
            ##Originally wanted to make it so that each coin would sit in a neat little row on the nest, but decided it was more work than it was worth
            $xcoinpos=xnestpos+40+(score*5)
            $ycoinpos=ynestpos+20+(score*5)
            #jump coinrespawn
            jump beforemovingspritegame
            
        jump game_loop
label gettouchedlol:
    $xbot1=xpmove+200
    $lives-=1
    
    jump game_loop
label timerendedlol:
    $timerstate=False
    N "You ran out of time."
    hide screen goosechase
    show screen bars
    jump returnlostlives
label lostlives:
    $timerstate=False
    N "You suck at dodging."
    hide screen goosechase
    show screen bars
    jump returnlostlives
label gobacktomain:
    $timerstate==False
    hide screen goosechase
    show screen bars
    jump day2continue
############## ADDD SOUND EFFECTS AND BETTER BGC AFTER


#                                                                                               ▓▓████▓▓▒▒            
#                                                                                           ░░████▓▓▓▓▓▓▓▓▓▓          
#                                                                                           ██▓▓  ░░▓▓████▓▓▓▓        
#                                                                                           ████░░░░  ▓▓██████▒▒      
#                                                                                         ▓▓████▒▒░░    ▒▒██▓▓▓▓▓▓██▒▒
#                                                                                         ██████▓▓░░░░░░  ▓▓██▒▒      
#                                                                                         ████████░░░░░░▒▒▒▒          
#                                                                                         ██████████▓▓░░              
#                                                                                         ██████████                  
#                                                                                         ██████████                  
#                                                                                       ░░████████▓▓                  
#                                                                                       ░░████████                    
#                                                                                       ██████▓▓██                    
#                                                                                       ██████████                    
#                                                                                       ████▓▓████                    
#                                                                                       ██████████                    
#                                                                                       ██████████                    
#                                                                                       ██████████                    
#                                                                                     ░░████▓▓██▓▓                    
#                                                                                     ▒▒████████▓▓                    
#                                                                                     ██████████▓▓                    
#                                                                                     ████████▓▓▓▓                    
#                                                                                     ██████████▓▓                    
#                                                                                   ░░██████████▓▓                    
#                                                                                   ▓▓██████▓▓▒▒                      
#                                                                                   ▓▓██▓▓▒▒░░░░                      
#                                                                                   ████▓▓░░░░                        
#                                                                                 ▒▒▓▓▓▓▒▒░░░░░░                      
#                                                                                 ▓▓▓▓▒▒░░░░░░░░                      
#                                                                   ░░░░▒▒▒▒░░░░▒▒▓▓▒▒▒▒░░░░░░░░                      
#                                                           ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░                      
#                                                     ░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒░░░░░░░░░░                        
#                                               ░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░                      
#                                           ▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░                        
#                                       ░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░                  
#                                   ░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░                  
#                             ░░▒▒▒▒▓▓▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░                  
#                       ░░▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░                  
#                   ░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░                    
#               ░░▒▒▓▓▓▓▓▓▒▒░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░                    
#         ░░▓▓▓▓▓▓▒▒▓▓▒▒▓▓██▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      
#     ████▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      
# ░░▒▒  ██░░░░████████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░                              
#     ▒▒▓▓████▓▓▓▓██▒▒░░  ░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░                          
#   ▓▓▓▓████▓▓▒▒▒▒░░░░░░░░░░░░░░      ░░░░░░      ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░                            
#                     ░░░░░░░░░░░░░░  ░░░░░░░░    ▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░  ░░                              
#                             ░░░░░░░░░░░░░░░░░░░░  ▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░                                
#                                   ░░░░░░░░░░░░    ░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░                                    
#                                     ░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒░░                                      
#                                         ░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░                                            
#                                             ████░░          ▓▓▒▒░░░░                                                
#                                             ▓▓████          ▒▒▒▒▒▒                                                  
#                                             ▓▓████          ░░▓▓▒▒                                                  
#                                             ██████          ▒▒▓▓░░                                                  
#                                             ██████          ░░▓▓░░                                                  
#                                           ░░████▓▓            ▓▓░░                                                  
#                                           ▒▒██████            ▓▓░░                                                  
#                                           ▓▓██████            ▓▓░░                                                  
#                                           ▒▒▓▓▒▒▓▓            ▓▓░░                                                  
#                                               ▒▒██            ▓▓▒▒                                                  
#                                               ▒▒▓▓          ░░▒▒▒▒                                                  
#                                               ▒▒░░            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓                                      
