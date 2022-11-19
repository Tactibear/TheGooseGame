## CL2
transform buttonmasherformat:
    zoom 0.4

    align(0.33,1.0)

## set initial variables
init python:
    ## amount of clicks user does
    clicks=0
    ## sets up variables for timmer
    timer_range = 0
    timer_jump = 0
    
label clickergamelabel:
    ## starting time (s)
    $time = 10

    $timer_ends = 'returnfromfirstgameentry'
    call screen clickers
    
screen clickers():
    frame:
        image "e6studyspace2.jpg" zoom 0.55
        hbox:
            spacing 10
            align(0.5,0.5)
            text "Score [clicks]" size 40 xpos 0.1 ypos 0.1 
    
        hbox:
            #align 0.5
            timer 0.1 repeat True action If(time > 0, SetVariable('time', time-0.1), false=Jump(timer_ends))
            timer 1 repeat True action If(time > 0, true=SetVariable('time', time-1), false=Jump(timer_ends))
            if time <= 3:
                text str(time) xpos .1 ypos .1 color "#FF0000" 
            else:
                text str(time) xpos .1 ypos .1 color '#00ff00'

    imagebutton auto "images/goosebutton_%s.png" align(0.5, 0.5) action [SetVariable("clicks",clicks+1),Play(config.has_sound,"audio/buttonhovereffect.mp3",selected=None)] at buttonmasherformat 

label returnfromfirstgameentry:
    jump returnfromclicker