# ## WORK IN PROGRESS
# transform buttonformat:
#     zoom 0.7
#     rotate -90
# transform goosegodimage:
#     zoom 0.7

# init python:
#     import pygame
#     import random
#     userchoice=0
#     user=""
#     userscore=0
#     compscore=0
#     def roundplayed(user):
#         compchoice=random.randint(1,3)
#         if compchoice==1:
#             compchoice=='rock'
#         if compchoice==2:
#             compchoice=='paper'
#         if compchoice==3:
#             compchoice=='scissors'
#         #
#         if compchoice=='scissors' and user=='scissors' or compchoice=='rock' and user=='rock' or compchoice=='paper' and user=='paper':
#             pass
#         if compchoice=='scissors' and user=='paper' or compchoice=='rock' and user=='scissors' or compchoice=='paper' and user=='rock':
#             compscore+=1
#             return computerscore
#         if compchoice=='scissors' and user=='rock' or compchoice=='rock' and user=='paper' or compchoice=='paper' and user=='scissors':
#             userscore+=1
#             return userscore

# screen rockpaperscissors():
#     frame:
#         image "fightinggod.jpg"
#         hbox:
#             spacing 10
#             align(0.5,0.5)
#             text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
     
    
#     imagebutton auto "rockgoose_%s.png" align(1.13, -1.1) action SetVariable[("userchoice",userchoice+1),Function(roundplayed(userchoice))] at buttonformat 
#     imagebutton auto "papergoose_%s.png" align(1.13, 0.5) action [SetVariable("user",'paper'),Function(roundplayed(user))] at buttonformat
#     imagebutton auto "scissorsgoose_%s.png" align(1.13, 1.8) action [SetVariable(user,'scissors'),Function(roundplayed(user))] at buttonformat
#     imagebutton auto "goosegod_%s.png" align(-1.2, 0.4) action NullAction() at goosegodimage

# label rockpaperscissorslabel:
#     call screen rockpaperscissors
    
           

    

    


