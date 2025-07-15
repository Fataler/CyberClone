
define BATTLE_MESSAGE_TIME = 2.5

define MSG_KOSTYAN_ATTACK = "Костян наносит удар. Снято 2 HP"
define MSG_MISHANYA_ATTACK = "Мишаня наносит удар. Снято 999 HP"
define MSG_KOSTYAN_DEFEATED = "Костян повержен!"
define MSG_ESCAPE_FAILED = "Побег невозможен!"
define MSG_BAG_USELESS = "В сумке завалялся вчерашний обед. Костяну это не поможет."
define MSG_MAGIC_SUCCESS = "Костян притворился спящим. Мишаня недоумевает и теряет 2 HP"
define MSG_MAGIC_FAILED = "Больше это не сработает."

default kostyan_hp = 100
default mishanya_hp = 100
default battle_state = "select_action"  # select_action, attacking, enemy_turn, defeated, kostyan_defeated
default battle_message = ""
default show_battle_buttons = True
default magic_used = False

transform pokemon_attack_left:
    xoffset 0
    linear 0.15 xoffset -40
    linear 0.15 xoffset 40
    linear 0.15 xoffset -40
    linear 0.15 xoffset 40
    linear 0.15 xoffset 0

transform pokemon_attack_right:
    xoffset 0
    linear 0.15 xoffset 40
    linear 0.15 xoffset -40
    linear 0.15 xoffset 40
    linear 0.15 xoffset -40
    linear 0.15 xoffset 0

transform battle_entrance_left:
    xpos -200
    alpha 0.0
    ease 1.0 xpos 150 alpha 1.0

transform battle_entrance_right:
    xpos 1500
    alpha 0.0
    ease 1.0 xpos 1100 alpha 1.0

transform kostyan_defeat_shake:
    xoffset 0
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -5
    linear 0.1 xoffset 5
    linear 0.1 xoffset 0
    ease 2.0 alpha 0.0

screen pokemon_battle():
    tag battle
    modal True
    
    add "#7DD3FC"
    
    add Solid("#65A30D") xysize (1920, 400) ypos 680
    
    if battle_state == "kostyan_defeated":
        add Solid("#FFD700") xysize (180, 180) pos (150, 350) at kostyan_defeat_shake
        text "Костян" pos (150, 540) size 22 color "#000000"
    elif battle_state != "defeated":
        if battle_state == "attacking":
            add Solid("#FFD700") xysize (180, 180) pos (150, 350) at pokemon_attack_left
        else:
            add Solid("#FFD700") xysize (180, 180) pos (150, 350) at battle_entrance_left
        text "Костян" pos (150, 540) size 22 color "#000000"
    
    if battle_state == "enemy_turn":
        add Solid("#FF6347") xysize (160, 160) pos (1100, 120) at pokemon_attack_right
    else:
        add Solid("#FF6347") xysize (160, 160) pos (1100, 120) at battle_entrance_right
    text "Мишаня" pos (1100, 290) size 22 color "#000000"
    
    frame:
        pos (950, 380)
        xysize (400, 140)
        background "#FFFFFF"
        
        vbox:
            spacing 5
            text "Костян" size 26 color "#000000" xalign 0.0
            hbox:
                text "Ур.17" size 20 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 18 color "#000000"
                bar:
                    value kostyan_hp
                    range 100
                    xysize (250, 20)
                    left_bar "#00FF00"
                    right_bar "#808080"
            
            text "[kostyan_hp]/100" size 18 color "#000000" xalign 1.0
    
    frame:
        pos (80, 80)
        xysize (350, 100)
        background "#FFFFFF"
        
        vbox:
            spacing 3
            text "Мишаня" size 24 color "#000000" xalign 0.0
            hbox:
                text "Ур.17" size 18 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 16 color "#000000"
                bar:
                    value mishanya_hp
                    range 100
                    xysize (200, 18)
                    left_bar "#00FF00"
                    right_bar "#808080"
    
    frame:
        pos (80, 600)
        xysize (1760, 300)
        background "#FFFFFF"
        
        hbox:
            spacing 20
            
            vbox:
                xsize 1100
                spacing 20
                
                if battle_message:
                    text battle_message size 28 color "#000000" xpos 30 ypos 30
                elif battle_state == "select_action":
                    text "Что сделает Костян?" size 28 color "#000000" xpos 30 ypos 30
                else:
                    text " " size 28 color "#000000" xpos 30 ypos 30
            
            if show_battle_buttons and battle_state == "select_action":
                vbox:
                    spacing 20
                    xpos 50
                    ypos 30
                    
                    hbox:
                        spacing 20
                        
                        textbutton "УДАР":
                            xysize (240, 80)
                            text_size 28
                            text_color "#FFFFFF"
                            background "#FF6347"
                            hover_background "#FF4500"
                            action Function(start_attack)
                        
                        textbutton "СУМКА":
                            xysize (240, 80)
                            text_size 28
                            text_color "#FFFFFF"
                            background "#4169E1"
                            hover_background "#1E90FF"
                            action Function(try_bag)
                    
                    hbox:
                        spacing 20
                        
                        textbutton "МАГИЯ":
                            xysize (240, 80)
                            text_size 28
                            text_color "#FFFFFF"
                            background "#32CD32"
                            hover_background "#00FF00"
                            action Function(try_magic)
                        
                        textbutton "БЕЖАТЬ":
                            xysize (240, 80)
                            text_size 28
                            text_color "#FFFFFF"
                            background "#FFD700"
                            hover_background "#FFA500"
                            action Function(try_escape)
    
    if battle_state == "attacking":
        timer BATTLE_MESSAGE_TIME action Function(enemy_attack)
    elif battle_state == "enemy_turn":
        timer BATTLE_MESSAGE_TIME action Function(defeat_kostyan)
    elif battle_state == "defeated":
        timer BATTLE_MESSAGE_TIME action Function(start_kostyan_defeat)
    elif battle_state == "kostyan_defeated":
        timer 3.0 action Function(end_battle)
    elif battle_message == MSG_ESCAPE_FAILED:
        timer BATTLE_MESSAGE_TIME action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]
    elif battle_message == MSG_BAG_USELESS:
        timer BATTLE_MESSAGE_TIME action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]
    elif battle_message in [MSG_MAGIC_SUCCESS, MSG_MAGIC_FAILED]:
        timer BATTLE_MESSAGE_TIME+1.0 action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]

