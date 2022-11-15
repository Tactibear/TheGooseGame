# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME


# main game ipt


# give character a name and define to a variable

define N = Character("Goose God", color="#000000")
define mG = Character("Jupyter Journal", color="#ad2a28")
define MsG = Character("[MsGName]", color="#f542cb")
define T = Character("Timmy Tam", color= "#35ad28")
define A = Character("Ana Conda", color = "#2f1fc2")


# dialogue starts here
label start:
    N "What's your name again? I didn't quite catch it the first time."

    python:
        MsGName=renpy.input("Help me out here, bud:", length=25)
        MsGName=MsGName.strip()
        if not MsGName:
            MsGName="CHE120"
    N "What a funny name for a goose, does your mom also call you that?"
    N "Alright, so your job here now is to ignore me and indulge in university life."
    N "You may have noticed that about $16,000 has disappeared from your bank account, but such is life when you're at uwaterloo :)."
    N "Welcome to campus little goosling, enjoy your stay. (Don't enjoy it too much though)"
    # background here, just add file name, no file format at end
    play music "audio/rockgardenmusic.mp3"
    scene rock garden 3
    show rock garden 3 with dissolve
    N "It's a beautiful Sunday afternoon. you and your friend, Ana Conda, are at the University of Waterloo's Rock Garden"
    N "It is currently 3pm, and you just got a text from your childhood friend, Timmy Tam, asking if you wanted to hang out with him and his friend, Jupyter Journal in MC."
    MsG "Thinking: I can't wait to see Timmy again! It's been so long since I last saw him."
    hide rock garden 3 with dissolve
    show mc trelfords office 2 with dissolve
    N "You and Ana walk into MC and take the elevator to the 6th floor, where Timmy and his friend are studying."
    MsG "I hope you don't mind that I brought my friend Ana!"
    show timmy with dissolve
    T "Oh my gosh, MsG! I haven't seen you in so long! How have you been?"
    MsG "I've been doing great! I missed you so much Timmy!"
    T "Me too! This is my friend Jupyter by the way, he's in CS BBA, what a silly CS boy."
    hide timmy with dissolve
    show standard mr goose with dissolve
    MsG "thinking: Omg Omg Jupyter is such a dapper goose!!! He is soooo cute"
    MsG "Hi Jupyter! I'm (MsG) nice to meet you! I'm in Chem Eng :)"
    mG "Nice to meet you! How were your first week of classes?"
    MsG "Tt has been going well :). My favorite class so far has been Computer Literacy and Programming! I love coding and I am so amped to be learning Python"
    mG "that's great to hear! I code in G++, but I love Python way more!"
    hide standard mr goose with dissolve
    N "You and Jupyter talk more about your hobbies. You discover that you both enjoy swimming, playing GO FISH with your fellow goose comrades, and finding new plant-based recipes"
    N "The group continues to study and get to know each other. After a few hours of hard work on that Waterloo grind set, you all exchange information and plan to meet up the next day for more studying (and possibly more)."
    MsG "Thinking: Omg, sould I check Wingstagram to see if Jupyter has a girlfriend?"
    menu:
        "Yes, stalk Jupyter's Wingstagram and see if he has a girlfriend":
            N "you open Wingstagram"
            MsG "Thinking: He has no tagged posts of him with any girls, or any photos with any girls... I think he's single!"
            N "You have learned that Jupyter is single, even though stalking his Wingstagram might be a little creepy... But is it really that creepy?"
            N "plus 5 relationship points"
        "No, just suffer in ambiguity about Jupyter's relationship status":
            MsG "Thinking: Damn, I don't really know if I should look at Jupyter's Wingstagram, is that a little creepy?"
            N "You decided not to check Jupyter's Wingstagram to see his relationship status. There is no change to your relationship points"

