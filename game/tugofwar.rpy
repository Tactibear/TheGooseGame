##CL2
screen tog():
    if timerstate:
        if timervariance==1:
            timer 0.2 action Return("timedshift") repeat True  
        else:
            timer 0.08 action Return("timedshift") repeat True  

   
        key "n" action [Return("n")]
        key "m" action [Return("m")]
   
    add "e6 hallway.jpg" zoom 0.6
    add "standard ms goose right facing" zoom 0.4 anchor (1.0, 0.0) pos (goosepos, 300)    

label tugofwar:
   
    $losehere = 2000    
    $winhere = 250 
    $goosepos = 1500  
    $previouskey = ""  
    $timerstate = False
    "..."
    show screen tog
    "game start"
    $timerstate = True

    label loopdetect:
        $timervariance=renpy.random.randint(0,2)
        $userinput = ui.interact()
        if goosepos >= losehere:
            $timerstate = False
            jump losetog
        if goosepos <= winhere:
            $ timerstate = False
            jump wintog
       
        if userinput == "timedshift":
            $goosepos += renpy.random.randint(3,10)  
           
       
        if previouskey == "":
            $previouskey = userinput
       
        if userinput == "n" and previouskey != "n":
            $previouskey = "n"
            $goosepos -= 25
        elif userinput == "m" and previouskey != "m":
            $previouskey = "m"
            $goosepos -= 25
       
        jump loopdetect
       

   
label losetog:  
    N "You lost"
    hide screen tog
    jump placeholderreturntog
label wintog:  
    N "You won"
    hide screen tog
    jump placeholderreturntog