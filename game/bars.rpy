# # Camilo - CL
# # Charles - CL2
# # Emily - EM
# # Stephanie - SL
# # SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over

###############           CL2                ################
style bar:
    bar_resizing True

screen bars:
    ## set vbox to not disrupt the other on screen elements, since it spans downwards
    vbox:
        ## background for display bar
        frame:
            background "barbackground.png"
            ##set max value
            $maxshipfavour=120
            ##align against vbox
            xalign 0.5
            yalign 0.05
            ## max value, in pixels
            xmaximum 800
            ##set the current and max vaues, and the time it takes for animation to play
            bar value AnimatedValue(shipfavour, maxshipfavour, delay = 1.0):
                ## bar positions relative to bar background, the max, and what it is made of
                xpos 70
                yalign 0.075
                xmaximum(500)
                left_bar Frame("goosedispbar", 75, 10)
                right_bar Frame("barfiller.png", 100, 10)
            # bar:
                # xmaximum 382
                # yalign 0.075
                # xpos 70
                # value shipfavour
                # range 120
                # right_bar "barfiller.png" 
                # left_bar "goosedispbar.png" 
            ## text for the score, to be displayed under the bar
            hbox:
                yalign 0.115
                xpos 70
                text "[shipfavour]/[maxshipfavour] " xalign 0 yalign 0.02 color '#000000' font "fonts/Blomberg.otf"
