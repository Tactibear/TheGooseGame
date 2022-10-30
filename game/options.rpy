# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME

## CL2
## Name the game on title screen
## none is needed, since we have our own custom text
define config.name = _("")

## allow to show title on title screen
define gui.show_name = True

## subtitle on title screen
## empty as well, not needed
define config.version = ""
## both title and subtitle are awkwardly placed and we don't want to work with it

## About menu text
## in a paragraph, write contents when called in about screen
define gui.about = _p("""Regretted by Camillo, Charles, Emily, and Stephanie
""")

## file name, pls dont change
define build.name = "GooseVisualNovel"

## Gives the user ability to use sound mixer, and for sound to be existent
## these define 3 separate sound channels
##since only a single file can be played at a time per channel, 
##multiple are needed to play background music, and sound effects at the same time
define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## sample sound for user to test
## define config.sample_sound = "sample-sound.ogg"
## define config.sample_voice = "sample-voice.ogg"


## music to be played on the main menu
## Nintendo, Fountain Gardens (Kirbys Epic Yarn)
define config.main_menu_music = "audio/titlescreenmusic.mp3"

## transition type into main game menu
define config.enter_transition = dissolve
define config.exit_transition = dissolve

## transition type between game menus
define config.intra_transition = dissolve

## transition type into loaded game
define config.after_load_transition = dissolve

## transition type for enterting main menu when game ends
define config.end_game_transition = dissolve

## Controls if dialogue window is displayed 
## If "show", it is always up
## If "hide", only shows if dialogue is present
## "auto", hidden before scene statements then shown again
define config.window = "auto"

## dialogue window transitions, type(time in seconds)
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## text scrolling speed, in characters per second
default preferences.text_cps = 75

## Auto forward delay, values of 0-30, the larger the number, the slower
default preferences.afm_time = 15

## Place where files will be saved (DO NOT CHANGE): 
## for Windows: %APPDATA\RenPy\<config.save_directory>
##
## for Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## for Linux: $HOME/.renpy/<config.save_directory>
define config.save_directory = "GooseVisualNovel-1666730980"

## defines the app icon
define config.window_icon = "gui/window_icon.png"

## This section controls how Ren'Py turns your project into distribution files.
## DONT TOUCH 
## 
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    ## To archive files, classify them as 'archive'.
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')
    build.documentation('*.html')
    build.documentation('*.txt')
