###############           CL2                ################
define N = Character("Goose God", color="#000000")

##CL just fixing some code
## CL2 :(((((
transform goosegood:
    zoom 0.5
    xpos 400
    ypos 100

label rpsagainstgod:
    play music "audio/rpsmusic Battle Ready By AudioMachine.mp3"
    show fightinggod
    show goosegod_idle at goosegood
    N 'So it seems that you want to challenge me of all geese.'
    N 'This will indeed be good practice for when you face Jupyter.'
    N 'Whoops did not mean to spoil.'
    N 'So now, little goosling, try and win against the almighty omnipotent being.'
    N 'Choose your hand.'
    ## make the computer always win, cause its god
    ## mwahahahahahaha
    menu:
        "Rock!":
            $userchoice='rock'
        "Paper!":
            $userchoice='paper'
        "Scissors!":
            $userchoice='scissors'
    if userchoice=='rock':
        N 'Well this is truly too bad.' with vpunch
        N 'I probably live in your head rent free, cause I chose paper.' with vpunch
        N 'I win!' with vpunch
        N 'Better luck next time haha.'
        jump afterrpsgod
    if userchoice=='paper':
        N 'Well this is truly too bad.' with vpunch
        N 'I probably live in your head rent free, cause I chose scissors.' with vpunch
        N 'I win!' with vpunch
        N 'Better luck next time haha.'
        jump afterrpsgod
    if userchoice=='scissors':
        N 'Well this is truly too bad.' with vpunch
        N 'I probably live in your head rent free, cause I chose rock.' with vpunch
        N 'I win!' with vpunch
        N 'Better luck next time haha.'
        jump afterrpsgod

   