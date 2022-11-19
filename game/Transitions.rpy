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

## CL
screen day1():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('Day One'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'

## CL, CL2
screen day2():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('Day Two'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'

screen day3():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('Day Three'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'

screen day4():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('Day Four'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'

screen day5():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('Day Five'):
            ##size in pixels
            size 200
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'
##CL endgame screens that are conditional based off the likeability meter and the transitions to the 1B term
##CL comments
screen Timeskip():
    frame:
        xalign 0.5
        ## allow for the image to stretch the height and width of screen
        xfill True
        yfill True
        ##set the background itself
        background "images/Opening.png" ###maybe change this when theres a chance to
screen TimeSkipText1():
    hbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('A few Moments later'):
            ##size in pixels
            size 100
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'
screen TimeSkipText2():
    vbox:
        ##in its separate container, set the style to defined above
        style "Centering"
        ## type out text, not using python print since it can't be formatted as easily
        text('You find yourself in your 1B term'):
            ##size in pixels
            size 100
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'

##CL creating end of the game screen with credits
screen EndCreditsBG():
    frame:
        xalign 0.5
        ## allow for the image to stretch the height and width of screen
        yfill True
        ##set the background itself
        background "images/Opening.png" ###maybe change this when theres a chance to a background image for the credits

screen EndCredits1():
    frame:
        xalign 0.5
        ## allow for the image to stretch the height and width of screen
        yfill True
        ##set the background itself
        background "images/ana.png" ###maybe change this when theres a chance to a background image for the credits
    vbox:
            ##align the text
        xalign 0.8
        yalign 0.3
        ##spacing between text
        spacing 10
        ## type out text, not using python print since it can't be formatted as easily
        text('Created by sacrificing the mental health of:\n Charles Liu\n Camilo Llanten\n Emily Medved\n Stephanie Li'):
            ##size in pixels
            size 50
            ##set colour
            color '#ffffff'
            ## set font
            font 'fonts/Blomberg.otf'
## CL function that scrolls the text in the end credits we need images for it to work
label endcredits2:
    show screen my_keys()
    $ renpy.block_rollback()
    $ credits_speed = 25 #scrolling speed in seconds
    scene white #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show text(credits_s) at Move((0.5, 4.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    hide screen my_keys
    return
init python:
    credits = ('Backgrounds', 'aah'), ('Backgrounds', 'UwU'), ('Sprites and CG', 'my mental health'), ('GUI', 'Charles\'s work ethic'), ('Writing', 'emily and steph\'s'), ('Writing', 'fanfic dreams'), ('Programming', '2AM code with snapple'), ('Music', 'nintendo daddys music'), ('Music', 'boutta get copyright striked')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to our Ren'py version
##CL try to disable the functionality of skipping through some text/scenes