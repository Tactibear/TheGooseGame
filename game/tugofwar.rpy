##CL2
init python:
    gooseorient=0
    randelevate=0
    goosevol=1.8
screen tog():
    if timerstate:
        if timervariance==1:
            timer 0.2 action Return("timedshift") repeat True  
        else:
            timer 0.08 action Return("timedshift") repeat True  

   
        key "n" action [Return("n")]
        key "m" action [Return("m")]
   
    add "e7 lobby.jpg" zoom 0.6
    add "rope1.png" zoom 1.3 anchor (0.6, 0.0) pos (goosepos+1050, 840+randelevate) 
    add "pulling ms goose.png" zoom 0.7 anchor (1.0, 0.0) pos (goosepos, 330+randelevate) rotate gooseorient
      

label tugofwar:
    play music "audio/Fluffing-a-Duck-KevinMcleod.mp3"
    $losepos = 2300    
    $winpos = 450 
    $goosepos = 1500  
    $previouskey = ""  
    $timerstate = False
    "..."
    "Alternate N and M to move"
    show screen tog
    "game start"
    $timerstate = True

    

    label loopdetect:
        $goosevol=(goosepos/losepos)*5
        $timervariance=renpy.random.randint(0,2)
        $userinput = ui.interact()
        if goosepos >= losepos:
            $timerstate = False
            jump losetog
        if goosepos <= winpos:
            $ timerstate = False
            jump wintog
       
        if userinput == "timedshift":
            $prevpos=goosepos
            $goosepos += renpy.random.randint(3,25)  
            if goosepos-prevpos>23:
                play sound "audio/honk.mp3" volume 1.8
           
       
        if previouskey == "":
            $previouskey = userinput
       
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
label losetog:  
    N "You lost"
    hide screen tog
    jump returnfromtog
label wintog:  
    N "You won"
    hide screen tog
    jump returnfromtog
