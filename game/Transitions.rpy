style opening:
    xalign 0.5
    xfill True
    yfill True
    background "images/Opening.png"
style Centering:
    xalign 0.5
    yalign 0.5
    spacing 8



screen Opening1():
    frame:
        style "opening"
screen day1():
    hbox:
        style "Centering"
        text('Day one'):
            size 200
            color '#ffffff'
            font 'fonts/Handwritten_Bold.ttf'
