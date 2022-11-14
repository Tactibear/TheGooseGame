# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME


## The statements in this file run before any other file because of the negative offset number
init offset = -2

## sets width and height of the game
init python:
    gui.init(1920, 1080)

## interface highlight colour
define gui.accent_color = '#cc0066'

## colour for text and buttons when no mouse hover
define gui.idle_color = '#ffffff'

## smaller sized text use this colour
define gui.idle_small_color = '#888888'

## colour of buttons and bars when hovered
define gui.hover_color = '#cc0066'

## colour of text when it is selected
define gui.selected_color = '#555555'

## unselectable text colour
define gui.insensitive_color = '#aaaaaa7f'

## colour for the unfilled part of bars
define gui.muted_color = '#e066a3'
define gui.hover_muted_color = '#ea99c1'

## dialogue and menu text colour
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'

## in-game text fonts
define gui.text_font = "DejaVuSans.ttf"
## character name fonts
define gui.name_text_font = "DejaVuSans.ttf"

## outside of game text
define gui.interface_text_font = "fonts/Blomberg.otf"

## size of dialogue text
define gui.text_size = 33

## character name sizes
define gui.name_text_size = 45

## GUI text size
define gui.interface_text_size = 50

## GUI labelling text size
define gui.label_text_size = 36

## notify screen text size
define gui.notify_text_size = 24

## game title text size
define gui.title_text_size = 75
define gui.title_text_outlines = [ (4, "#00000034", 7, 7), (4, "#000000", 3, 3) ]

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 360
define gui.name_ypos = 0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## styles that change button looks

## The width and height of a button, in pixels. If None, auto fits size
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, ordered left, top, right, bottom
define gui.button_borders = Borders(6, 2, 6, 2)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## button font
define gui.button_text_font = gui.interface_text_font

## button text size
define gui.button_text_size = gui.interface_text_size

## colour of button in different states
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## relative horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## variable customizations for each type of button

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## in-game menu button styles

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#ff00db"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_idle_color = '#000000'
define gui.choice_button_text_insensitive_color = "#444444"

## in-game menu confirm buttons CL

define gui.button_confirm_idle_color = '#303030'
define gui.button_confirm_color = gui.hover_color
define gui.button_confirm_selected_color = gui.selected_color
define gui.button_Confirm_insensitive_color = gui.insensitive_color

## save file slot buttons

## save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## width and height of thumbnails 
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## number of columns and rows in the grid
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## position of the left side of the navigation buttons, relative to the left
## side of the screen
define gui.navigation_xpos = 60

## vertical position of the skip indicator
define gui.skip_ypos = 15

## vertical position of the notify screen
define gui.notify_ypos = 68

## spacing between menu choices
define gui.choice_spacing = 33

## main menu navigation buttons spaces defined
define gui.navigation_spacing = 4

## amount of spacing between preferences
define gui.pref_spacing = 15

## amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## spacing between file page buttons.
define gui.page_spacing = 0

## spacing between file slots.
define gui.slot_spacing = 15

## position of the main menu text.
define gui.main_menu_text_xalign = 1.0

## the actual containers used to contain certain preset screens 

## Generic frames
define gui.frame_borders = Borders(6, 2, 6, 2)

## confirm screen frame
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## skip screen frame
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## notify screen frame
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## frame bgc tiling statement
define gui.frame_tile = False

## The height and width of horizontal bars, scrollbars, and sliders
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## to tile: true, to linear scale: false
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## If a bar is unscrollable, hide
define gui.unscrollable = "hide"

## number of blocks of dialogue history that will be kept
define config.history_length = 250

## The height of a history screen entry
define gui.history_height = 210

## character name position, width, and alignment
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Visual novels have two types of presentation, ADV mode (above) where narration and characters speak dialogue one line at a time, in a window at the bottom of the screen, while NVL mode (below) shows multiple lines at a time, in a window that takes up the entire screen. WIll be irrelevant for most of the project.

## borders of the background of the NVL-mode background window
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries that can be displayed
define gui.nvl_list_length = 6

## height of an NVL-mode entry
define gui.nvl_height = 173

## spacing between NVL-mode entries 
define gui.nvl_spacing = 15

## speaking character position, width, and alignment
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## position, width, and alignment of nvl narration text
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## position of nvl menu_buttons
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## defines the language of graphics user interface
define gui.language = "unicode"
