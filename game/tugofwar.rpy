###############           CL2                ################
init python:
    ##setting some fancy bouncy variables
    gooseorient=0
    randelevate=0
    goosevol=1.8
## i have lost so much sanity trying to integrate pygame within python within renpy i should not have done this
## how did i even get here
screen tog():
    if timerstate1:
        ## a little variance in timer to spice up the rope pulling movements
        if timervariance==1:
            timer 0.2 action Return("timedshift") repeat True  
        else:
            timer 0.08 action Return("timedshift") repeat True  

        ## user input keys to return
        key "n" action [Return("n")]
        key "m" action [Return("m")]
    ## displayables within the screen, position relatively to the user (goose)
    add "e7 lobby.jpg" zoom 0.6
    add "rope1.png" zoom 1.3 anchor (0.6, 0.0) pos (goosepos+1050, 840+randelevate) 
    add "pulling ms goose.png" zoom 0.7 anchor (1.0, 0.0) pos (goosepos, 330+randelevate) rotate gooseorient
      

label tugofwar:
    show screen tog
    play music "audio/Fluffing-a-Duck-KevinMcleod.mp3"
    ## set winning/losing conditions
    $losepos = 2300    
    $winpos = 450 
    $goosepos = 1500  
    $previouskey = ""  
    $timerstate1 = False
    "..."
    "Alternate N and M to move"
    
    "game start"
    $timerstate1 = True

    

    label loopdetect:
        $goosevol=(goosepos/losepos)*5
        $timervariance=renpy.random.randint(0,2)
        $userinput = ui.interact()
        ##check to see if userpos is past either condition for game ending
        if goosepos >= losepos:
            $timerstate1 = False
            jump losetog
        if goosepos <= winpos:
            $ timerstate1 = False
            jump wintog
        ## make it so that at a random interval, goose honks while it pulls 
        ## this is to make sure the user can hear its distress and maybe realize they should
        ## maybe be better at the game
        if userinput == "timedshift":
            $prevpos=goosepos
            $goosepos += renpy.random.randint(3,25)  
            if goosepos-prevpos>23:
                play sound "audio/honk.mp3" volume 3
           
        ##set the previous key pressed to the userinput
        if previouskey == "":
            $previouskey = userinput
        ## make sure the user has to alternate keys for the goose to be pulling back against the rope,
        ## dont want them spamming the same key 
        ## this matchup is biased for osu players to have a fighting chance in an otherwise alien environment 
        if userinput == "n" and previouskey != "n":
            $previouskey = "n"
            $goosepos -= 25
            $gooseorient+=10
            $randelevate-=10

        elif userinput == "m" and previouskey != "m":
            $previouskey = "m"
            $goosepos -= 25
            $gooseorient-=10
            $randelevate+=10
        jump loopdetect
## go back to script, depending on result
label losetog:  
    N "You lost"
    hide screen tog
    jump returnfromtog
label wintog:  
    N "You won"
    hide screen tog
    jump returnfromtog
