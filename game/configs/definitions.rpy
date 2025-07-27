#constants
default persistent.first_start = True
default persistent.game_completed = False

define splash_enabled = False

default textbox_style = "gui/textbox.png"
default character = "Taida"

define TEXTBOX_NORMAL = "gui/textbox.png"
define TEXTBOX_ROBOT = "gui/textbox_robot.png"
define CHARACTER_TAIDA = "Taida"
define CHARACTER_DZINZO = "Dzinzo"

init python:
    def set_character_taida():
        global textbox_style, character
        character = CHARACTER_TAIDA
        textbox_style = TEXTBOX_NORMAL
        renpy.restart_interaction()
    
    def set_character_dzinzo():
        global textbox_style, character
        character = CHARACTER_DZINZO
        textbox_style = TEXTBOX_ROBOT
        renpy.restart_interaction()
    
    def set_textbox_custom(path):
        global textbox_style
        textbox_style = path
        renpy.restart_interaction()