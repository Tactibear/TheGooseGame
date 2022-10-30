# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over


# main game script

## CL2
## start python script to be recognized
init python:
    ## define a function, callback, and allow for the acceptance of any number of inputs into the function
    def callback(scrollingtextevent, **kwargs):
        ## if a defined event is occuring, in this case, the text is scrolling past the user,
        ## play the sound file that plays with scrolling text, a text "blip" sound
        if scrollingtextevent == "show":
            renpy.music.play("audio/textblipsoundeffect.mp3", channel="sound", loop=True)
        ## the other two possible states of the dialogue content is when is done scrolling,
        ## and sitting idle, where the sound stops playing
        elif scrollingtextevent == "slow_done" or scrollingtextevent == "end":
            renpy.music.stop(channel="sound")

## give character a name to be displayed and define to a variable, then assign them a colour, 
## and, when they are speaking dialogue, activate the text blip sound function
define N = Character("Goose God", color="#000000", callback=callback)
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)
define T = Character("Timmy Tam", color= "#35ad28", callback=callback)
define A = Character("Ana Conda", color = "#2f1fc2", callback=callback)

## define and set a default value for the relationship score the player starts with
default shipfavour=25


## dialogue content starts here
label start:
    scene e6 window 2 goose god
    show e6 window 2 goose god with dissolve
    

    ## CL2
    N "Welcome to the University of Waterloo!"
    N "This is your first of many mistakes you'll make here, but it's ok."
    N "Mistakes are what makes us geese."
    N "Sorry what's your name again? I didn't quite catch it the first time."
    ## initiate python once again
    python:
        ##as for an input, and limit the input to 25 characters
        ## set that name to the users name for the rest of the game
        MsGName=renpy.input("Help me out here, bud:", length=25)
        ##if there are any spaces in front or behind the given name, take those away
        ##this saves on dialogue box space if someone decides to troll 
        MsGName=MsGName.strip()
        #capitalize every word of the string
        MsGName=str.title(MsGName)
        ##if no name is inputted at all, set default to "CHE120"
        if not MsGName:
            MsGName="CHE120"
    ## CL2, EM
    N "'[MsGName]'..... I see....."
    N "What a funny name for a goose, does your mom also call you that?"
    N "Alright, so your job here now is to ignore me and indulge in university life."
    N "You may have noticed that about $16,000 has disappeared from your bank account, but such is life when you're at uwaterloo :)."
    N "Welcome to campus little goosling, enjoy your stay. (Don't enjoy it too much though)"
    ## CL
    ##transition insertion before beginning the dialogue 
    with dissolve
    hide e6 window 2 good god
    with dissolve
    show screen Opening1() with dissolve
    with dissolve
    show screen day1() with dissolve
    ## wait before continuing with code (seconds)
    pause 3
    hide screen day1 with dissolve
    ## CL2, EM
    # background here, just add file name, no file format at end
    hide screen Opening1 with dissolve
    play music "audio/rockgardenmusic.mp3"
    scene rock garden 3
    show rock garden 3 with dissolve
    show screen bars
    N "It's a beautiful Sunday afternoon. You and your friend, Ana Conda, are at the University of Waterloo's Rock Garden"
    N "It is currently 3pm, and you just got a text from your childhood friend, Timmy Tam, asking if you wanted to hang out with him and his friend, Jupyter Journal in MC."
    MsG "Thinking: I can't wait to see Timmy again! It's been so long since I last saw him."
    hide rock garden 3 with dissolve
    show mc trelfords office 2 with dissolve
    N "You and Ana walk into MC and take the elevator to the 6th floor, where Timmy and his friend are studying."
    MsG "I hope you don't mind that I brought my friend Ana!"
    show timmy with dissolve
    T "Oh my gosh, [MsGName]! I haven't seen you in so long! How have you been?"
    MsG "I've been doing great! I missed you so much Timmy!"
    T "Me too! This is my friend Jupyter by the way, he's in CS BBA, what a silly CS boy."
    hide timmy with dissolve
    show standard mr goose with dissolve
    MsG "thinking: Omg Omg Jupyter is such a dapper goose!!! He is soooo cute"
    MsG "Hi Jupyter! I'm [MsGName] nice to meet you! I'm in Chem Eng :)"
    mG "Nice to meet you! How were your first week of classes?"
    MsG "Tt has been going well :). My favorite class so far has been Computer Literacy and Programming! I love coding and I am so amped to be learning Python"
    mG "that's great to hear! I code in G++, but I love Python way more!"
    hide standard mr goose with dissolve
    N "You and Jupyter talk more about your hobbies. You discover that you both enjoy swimming, playing GO FISH with your fellow goose comrades, and finding new plant-based recipes"
    N "The group continues to study and get to know each other. After a few hours of hard work on that Waterloo grind set, you all exchange information and plan to meet up the next day for more studying (and possibly more)."
    MsG "Thinking: Omg, sould I check Wingstagram to see if Jupyter has a girlfriend?"
    ## CL2, EM
    ## menu defines a set of clickable choices for the suer
    ## under each "if" circumstance, is a set of actions that happens upon selecting that option
    ## afterwards, the if statement breaks, continuing on with the next code
    menu:
        "Yes, stalk Jupyter's Wingstagram and see if he has a girlfriend":
            N "you open Wingstagram"
            MsG "Thinking: He has no tagged posts of him with any girls, or any photos with any girls... I think he's single!"
            N "You have learned that Jupyter is single, even though stalking his Wingstagram might be a little creepy... But is it really that creepy?"
            N "plus 5 relationship points"
        "No, just suffer in ambiguity about Jupyter's relationship status":
            MsG "Thinking: Damn, I don't really know if I should look at Jupyter's Wingstagram, is that a little creepy?"
            N "You decided not to check Jupyter's Wingstagram to see his relationship status. There is no change to your relationship points"
    
    # show the character sprite, no file format at end eiother
    ## want about 875x875 pixel image for best results
    # game ends here, return to main screen
    return