init python:
    def start_attack():
        global battle_state, battle_message, show_battle_buttons, mishanya_hp
        
        battle_state = "attacking"
        show_battle_buttons = False
        battle_message = MSG_KOSTYAN_ATTACK
        mishanya_hp -= 2
        
        renpy.restart_interaction()
    
    def try_escape():
        global battle_message, show_battle_buttons
        
        show_battle_buttons = False
        battle_message = MSG_ESCAPE_FAILED
        
        renpy.restart_interaction()

    def try_bag():
        global battle_message, show_battle_buttons
        
        show_battle_buttons = False
        battle_message = MSG_BAG_USELESS
        
        renpy.restart_interaction()
    
    def try_magic():
        global battle_message, show_battle_buttons, magic_used, mishanya_hp
        
        if not magic_used:
            show_battle_buttons = False
            battle_message = MSG_MAGIC_SUCCESS
            mishanya_hp -= 2
            magic_used = True
        else:
            show_battle_buttons = False
            battle_message = MSG_MAGIC_FAILED
        
        renpy.restart_interaction()
        
    def enemy_attack():
        global kostyan_hp, battle_message, battle_state
        
        battle_state = "enemy_turn"
        battle_message = MSG_MISHANYA_ATTACK
        kostyan_hp -= 999
        
        if kostyan_hp <= 0:
            kostyan_hp = 0
        
        renpy.restart_interaction()
    
    def defeat_kostyan():
        global battle_message, battle_state, show_battle_buttons
        
        if kostyan_hp <= 0:
            battle_message = MSG_KOSTYAN_DEFEATED
            battle_state = "defeated"
        else:
            battle_message = ""
            battle_state = "select_action"
            show_battle_buttons = True
        
        renpy.restart_interaction()
    
    def start_kostyan_defeat():
        global battle_state, battle_message
        
        battle_state = "kostyan_defeated"
        battle_message = ""
        renpy.restart_interaction()
    
    def end_battle():
        renpy.hide_screen("pokemon_battle")
        renpy.return_statement()