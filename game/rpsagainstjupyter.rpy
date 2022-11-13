## CL2
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

define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]

init python:
    def rpsrolling(userchoice):
        import random
        compchoice=random.randint(1,3)
transform buttonformat:
    zoom 0.7
    rotate -90
transform jupyterimage:
    zoom 0.7
transform backgroundimage:
    zoom 0.5

screen rpstest():
    frame:
        image "e7 lobby 2.jpg" zoom 0.8
        hbox:
            spacing 10
            align(0.5,0.5)
            text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    

    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) at buttonformat action [SetVariable('userchoice','rock'),Function(rpsrolling,userchoice), Jump('choserock')]
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) at buttonformat action [SetVariable('userchoice','paper'),Function(rpsrolling,userchoice), Jump('chosepaper')]
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) at buttonformat action [SetVariable('userchoice','scissors'),Function(rpsrolling,userchoice), Jump('chosescissors')]
  
    imagebutton auto "standard mr goose right facing_%s.png" align(0, 0.4) action NullAction() at jupyterimage

label rpstest11:
    call screen rpstest
    show standard mr goose right facing 
    mG "Go ahead, choose an option."
label choserock:
    scene e7 lobby 2
    show e7 lobby 2 
    $userchoice='rock'
    mG "so you chose rock"

    jump rpsresult

label chosepaper:
    scene e7 lobby 2
    show e7 lobby 2
    $userchoice='paper'
    mG "so you chose paper"
    jump rpsresult
    
label chosescissors:
    scene e7 lobby 2
    show e7 lobby 2
    $userchoice='scissors'
    mG "so you chose scissors"
    jump rpsresult

label rpsresult:
    scene e7 lobby 2 at backgroundimage
    show e7 lobby 2
    $compchoice=renpy.random.choice(['rock', 'paper', 'scissors'])
    if (userchoice, compchoice) in rpslibrary:
        mG "I chose [compchoice]"
        mG 'L, I win'
        $compscore+=1
        jump rpstest11

    elif (compchoice, userchoice) in rpslibrary:
        mG "I chose [compchoice]"
        mG 'Got lucky, you win'
        $userscore+=1
        jump rpstest11
    else:
        mG "I chose [compchoice]"
        mG 'tie, go again'
        jump rpstest11
