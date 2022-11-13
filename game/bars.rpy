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
            text "[shipfavour]/[maxshipfavour] " xalign 0 yalign 0.02 color '#000000'
        



