###############           Cl, CL2                ################
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
    ##define variables to start off at
    count=1
    ### was initially gonna check to make sure the user only inputted consecutive numbers but proved too hard
    ## was gonna check if they were next to each other in the list but code kept self destructing :(
    counthistory=[0,1,2,3,4,5,6,7,8,9,10]
    track=1    

label counting_to_ten:
    mG "The goal of this game is to not be the one who says 10."
    mG "We take turns counting up to 3 consecutive numbers, in order."
label repeatcount:
    mG "Do you want to start at 1, or do you want me to start?"
    ## see who starts, and go to appropriate label
    menu:
        "I'll start.":
            $countstate=0
        "You start.":
            $countstate=1
    
label startcounting:
    mG "Let's do this!"
label computercalc:
    ##check if number was hit, then user lost counting from at least second roundabout loop
    if count>11 or count==11:
        jump userlostcounting
    if count<11:
        ## let computer choose and assign the length
        if countstate==1:
            $compcurrentcount=renpy.random.choice(["1","12","123"])
            $count+=len(compcurrentcount)
            jump printcompnum
        elif track==1:
            jump userchooses
    
label printcompnum:
    ##print what the computer chose
    if track!=count:
        N "[track]"
        $track+=1
        ## if what comp chooses loses, go to comp lost label
        if track==11:
            N "[count]"
            jump complostcounting
        jump printcompnum
    ## now let user chooses
    jump userchooses

label userchooses:
    ## check for a comp L
    if count>11 or count==11:
        jump complostcounting
    ## let user input, restrict possible inputs 
    $userinput=renpy.input('Enter up to 3 numbers, unseparated',length=3, allow=['1','2','3','4','5','6','6','7','8','9','0'])
    ## if no input, let user just have 1 length
    if not userinput:
        $ userinput='1'
    
    $countstate=1
    ## add to the current count
    $count+=len(userinput)
    $track+=len(userinput)
    ## let computer count again
    jump computercalc 
 
##once game over, back to main script
label complostcounting:
    mG "You win"
    jump returnfromcounting
label userlostcounting:
    mG "Haha I win"
    jump returnfromcounting
        

label returnfromcounting:
    ## hashtag replayability
    mG "Shall we play again?"
    menu:
        "Yes!":
            ## dont forget to reset the variables
            $count=1
            $track=1
            jump repeatcount
            
        "Nah, let's go check the market out now!":
            ## sodge
            jump returnfromten