################                  CL Function to create the game base of a working piano game                   ########################
transform zoom1:
    yalign 0.00000001
    xalign 0.05
    zoom 0.45

label ddrgamesetup2:
    $ renpy.block_rollback()
    show qnc piano at zoom1
    show keyboard:
        zoom 2.8
        xalign 0.5
        yalign 0.8
    with Dissolve(3)
    $ cont = 0 #continue variable
    $ arr_keys = ["a", "s", "k", "l"] #list of keyboard inputs to be selected from (https://www.pygame.org/docs/ref/key.html) keys
    $ noteremain = 30
    $ Livesleft1 = 3
    "Use the A,S,K,L keys to input"
    "Game Start"
    play music "<from 3.0>audio/MaryHadALittleLamb.mp3" volume 3
    call piano_setup2(0.5, 0.5, 0.005, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, 0.5)
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomize the location
    jump ddrgame2

label ddrgame2:
    $ renpy.block_rollback()
    while cont == 1:
        call piano_setup2(0.5, 0.5, 0.005, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, 0.5)
        # to repeat the qte events until it is missed
    jump pianoend2

## The label that will call the screen that the game is held in
label piano_setup2(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ renpy.block_rollback()
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen piano_game2

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

transform pianokey:
    zoom 0.8

## The Screen that contains the visuals for the game itself
screen piano_game2:
    text "Notes Remaining: [noteremain]":
            ypos 10
            xalign 0.95
            color "#fff"
            size 50
            outlines [ (6,"#000000",0,0) ]
    text "Lives: [Livesleft1]":
        ypos 10
        xalign 0.05
        color "#fff"
        size 50
        outlines [ (6,"#000000",0,0) ]

    ###disable the inputs:
    for i in arr_keys:
        python:
            if i == trigger_key:
                wrongtrigger = True
            else:
                wrongtrigger = False
        if wrongtrigger == True:
            key trigger_key action Jump('onkeypress2')
        else:
            key i action Jump('missedkey2')
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action Jump('onkeypress2')
    # the "key detector" (ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement
        $ trigger_key_dis= str.capitalize(trigger_key)
        imagebutton auto "images/Keyback1_%s.png" ypos 140 at pianokey action NullAction()
        text trigger_key_dis:
            ypos -10
            xalign 0.5
            color "#fff"
            size 45
            outlines [ (6,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 150
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%

label missedkey2:
    with vpunch
    if Livesleft1 >1:
        $ Livesleft1-=1
        $ cont = 1
        jump ddrgame2
    else:
        $ cont = 0
        jump ddrgame2

label onkeypress2:
    if noteremain>1:
        $ noteremain -=1
        $ cont = 1
    else:
        $ cont=2
    jump ddrgame2

label pianoend2:
    play music rch301musicpolybridge
    if cont == 2:
        $ shipfavour+=15
        N "ConGraTs On FinIsHiNg ThE SoNg"
        N "Sorry its hard to slap you with sarcasm when I'm an omnipotent, omnipresent goose delivering messages to you via telepathy..."
        N "At least you did finish it so it seems like Jupyter doesn't fully hate your song choice"
    else:
        $shipfavour-=5
        N "You deserve this" with hpunch
        $ renpy.run(OpenURL('https://www.youtube.com/watch?v=lO9K7VMFo2Y'))
        N "sorry but you did pick the easier song and still manage to fail it"
        N "I guess coordination is hard when you try to play the piano with wings.."
        N "Oh well at least you tried.... lets hope he had fun"
    jump returnfromddr