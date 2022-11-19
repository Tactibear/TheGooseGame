## CL using RPS as a basis for the DDR game
# init python:
#     ## define a function, callback, and allow for the acceptance of any number of inputs into the function
#     def callback(scrollingtextevent, **kwargs):
#         ## if a defined event is occuring, in this case, the text is scrolling past the user,
#         ## play the sound file that plays with scrolling text, a text "blip" sound
#         if scrollingtextevent == "show":
#             renpy.music.play("audio/textblipsoundeffect.mp3", channel="sound", loop=True)
#         ## the other two possible states of the dialogue content is when is done scrolling,
#         ## and sitting idle, where the sound stops playing
#         elif scrollingtextevent == "slow_done" or scrollingtextevent == "end":
#             renpy.music.stop(channel="sound")

# define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
# define MsG = Character("[MsGName]", color="#f542cb", callback=callback)

# define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]

# init python:
#     def rpsrolling(userchoice):
#         import random
#         compchoice=random.randint(1,3)
# transform buttonformat:
#     zoom 0.7
#     rotate -90
# transform jupyterimage:
#     zoom 0.7
# transform backgroundimage:
#     zoom 0.5

# screen rpstest():
#     frame:
#         image "e7 lobby 2.jpg" zoom 0.8
#         hbox:
#             spacing 10
#             align(0.5,0.5)
#             text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    

#     imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) at buttonformat action Jump('choserock')
#     imagebutton auto "papergoose_%s.png" align(1.13,0.5) at buttonformat action Jump('chosepaper')
#     imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) at buttonformat action Jump('chosescissors')
  
#     imagebutton auto "standard mr goose right facing_%s.png" align(0, 0.4) action NullAction() at jupyterimage

# label rpstest11:
#     if compscore+userscore==7:
#         hide screen rpstest
#         hide e7 lobby 2
#         jump placeholderreturnfromrps
#     scene e7 lobby 2 
#     show e7 lobby 2 at backgroundimage
#     mG "Go ahead, choose an option."
#     call screen rpstest

# label choserock:
#     scene e7 lobby 2
#     show e7 lobby 2 
#     $userchoice='rock'
#     mG "so you chose rock"

#     jump rpsresult

# label chosepaper:
#     scene e7 lobby 2
#     show e7 lobby 2
#     $userchoice='paper'
#     mG "so you chose paper"
#     jump rpsresult
    
# label chosescissors:
#     scene e7 lobby 2
#     show e7 lobby 2
#     $userchoice='scissors'
#     mG "so you chose scissors"
#     jump rpsresult

# label rpsresult:
#     scene e7 lobby 2 at backgroundimage
#     show e7 lobby 2
#     $compchoice=renpy.random.choice(['rock', 'paper', 'scissors'])
#     if (userchoice, compchoice) in rpslibrary:
#         mG "I chose [compchoice]"
#         mG 'L, I win'
#         $compscore+=1
#         jump rpstest11

#     elif (compchoice, userchoice) in rpslibrary:
#         mG "I chose [compchoice]"
#         mG 'Got lucky, you win'
#         $userscore+=1
#         jump rpstest11
#     else:
#         mG "I chose [compchoice]"
#         mG 'tie, go again'
#         jump rpstest11

##CL Function to create the game base

label ddrgame:

    $ cont = 0 #continue variable
    $ arr_keys = ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"] #list of keyboard inputs to be selected from (https://www.pygame.org/docs/ref/key.html) keys

    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, 0.5)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        # to repeat the qte events until it is missed

    "{b}GAME OVER{/b}"

    return
#########################################
#FUNCTION
#########################################
label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

############################################
#SCREEN
############################################
screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Return(1) )
    # the "key detector" (ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            #outlines [ (2,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%
