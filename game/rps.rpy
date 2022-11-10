transform buttonformat:
    zoom 0.7
    rotate -90
transform goosegodimage:
    zoom 0.7
init python:
    userscore=0
    compscore=0
    userchoice=''
    
label rpsfinal:
    ## starting time (s)
    $time = 10

    $timer_ends = 'returnfromfirstgameentry'
    call screen rpstest
    

screen rpstest():
    frame:
        image "fightinggod.jpg" zoom 0.8
        hbox:
            spacing 10
            align(0.5,0.5)
            text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    
        
    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) at buttonformat action NullAction()
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) at buttonformat action NullAction()
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) at buttonformat action NullAction()
  
    imagebutton auto "goosegod_%s.png" align(-1.2, 0.4) action NullAction() at goosegodimage

