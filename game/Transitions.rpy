# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over

## CL for code
## CL2 for commenting
##create a style for the background image used for the transition days
style opening:
    ## center the opening
    xalign 0.5
    ## allow for the image to stretch the height and width of screen
    xfill True
    yfill True
    ##set the background itself
    background "images/Opening.png"
##creates the style that will center the text to the middle of the screen
style Centering:
    ##align the text
    xalign 0.5
    yalign 0.5
    ##spacing between text
    spacing 8


##Defines the screen that will draw the background
screen Opening1():
    frame:
        ##in its separate container, set the style to defined above
        style "opening"
##defines the screen that will create the text onscreen, this will be overlayed on top of the previous screen 
## to create the full display
screen day1():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using pythong print since it can't be formatted as easily
        text('Day one'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'
