# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME


# main game script


# give character a name and define to a variable
init python:
    def callback(scrollingtextevent, **kwargs):
        if scrollingtextevent == "show":
            renpy.music.play("audio/textblipsoundeffect.mp3", channel="sound", loop=True)
        elif scrollingtextevent == "slow_done" or scrollingtextevent == "end":
            renpy.music.stop(channel="sound")

define N = Character("Goose God", color="#000000", callback=callback)
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)
define T = Character("Timmy Tam", color= "#35ad28", callback=callback)
define A = Character("Ana Conda", color = "#2f1fc2", callback=callback)

default shipfavour=25


# dialogue starts here
label start:
<<<<<<< HEAD
    N "What's your name again? I didn't quite catch it the first time."

=======
    with dissolve
    show screen Opening1() with dissolve
    with dissolve
    show screen day1() with dissolve
    pause 3
    hide screen day1 with dissolve
    N "What's your name again? I didn't quite catch it the first time."
>>>>>>> cca2120 (updated transitiojns)
    python:
        MsGName=renpy.input("Help me out here, bud:", length=25)
        MsGName=MsGName.strip()
        if not MsGName:
            MsGName="CHE120"
    N "What a funny name for a goose, does your mom also call you that?"
    N "Alright, so your job here now is to ignore me and indulge in university life."
    N "You may have noticed that about $16,000 has disappeared from your bank account, but such is life when you're at uwaterloo :)."
    N "Welcome to campus little goosling, enjoy your stay. (Don't enjoy it too much though)"
<<<<<<< HEAD
=======
    hide screen Opening1 with dissolve
>>>>>>> cca2120 (updated transitiojns)
    # background here, just add file name, no file format at end
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