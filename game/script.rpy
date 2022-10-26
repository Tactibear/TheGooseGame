# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME


# main game script


# give character a name and define to a variable

define N = Character("Goose God", color="#000000")
define mG = Character("Jupyter Journal", color="#ad2a28")
define MsG = Character("[MsGName]", color="#f542cb")
define T = Character("Timmy Tam", color= "#35ad28")
define A = Character("Ana Conda", color = "#2f1fc2")


# dialogue starts here
label start:
    N "What's your name again? I didn't quite catch it the first time."

    python:
        MsGName=renpy.input("Help me out here, bud:", length=25)
        MsGName=MsGName.strip()
        if not MsGName:
            MsGName="CHE120"
    N "What a funny name for a goose, does your mom also call you that?"
    N "Alright, so your job here now is to ignore me and indulge in university life."
    N "You may have noticed that about $16,000 has disappeared from your bank account, but such is life when you're at uwaterloo :)."
    N "Welcome to campus little goosling, enjoy your stay. (Don't enjoy it too much though)"
    # background here, just add file name, no file format at end
    play music "audio/rockgardenmusic.mp3"
    scene rock garden 3
    show rock garden 3
    # show the character sprite, no file format at end eiother
    show angry mr goose with dissolve

    # dialogue starts here, from above defined character
    ## want about 875x875 pixel image for best results
    mG "ima smack the taste out of yo mouth if you don't stop with the amongus jokes"
    hide angry mr goose 
    show blushing mr goose right facing 
    mG "omg no way its the red imposter"
    mG "uwu i am a go-owo-se"
    mG "do you like pizza or nah"
    menu:
        "not really":
            hide blushing mr goose
            show angry mr goose
            mG "so bad, mate"
           
        "yes":
            "good."
        "option C":
            "heres option C"
   
    hide blushing mr goose 
    hide angry mr goose 
    show blushing mr goose right facing
    mG "poggers"
    hide blushing mr goose right facing with dissolve
    show blushing ms goose with dissolve
    MsG "this is me"
    hide blushing ms gooses with dissolve
    show ana wave with dissolve
    A "hi"
    hide ana wave with dissolve
    show timmy wave with dissolve
    T "hi"

   
    # game ends here, return to main screen
    return