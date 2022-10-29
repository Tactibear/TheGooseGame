## CL for code
## CL2 for commenting
##create a style for the background image used for the transition days
style opening:
    xalign 0.5
    xfill True
    yfill True
    background "images/Opening.png"
##creates the style that will center the text to the middle of the screen
style Centering:
    xalign 0.5
    yalign 0.5
    spacing 8


##Defines the screen that will draw the background
screen Opening1():
    frame:
        style "opening"
##defines the screen that will create the text onscreen
screen day1():
    hbox:
        style "Centering"
        text('Day one'):
            size 200
            color '#ffffff'
            font 'fonts/Blomberg.otf'
