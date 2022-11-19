##CL2 code
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
define N = Character("Goose God", color="#000000", callback=callback)
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)

init python:
    count=0
    counthistory=[0,1,2,3,4,5,6,7,8,9,10]
    track=1    

label counting_to_ten:
    mG "The goal of this game is to not be the one who says 10."
    mG "We take turns counting up to 3 consecutive numbers, in order."
label repeatcount:
    mG "Do you want to start at 1, or do you want me to start?"
    menu:
        "I'll start.":
            $countstate=0
        "You start.":
            $countstate=1
label startcounting:
    N "Game start"
label computercalc:
    if count>10 or count==10:
        jump userlostcounting
    if count<10:
        if countstate==1:
            $compcurrentcount=renpy.random.choice(["1","12","123"])
            $count+=len(compcurrentcount)
            jump printcompnum
    
label printcompnum:
    if track!=count:
        N "[track]"
        $track+=1
        if track==10:
            N "[count]"
            jump complostcounting
        jump printcompnum
    jump userchooses

label userchooses:
    if count>10 or count==10:
        jump complostcounting
    $userinput=renpy.input('Enter up to 3 numbers, unseparated',3)
    $count+=len(userinput)
    $track+=len(userinput)

    jump computercalc 
 

label complostcounting:
    N "You win"
    jump returnfromcounting
label userlostcounting:
    N "Haha I win"
    jump returnfromcounting
        

label returnfromcounting:
    N "Shall we play again?"
    menu:
        "Yes":
            $count=0
            $track=1
            jump repeatcount
            
        "No":
            jump placeholderreturnfromrps