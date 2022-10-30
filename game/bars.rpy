# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over

## CL2 - all
##define a style group, all items that is defined by this style will have the changes below applied to them
style bars:
    ##the background bar will be set by an image in the files
    right_bar "barfill.png"
    xysize(400,35)
    xalign 0.08
    yalign 0.10
    
#>>>>>>> cca2120 (updated transitiojns)

screen bars:
    ## create a display bar
    bar: 
        ## apply the style to this bar
        style "bars"
        ## make it dependant on the defined variable in the script file
        ## (current value, max value)
        value VariableValue("shipfavour",100)
        ##overtop of the defined bar, which will be in the background, have the bar filler overtop
        left_bar "barfiller.png"
#<<<<<<< HEAD
        #xysize(400,24)

        #xalign 0.05
#=======
        ## define size again
        xysize(400,35)
        ##align once again
        xalign 0.08

        yalign 0.05
