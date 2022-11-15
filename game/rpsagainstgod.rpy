## CL2
define N = Character("Goose God", color="#000000")

label rpsagainstgod:
    show fightinggod
    show goosegod_hover 
    N 'So it seems that you want to challenge me of all geese.'
    N 'This will indeed be good practice for when you face Jupyter.'
    N 'Whoops did not mean to spoil.'
    N 'So now, little goosling, try and win against the almighty omnipotent being.'
    N 'Choose your hand.'
    ##let player choose an option, and set it to that
    menu:
        "Rock!":
            $userchoice='rock'
        "Paper!":
            $userchoice='paper'
        "Scissors!":
            $userchoice='scissors'
    ## now check for the option the player took, and force the computer to win every single time
    ## you fought god, what did you expect???
    if userchoice=='rock':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose paper.'
        N 'I win!'
        N 'Better luck next time haha.'
        ## now that we made fun of the user, go back to main script
        jump afterrpsgod
    if userchoice=='paper':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose scissors.'
        N 'I win!'
        N 'Better luck next time haha.'
        ## now that we made fun of the user, go back to main script
        jump afterrpsgod
    if userchoice=='scissors':
        N 'Well this is truly too bad.'
        N 'I probably live in your head rent free, cause I chose rock.'
        N 'I win!'
        N 'Better luck next time haha.'
        ## now that we made fun of the user, go back to main script
        jump afterrpsgod

   