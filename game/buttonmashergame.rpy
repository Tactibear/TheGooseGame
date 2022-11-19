## CL2
<<<<<<< HEAD
## transformations for the button
transform buttonmashing:
    align(0.5, 0.5)
    zoom 0.5
    xpos 300
    ypos 850
    
## set initial vairables in python
init python:
    ## amount of clicks user does
    clicks=0
    ## sets up variables for timer, these don't really matter, since we just need to define them for now
    ## new values will be assigned to them later
    timer_range = 0
    timer_jump = 0

##potential button up and down animation on clicks, will need to jump to label in button action
##script still janked

# label buttondown:
#     show 1goosebutton_hover at buttonmashing
#     pause 0.1
#     hide 1goosebutton_hover at buttonmashing

label clickergamelabelentry1:
    ## starting time (s)
    $time = 10
    ## check if the timer_ends variable has been called, and if it has, assign a string that will send us back to script file
    $timer_ends = 'returnfromclickers'

    ## part of button animation framework
    ##show 1goosebutton_idle at buttonmashing

    ##activate screen with the image button and timer text on it 
    call screen clickers

screen clickers():
    ##create a container for the background, biggest, so declared first, and takes the entirety of the outermost frame (app screen)
    frame:
        ## show the background, zoomed smaller
        image "e6studyspace2.jpg" zoom 0.55
        ## in a horizontal container, 
        hbox:
            ## give margins of 10px
            spacing 10
            ## align in the center of the outer box (x,y) relative positioning, in this case, the frame
            align(0.5,0.5)
            ## display text that displays the clicks made by the player, define size, position appropriately 
            text "Score [clicks]" size 40 xpos 0.1 ypos 0.1 
        ## in another container
        hbox:
            #align 0.5

            ## two timer counts here, one counts the tenths, and another the ones columns for numbers, counting down from 10s defined before

            ## check every 0.1/1 seconds, if the timer is larger than 0, we continue subtracting 0.1 and 1 from the timer, and assigning that new value to time again
            ## if we hit 0, when its no longer true, we jump to the timer_ends variable, which brings us back to the main screen
            timer 0.1 repeat True action If(time > 0, SetVariable('time', time-0.1), false=Jump(timer_ends))
            timer 1 repeat True action If(time > 0, true=SetVariable('time', time-1), false=Jump(timer_ends))
            ## if the time is less than 3s, we colour the text red
            if time <= 3:
                text str(time) xpos .1 ypos .1 color "#FF0000" 
            ## otherwise it should stay green
            else:
                text str(time) xpos .1 ypos .1 color '#00ff00'
    ## this is the button the user clicks on, add 1 to the clicks variable every time it detects a user input on it, and play a sound
    ## give it the transformations defined by the buttonmashing style
    imagebutton auto "images/1goosebutton_%s.png" action [SetVariable("clicks",clicks+1),Play(config.has_sound,"audio/buttonhovereffect.mp3",selected=None)] at buttonmashing

## if we jump here, we go back to main code script
label returnfromclickers:
    hide clickers
=======
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
>>>>>>> 37d109f (DDR game code with other working files)
    jump returnfromclicker




    
    

    


