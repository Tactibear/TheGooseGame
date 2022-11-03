## format the actual button (replace with better image later on)
transform buttonformat:
    zoom 0.4
    xzoom 0.9
    yzoom 0.8
    align(0.24,1.0)

## set initial vairables
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
            timer 0.1 repeat True action If(time > 0, SetVariable('time', time - 0.1), false=Jump(timer_ends))
            timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=Jump(timer_ends))
            if time <= 3:
                text str(time) xpos .1 ypos .1 color "#FF0000" 
            else:
                text str(time) xpos .1 ypos .1 color '#00ff00'

    imagebutton auto "images/goosebutton_%s.png" align(0.5, 0.5) action [SetVariable("clicks",clicks+1),Play(config.has_sound,"audio/buttonhovereffect.mp3",selected=None)] at buttonformat 

    

label returnfromfirstgameentry:
    jump returnfromfirstgame




    
    

    


