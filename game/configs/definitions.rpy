#constants
default persistent.first_start = True
default persistent.game_completed = False

define splash_enabled = False

default textbox_style = "gui/textbox.png"

define TEXTBOX_NORMAL = "gui/textbox.png"
define TEXTBOX_ROBOT = "gui/textbox_robot.png"

init python:
    def set_textbox_normal():
        global textbox_style
        textbox_style = TEXTBOX_NORMAL
        renpy.restart_interaction()
    
    def set_textbox_robot():
        global textbox_style  
        textbox_style = TEXTBOX_ROBOT
        renpy.restart_interaction()
    
    def set_textbox_custom(path):
        global textbox_style
        textbox_style = path
        renpy.restart_interaction()