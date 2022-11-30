## CL2
transform buttonmasherformat:
    zoom 0.4

    align(0.33,1.0)

###############           CL2                ################
## set initial variables
init python:
    ## amount of clicks user does
    clicks=0
    ## sets up variables for timmer
    timer_range = 0
    timer_jump = 0
    
label clickergamelabel:
    ## starting time (s)
    play music buttonmash
    $time = 15

    $timer_ends = 'returnfromfirstgameentry'
    call screen clickers
    
screen clickers():
    frame:
        image "e6studyspace2.jpg"
        window:
            align(0.5,0.5)

            hbox:
                spacing 10
                align(0.5,0.5)
                text "{b}Score [clicks]{b}" size 40 xpos 0.1 ypos 0.1 
        fixed:

            hbox:
                xalign 0.25
                yalign -0.08

                image "clock2.png"
            hbox:
                xalign 0.3
                yalign 0.2
                timer 0.1 repeat True action If(time > 0, SetVariable('time', time-0.1), false=Jump(timer_ends))
                timer 1 repeat True action If(time > 0, true=SetVariable('time', time-1), false=Jump(timer_ends))
                if time <= 5:
                    text str(time) xpos .5 ypos .3 color "#ad0a0a" 
                else:
                    text str(time) xpos .5 ypos .3 color '#0c960c'

    imagebutton auto "images/goosebutton_%s.png" align(0.5, 0.5) focus_mask True action [SetVariable("clicks",clicks+1),Play(config.has_sound,"audio/buttonhovereffect.mp3",selected=None)] at buttonmasherformat 

label returnfromfirstgameentry:
    jump returnfromclicker