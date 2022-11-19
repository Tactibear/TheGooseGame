# # Camilo - CL
# # Charles - CL2
# # Emily - EM
# # Stephanie - SL
# # SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over

# ## CL2 - all
style bar:
    bar_resizing True
## ADD a background for the bar so text can be seen better
## add sound effect when bar value changes
screen bars:
<<<<<<< HEAD
    ## we will always be showing this screen, over top of any other screen
    vbox:
        ## align to top left corner
        xalign 0.04
        yalign 0.04
        ## inside box, have the bar
        hbox:
            ##set max the bar can be set to
            $maxshipfavour=120
            ##center the box relative to vertical box
            xalign 0.5
            yalign 0.05
            ## set x (pixels) max for the box
            xmaximum 382
            ## set bar value to the shipfavour, defined in script
            bar:
                value shipfavour
                ##max set 
                range 120
                ## define foreground/background bar images
                right_bar "barfiller.png" 
                left_bar "goosedispbar.png" 
        hbox:
            ##display current bar score to user, with alignments and colours
=======
    vbox:
        xalign 0.04
        yalign 0.04
        hbox:
            $maxshipfavour=120
            xalign 0.5
            yalign 0.05
            xmaximum 382
            bar:
                value shipfavour
                range 120
                right_bar "barfiller.png" 
                left_bar "goosedispbar.png" 
        hbox:
>>>>>>> 37d109f (DDR game code with other working files)
            text "[shipfavour]/[maxshipfavour] " xalign 0 yalign 0.02 color '#000000'
        



