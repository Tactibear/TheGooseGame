## janked code, python based
init python:
    def rpsrolling(userchoice):
        import random
        compchoice=random.randint(1,3)
transform buttonformat:
    zoom 0.7
    rotate -90
transform goosegodimage:
    zoom 0.7

screen rpstest():
    frame:
        image "fightinggod.jpg" zoom 0.8
        hbox:
            spacing 10
            align(0.5,0.5)
            text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
    

    imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) at buttonformat action [SetVariable('userchoice',1),Function(rpsrolling,userchoice)]
    imagebutton auto "papergoose_%s.png" align(1.13,0.5) at buttonformat action [SetVariable('userchoice',2),Function(rpsrolling,userchoice)]
    imagebutton auto "scissorsgoose_%s.png" align(1.13,1.8) at buttonformat action [SetVariable('userchoice',3),Function(rpsrolling,userchoice)]
  
    imagebutton auto "goosegod_%s.png" align(-1.2, 0.4) action NullAction() at goosegodimage
#####################
## working code, besides a few misplaced vars, renpy based
define N = Character("Goose God", color="#000000")

define rpslibrary=[('rock','paper'), ('paper','scissors'), ('scissors','rock')]
label rps1final:
    #call screen rpstest

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
            $ rps_player='scissors'
            
    $compchoice=renpy.random.choice(['rock', 'paper', 'scissors'])
    if (rps_player, rps_npc) in rps_beats:
        N 'L, I win'
    elif (rps_npc, rps_player) in rps_beats:
        N 'Got lucky, you win'
    else:
        N 'tie, go again'
        jump rps