Label Day3
    N "Two weeks later..."
    N "You just finished a Chem Egg Student Society (CESS) meeting when you receive a text from Jupyter asking to hang out in the QNC basement."
    menu:
        "Option 1: Go to QNC and meet Jupyter for some fun times (+10 relationship points)"
            N "You decide to go to the QNC basement to hang out with Jupyter and hopefully get some 'studying' done while you're there."
            scene qnc basement
            show qnc basement with dissolve
            show standard mr goose with dissolve
            mG "Hey (MsG)!! What's up!"
            MsG "Hiiiiiii, I just finished a CESS meeting but I wanted to see you :))"
            hide standard mr goose with dissolve
            show blushing mr goose with dissolve
            mG "Ayo okay bro chill chill, I just wanted to show you my awesome piano skills on this piano."
            MsG "You play piano?! That's so slay, so do I! When did you start playing?"
            hide blushing mr goose with dissolve
            show standard mr goose with dissolve
            mG "Ever since I was a wee little gosling, I played piano in the Ryan Piano School for Goslings"
            MsG "Yoooo that's so cool! Let's play something together :))))"
            hide standard mr goose with dissolve
            N "Pick a song to play!"
            menu:
                "Option 1: Hungarian Dance No 2. by Franz Liszt (+15 relationship points just for the synergy)"
                "Option 2: Mary Had a Little Lamb (-15 relationship points, DO BETTER!!!)"
                #transition to minigame
                ## if game is won grant an additional 15 relationship points
                ## if game is lost no change is relationship points
            #regardless of win/loss/choice in song
            N "You and Jupyter jam along happily on the QNC piano, possibly disturbing every other goose in the vicinity."
            MsG "I think we make a pretty good duet! You play super well by the way"
            show blushing mr goose with dissolve
            mG "Aw thanks (MsG), you're not so bad yourself!"
            MsG "Thanks Jupyter !! Let's continue to jam on the piano"
            N "You and Jupyter continue to jam out on the QNC piano, possibly sending every other goose in the room into the 4th dimension with how “beautiful” your playing was. An hour or two passes by, and before you both knew it, it was time for Jupyter to leave to his ECON 120 lecture."
            hide blushing mr goose with dissolve
            show standard mr goose with dissolve
            mG "Bye (MsG)!! I had fun today!!"
            MsG "Bye Jupyter!! I did too, have fun in econ!"
            mG "Thanks! Have a great day too!!"
            menu:
                "Option 1: Lean in for a hug (+5 relationship points)"
                    N "You lean in for a hug. You can feel Jupyter stiffen and offer you an awkward hug back."
                "Option 2: Wave goodbye (No change to relationship points)"
                    N "You wave goodbye at Jupyter and he waves back and smiles"
            N "You feel your heart beat a little faster than before. Maybe someone is beginning to feel like they're in love?"
        "Option 2: Say no and go to the WEEF office to ask questions about the CHE 100 assignment (-20 relationship points)"
            N "You leave Jupyter on read and decide to head to WEEF to ask the WEEF TAs about your CHE 100 assignment. Boohoo, nerd."
        #end of day 3
label day5
    scene toronto
    show toronto with dissolve
    N "After 1A..."
    N "It's been a crazy first term at the University of Waterloo and you can't believe that it's only been that long since you've met Jupyter! After a long day of classes, you get a text from him asking if you want to explore downtown Toronto with the group. Of course, you accept and you all explore the downtown area."
    N "After a long ride on the GO Train, you go into the AGO to see all the wonderful art it has to offer. Then, you waddle around the sketchy streets of Toronto before ending up in the Christmas Market."
    show standard mr goose with dissolve
    mG "Hey (MsG)! How were your final exams?"
    MsG "Jupyter!!!! I think they went well! All of our studying really paid off and I am confident I passed them all. Is everyone excited to be in the Christmas Market? Although I don’t love the cold, Christmas is my favourite holiday!"
    hide standard mr goose with dissolve
    show ana with dissolve
    A "Frankly, I am super happy to be done exams! Chem was really hard!"
    hide ana with dissolve
    show timmy with dissolve
    T "I personally wish I was down in Florida right now! This cold weather really sucks!"
    hide timmy with dissolve
    show standard mr goose with dissolve
    mG "I love Christmas too! It's the best season to show the people you care about what they mean to you. I know there is someone whom I want to give extra thanks to."
    MsG "Lets go explore the Market!!!!"
    N "You, Ana, Timmy and Jupyter waddle around the Christmas Market and explore all the beauty it has in store for you. The Christmas lights shine bright in the night sky and you all approach the gorgeous massive Christmas tree in the middle of the square."
    hide standard mr goose with dissolve
    hide toronto with dissolve
    show christmas market with dissolve
### these names could change not sure what the images will be called if they arent already in the folder
    MsG "This has got to be the BIGGEST Christmas tree I've ever seen! Like how do they even get this thing in here?"
    show timmy with dissolve
    T "I don't know but it's pretty epic!"
    hide timmy with dissolve
    show ana with dissolve
    A "Hey Tim-Tim, do you want to come get some Hot Cocoa with me? I think there Is a booth down this way"
    hide ana with dissolve
    show timmy with dissolve
    T "For sure! I am so cold I feel like I will turn into a Goose-sicle"
    hide timmy with dissolve
    N "Ana and Timmy go off and somehow you and and Jupyter have ended up alone. The mood in the square has given you a warm feeling of happiness and romance. Jupyter gets a little closer and seems to have an anxious look about him"
    MsG "Jupyter is everything ok? You look like you're gonna throw up lmao"
    show blushing mr goose
    mG "Huh? Oh yea. Sorry I was just thinking about something. (MsG) there has been something I’ve been wanting to tell you for the longest time."
    MsG "What's up? You can tell me anything."
    mG "I have had so much fun getting to know you over this past term. You have helped me with so many things and made me the goose I am today. This first term has been so stressful and hectic and I don’t think I would have survived it without you by my side. I guess what I am trying to say is..."
    mG "I like you (MsG). So yea. That's all."

# show the character sprite, no file format at end eiother
    ## want about 875x875 pixel image for best results
    # game ends here, return to main screen
return