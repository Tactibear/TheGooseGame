###############           CL2                ################
transform buttonmasherformat:
    zoom 0.4

    align(0.33,1.0)

## Hi Prof. Pendar
## hope you're enjoying our game/code so far
## pls feature us for next years new admitted undergrad shadow day when you talk to the new dudes in the classroom demo
## that was kinda why we did this in the first place

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
    ## preset time
    $time = 15

    $timer_ends = 'returnfromfirstgameentry'
    ## activate game bweep bweeop
    call screen clickers
    
screen clickers():
    ## set a frame within the window, to stretch across entire screen
    frame:
        ## image will span the entire frame
        image "e6studyspace2.jpg"
        ##window within frame is centered
        window:
            align(0.5,0.5)
            ## multiple "horizontal boxes" auto align elements next to each other, like a container
            hbox:
                ## inside the box, align center, with a text display for userscore
                spacing 10
                align(0.5,0.5)
                text "{b}Score [clicks]{b}" size 40 xpos 0.1 ypos 0.1 
        fixed:
            ## in a fixed box, that will not position itself relative to the other boxes in the same frame
            hbox:
                ## make a base clock
                xalign 0.25
                yalign -0.08

                image "clock2.png"
            hbox:
                ## set a timer within the clock, so it can overlay and won't push the image away instead
                ## for some weird reason, the timer has a single decimal place and is centered in the clock for some computers
                ## but for others, it has a bunch of decimal places and offset from clock
                ## weird bug? satans way of stopping our insane goose game? who knows
                xalign 0.314
                yalign 0.2
                ## as long as "time" variable is greater than 0, the timer will subtract 0.1/1 seconds from the variable, for every 0.1/1 second increment
                ## if time hits 0, we jump to the timer end label
                #timer 0.1 repeat True action If(time > 0.1, SetVariable('time', time-0.1), false=Jump(timer_ends))
                timer 1 repeat True action If(time > 0, true=SetVariable('time', time-1), false=Jump(timer_ends))
                ## set text colour when timer below a certain time
                if time <= 5:
                    text str(time) xpos .5 ypos .3 color "#ad0a0a" 
                else:
                    text str(time) xpos .5 ypos .3 color '#0c960c'
    ##clickable element, with sound plays when clicked and returns a variable when clicked
    imagebutton auto "images/goosebutton_%s.png" align(0.5, 0.5) focus_mask True action [SetVariable("clicks",clicks+1),Play(config.has_sound,"audio/buttonhovereffect.mp3",selected=None)] at buttonmasherformat 
## go back to main script
label returnfromfirstgameentry:
    jump returnfromclicker