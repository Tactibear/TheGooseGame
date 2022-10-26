# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME


# main game script


# give character a name and define to a variable
define mG = Character("Mr Goose")

# dialogue starts here
label start:

    # background here, just add file name, no file format at end
    scene placeholder

    # show the character sprite, no file format at end eiother
    show angry mr goose 

    # dialogue starts here, from above defined character
    ## want about 875x875 pixel image for best results
    mG "ima smack the taste out of yo mouth if you don't stop with the amongus jokes"
    hide angry mr goose 
    show blushing mr goose right facing 
    mG "omg no way its the red imposter"

    
    # game ends here, return to main screen
    return
