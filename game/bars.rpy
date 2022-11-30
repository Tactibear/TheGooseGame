# # Camilo - CL
# # Charles - CL2
# # Emily - EM
# # Stephanie - SL
# # SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over

###############           CL2                ################
style bar:
    bar_resizing True

    
    
## ADD a background for the bar so text can be seen better
## add sound effect when bar value changes
screen bars:
    vbox:

        frame:
            background "barbackground.png"
            
            $maxshipfavour=120
            xalign 0.5
            yalign 0.05
            xmaximum 382
            bar:
                xmaximum 382
                yalign 0.075
                xpos 70
                value shipfavour
                range 120
                right_bar "barfiller.png" 
                left_bar "goosedispbar.png" 
            hbox:
                yalign 0.105
                xpos 70
                text "[shipfavour]/[maxshipfavour] " xalign 0 yalign 0.02 color '#000000' font "fonts/Blomberg.otf"
