## CL2
define N = Character("Goose God", color="#000000")

# define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]
# screen rpstest():
#     frame:
#         image "fightinggod.jpg" zoom 0.8

#     imagebutton auto "goosegod_%s.png" align(-1.2, 0.4) action NullAction() at goosegodimage
##CL just fixing some code
transform goosegood:
    zoom 0.5
    xpos 400
    ypos 100

label rpsagainstgod:
    show fightinggod
    show goosegod_idle at goosegood
    N 'So it seems that you want to challenge me of all geese.'
    N 'This will indeed be good practice for when you face Jupyter.'
    N 'Whoops did not mean to spoil.'
    N 'So now, little goosling, try and win against the almighty omnipotent being.'
    N 'Choose your hand.'
    menu:
        "Rock!":
            $userchoice='rock'
        "Paper!":
            $userchoice='paper'
        "Scissors!":
            $userchoice='scissors'
    if userchoice=='rock':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose paper.'
        N 'I win!'
        N 'Better luck next time haha.'
        jump afterrpsgod
    if userchoice=='paper':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose scissors.'
        N 'I win!'
        N 'Better luck next time haha.'
        jump afterrpsgod
    if userchoice=='scissors':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose rock.'
        N 'I win!'
        N 'Better luck next time haha.'
        jump afterrpsgod

   