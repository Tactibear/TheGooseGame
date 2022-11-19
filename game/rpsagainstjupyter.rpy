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

<<<<<<< HEAD
## no need to redefine, since renpy reads across files, but I get confused so :(
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)

## create a list, that defines the possible winning/losing outcomes of a rock paper scissors game
define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]

## find a random integer between 1 and 3 and assign it to a variable.
=======
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)

define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]


>>>>>>> 37d109f (DDR game code with other working files)
init python:
    def rpsrolling(userchoice):
        import random
        compchoice=random.randint(1,3)
<<<<<<< HEAD

## stylings to be assigned to certain images
=======
>>>>>>> 37d109f (DDR game code with other working files)
transform buttonformat:
    zoom 0.7
    rotate -90
transform jupyterimage:
    zoom 0.7
transform backgroundimage:
    zoom 0.5

<<<<<<< HEAD
## screen to be called, later on
screen rpstest():
    frame:
        ## background image set
        image "e7 lobby 2.jpg" zoom 0.8
        ## contain the score of the rps game, within a container, and display as variables
=======
screen rpstest():
    frame:
        image "e7 lobby 2.jpg" zoom 0.8
>>>>>>> 37d109f (DDR game code with other working files)
        hbox:
            spacing 10
            align(0.5,0.5)
            text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    
<<<<<<< HEAD
    ##display the buttons that let the player choose an option. If they do click it, set the userchoice variable, to the corresponding string, then jump to the correct label
    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) at buttonformat action [SetVariable('userchoice','rock'),Function(rpsrolling,userchoice), Jump('choserock')]
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) at buttonformat action [SetVariable('userchoice','paper'),Function(rpsrolling,userchoice), Jump('chosepaper')]
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) at buttonformat action [SetVariable('userchoice','scissors'),Function(rpsrolling,userchoice), Jump('chosescissors')]
  
    imagebutton auto "standard mr goose right facing_%s.png" align(0, 0.4) action NullAction() at jupyterimage

## main label that we start in, if the score, (best of 7) hits 7 in total, we just go right back to the main script 
## otherwise, we continue the game
=======
    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) focus_mask True at buttonformat action Jump('choserock')
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) focus_mask True at buttonformat action Jump('chosepaper')
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) focus_mask True at buttonformat action Jump('chosescissors')
  
    imagebutton auto "standard mr goose right facing_%s.png" align(0, 0.4) action NullAction() at jupyterimage

>>>>>>> 37d109f (DDR game code with other working files)
label rpstest11:
    if compscore+userscore==7:
        hide screen rpstest
        hide e7 lobby 2
        jump placeholderreturnfromrps
    scene e7 lobby 2 
    show e7 lobby 2 at backgroundimage
    mG "Go ahead, choose an option."
<<<<<<< HEAD
    ## we now show the buttons to the user
    call screen rpstest

## we set the userchoice to the variable in the label, and let Jupyter say something witty
=======
    call screen rpstest

>>>>>>> 37d109f (DDR game code with other working files)
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

<<<<<<< HEAD
## this determines the result of the rps 
label rpsresult:
    scene e7 lobby 2 at backgroundimage
    show e7 lobby 2
    ##let the computer pick a random string as well, as their play
    $compchoice=renpy.random.choice(['rock', 'paper', 'scissors'])
    ##now check if this specific pairing and order is in the losing library, if it is, then the computer won
    if (userchoice, compchoice) in rpslibrary:
        mG "I chose [compchoice]"
        mG 'L, I win'
        ## add a point to compscore
        $compscore+=1
        jump rpstest11
    ## if it isn't found in the losing library, player won
    elif (compchoice, userchoice) in rpslibrary:
        mG "I chose [compchoice]"
        mG 'Got lucky, you win'
        ## add one to userscore
        $userscore+=1
        jump rpstest11
    ##otherwise, it was a tie for sure
    else:
        mG "I chose [compchoice]"
        mG 'tie, go again'
        ##regardless we go back to the game initiation once again, to play more as long as the sum of the scores isn't 7
=======
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
>>>>>>> 37d109f (DDR game code with other working files)
        jump rpstest11
