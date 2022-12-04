###############           CL2                ################
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

define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)

## define a library for Scenarios of Computed Possibility (tm) (SCP-4633)
define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]

init python:
    ## function for assigning a random choice 
    def rpsrolling(userchoice):
        import random
        compchoice=random.randint(1,3)
    ## set at the very start, init python is called with a higher priority than renpy functions, and called before the code even executes, and only once
    compscore = 0
    userscore = 0
## a little **style** on the buttons and images eh
transform buttonformat:
    zoom 0.7
    rotate -90
transform jupyterimage:
    zoom 0.7
transform backgroundimage:
    zoom 0.5

screen rpstest():
    ## displayables for the background 
    frame:
        image "campuspizza.jpg" 
        hbox:
            spacing 10
            align(0.5,0.88)
            text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    ##displayed option buttons for the goose rps, align to an absolute position, and jump to appropriate label afterwards
    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) focus_mask True at buttonformat action Jump('choserock')
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) focus_mask True at buttonformat action Jump('chosepaper')
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) focus_mask True at buttonformat action Jump('chosescissors')
    ## lazy, so just made the jupyter another button, that just honks at you when you click him
    imagebutton auto "standard mr goose right facing_%s.png" align(0, 0.99999) action Play(config.has_sound,"audio/honk.mp3",selected=None) at jupyterimage

label rpstest11:
    play music pizza ### pizza time
    
label rpstest11start:
    ## if best of 7 is achieved, get outta here and back to romancing the geese
    if compscore+userscore==7:
        hide screen rpstest
        hide rockicon
        hide papericon
        hide scissorsicon
        hide rockicon2
        hide papericon2
        hide scissorsicon2

        hide campuspizza
        jump returnfromrps
    ## otherwise jupyter prompts 
    mG "Go ahead, choose an option."
    ##refresh screen
    call screen rpstest

##scenarios for user clicking a button
label choserock:
    scene campuspizza
    show campuspizza 
    $userchoice='rock'
    show rockicon at right with moveinright 
    mG "so you chose rock"

    jump rpsresult

label chosepaper:
    scene campuspizza
    show campuspizza
    $userchoice='paper'
    show papericon at right with moveinright 
    mG "so you chose paper"
    jump rpsresult
    
label chosescissors:
    scene campuspizza
    show campuspizza
    $userchoice='scissors'
    show scissorsicon at right with moveinright 
    mG "so you chose scissors"
    jump rpsresult

label rpsresult:
    ## comp chooses a random option from a set amount of options
    $compchoice=renpy.random.choice(['rock', 'paper', 'scissors'])
    ## check to see if the user and comp string, in a tuple is within the scenario library
    ## if it is, in given order, play correct animation and its a computer win for sure
    if (userchoice, compchoice) in rpslibrary:
        if compchoice=='rock':
            show rockicon2 at right with moveinleft 
            hide scissorsicon with dissolve
            play sound "rockthud.mp3" volume 50
        if compchoice=='paper':
            show papericon2 at right with moveinleft 
            hide rockicon with dissolve
            play sound "paper.mp3" volume 50
        if compchoice=='scissors':
            show scissorsicon2 at right with moveinleft 
            hide papericon with dissolve
            play sound "scissors.mp3" volume 50
        mG "I chose [compchoice]"
        mG 'L, I win'
        $compscore+=1
        jump rpstest11start
    ## and for the opposite scenario as well
    elif (compchoice, userchoice) in rpslibrary:
        if compchoice=='rock':
            show rockicon2
            show papericon at left with moveinright
            hide rockicon2 with dissolve
            play sound "paper.mp3" volume 50
        if compchoice=='paper':
            show papericon2 
            show scissorsicon at left with moveinright 
            hide papericon2 with dissolve
            play sound "scissors.mp3" volume 50
        if compchoice=='scissors':
            show scissorsicon2
            show rockicon at left with moveinright
            hide scissorsicon2 with dissolve
            play sound "rockthud.mp3" volume 50
        mG "I chose [compchoice]"
        mG 'Got lucky, you win'
        $userscore+=1
        
        jump rpstest11start
    ## besides that, its a tie and we give no one score
    else:
        if compchoice=='rock':
            show rockicon2 at left with moveinleft 
        if compchoice=='paper':
            show papericon2 at left with moveinleft 
        if compchoice=='scissors':
            show scissorsicon2 at left with moveinleft 
        mG "I chose [compchoice]"
        mG 'tie, go again'
        jump rpstest11start
