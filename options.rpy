# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL

## Name the game on title screen
define config.name = _("Goose Visual Novel")

## show title on title screen
define gui.show_name = True

## subtitle on title screen
define config.version = "Navigate the muddy waters of relationship trauma the average waterloo student experiences while their money is being used to make pull door handles that look like push"

## About menu text
define gui.about = _p("""Regretted by Camillo, Charles, Emily, and Stephanie
""")

## file name, pls dont change
define build.name = "GooseVisualNovel"

## Gives the user ability to use sound mixer
define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## sample sound for user to test
## define config.sample_sound = "sample-sound.ogg"
## define config.sample_voice = "sample-voice.ogg"


## music to be played on the main menu
## define config.main_menu_music = "main-menu-theme.ogg"

## transition into main game menu
define config.enter_transition = dissolve
define config.exit_transition = dissolve

## transition between game menus
define config.intra_transition = dissolve

## transition into loaded game
define config.after_load_transition = None

## transition for enterting main menu when game ends
define config.end_game_transition = None

## Controls if dialogue window is displayed 
## If "show", it is always up
## If "hide", only shows if dialogue is present
## "auto", hidden before scene statements then shown again
define config.window = "auto"

## dialogue window transitions
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## text speed, in characters per second
default preferences.text_cps = 10

## Auto forward delay, values of 0-30, the larger the number, the slower
default preferences.afm_time = 15

## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.
define config.save_directory = "GooseVisualNovel-1666730980"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.
define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
