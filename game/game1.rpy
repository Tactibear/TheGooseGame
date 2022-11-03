# ## WORK IN PROGRESS
# transform buttonformat:
#     zoom 0.7
#     rotate -90
# transform goosegodimage:
#     zoom 0.7

# init python:
#     import pygame
#     import random
#     userchoice=''
#     userscore=0
#     compscore=0
#     compchoice=random.randint(1,3)
#     if compchoice==1:
#         compchoice=='rock'
#     if compchoice==2:
#         compchoice=='paper'
#     if compchoice==3:
#         compchoice=='scissors'

# screen rockpaperscissors():
#     frame:
#         image "fightinggod.jpg"
#         hbox:
#             spacing 10
#             align(0.5,0.5)
#             text "Score [compscore]   [userscore]" size 40 xpos 0.1 ypos 0.1 
     
    
#     imagebutton auto "rockgoose_%s.png":
#         style buttonformat 
#         align(1.13, -1.1) 
#         action Function(rockplayed,userchoice)  
        
#     imagebutton auto "papergoose_%s.png":
#         style buttonformat
#         align(1.13, 0.5) 
#         action Function(paperplayed,userchoice) 
#     imagebutton auto "scissorsgoose_%s.png":
#         style buttomformat
#         align(1.13, 1.8) 
#         action Function(scissorsplayed,userchoice) 
#     imagebutton auto "goosegod_%s.png" align(-1.2, 0.4) action NullAction() at goosegodimage

# label rockpaperscissorslabel:
#     show screen rockpaperscissors
#     if userscore==7 or compscore==7:
#         jump tempstart    
# label compchoserock:

# label compchosepaper:
# label compchosescissors:
        
  
           

    

    


