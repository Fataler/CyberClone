#region images
image bg_battle = "images/MiniGames/Battle/bg.png"

image taida_sprite:
    "images/MiniGames/Battle/gg.png"
    zoom 0.8

image dzinzo_sprite:
    "images/MiniGames/Battle/rgg.png"
    xzoom -1
    zoom 0.65
#endregion

define MSG_TAIDA_DEFAULT = "Что сделает Тайда?"
define MSG_TAIDA_DEFEATED = "Тайда повержен! Бой окончен."
define MSG_ESCAPE_FAILED = "Побег невозможен!"

define BAG_MESSAGES = [
    "Тайда шарится в сумке и находит пару игрушек из игровых автоматов. Тайда наполняется решимостью.",
    "В сумке завалялся вчерашний обед. Костяну это не поможет.",
    "Тайда шарится в сумке, но больше ничего не может найти.",]

define MAGIC_MESSAGES = [
    "Тайда начинает носиться по комнате. Дзинзо недоумевает и теряет 2 HP.",
    "Чтобы отдохнуть, Тайда притворился спящим. Дзинзо теряет 20 секунд времени и 2 HP.",
    "Тайда слишком устала и не может двигаться. Дзинзо начинает опаздывать и теряет 2 HP.",
    "Больше это не сработает."]

define TAIDA_BATTLE_MESSAGES = [
    "Собрав все свои силы, Тайда ударяет Дзинзо. Снято 2 HP.",
    "Тайда снова наносит удар! Критический промах. Снятно 2 HP.",
    "Тайда решает применить свой особый удар. Удар оказывается неэффективным. Снято 2 HP.",
    "Тайда: 'Нет! Мы ещё не закончили!'"]

define DZINZO_BATTLE_MESSAGES = [
    "Дзинзо не понимает что проиходит и пропускает ход.",
    "Дзинзо пропускает ход и говорит: 'Господин, что происходит? Это какая-то тренировка ваших физических способностей?",
    "Дзинзо: 'Простите, меня ждет ваша мама в саду. Позвольте мне отканяться.'",]

define MSG_DZINZO_ATTACK = "Дзинзо: 'Хорошо, давайте я проверю ваши показатели защиты.' Дзинзо наносит удар. Снято 999 HP."

default kostyan_hp = 100
default mishanya_hp = 100
default battle_state = "select_action" #"select_action"  # select_action, attacking, enemy_turn, defeated, kostyan_defeated, message_show
default battle_message = ""
default show_battle_buttons = True
default magic_used = False
default bag_message_index = 0
default magic_message_index = 0
default taida_battle_index = 0
default dzinzo_battle_index = 0

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

transform dzinzo_hit_effect:
    matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.3)
    linear 0.3 matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.8)
    linear 0.3 matrixcolor TintMatrix("#ff0000") * BrightnessMatrix(0.3)
    linear 0.4 matrixcolor IdentityMatrix()

transform battle_entrance_left:
    xoffset -400
    alpha 0.0
    ease 1.5 xoffset 0 alpha 1.0

transform battle_entrance_right:
    xoffset 400
    alpha 0.0
    ease 1.5 xoffset 0 alpha 1.0

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

style message_text:
    color "#000000"
    size 45
    xalign 0.0
    yalign 0.5

transform taida_pos:
    pos (0, -215)
    anchor (0.0, 0.5)

transform dzinzo_pos:
    pos (-20, -178)
    anchor (0.0, 0.5)

transform ui_fade_in:
    alpha 0.0
    pause 1.0
    ease 0.8 alpha 1.0

screen pokemon_battle():
    tag battle
    modal True
    
    add "bg_battle"

    frame:
        pos (750, 1000)
        
        xysize (380, 130)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (15, 15)
        at battle_entrance_left
        
        vbox:
            spacing 8
            xalign 0.0
            yalign 0.5
            
            text "Тайда" size 28 color "#000000" xalign 0.0
            hbox:
                text "Ур.17" size 25 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 18 color "#000000"
                bar:
                    value AnimatedValue(kostyan_hp, 100, 2.0)
                    range 100
                    ysize 18
                    left_bar "#00FF00"
                    right_bar "#808080"
            
            text "[kostyan_hp]/100" size 20 color "#000000" xalign 1.0

        if battle_state == "kostyan_defeated":
            add "taida_sprite" at kostyan_defeat_shake, taida_pos
        elif battle_state == "attacking":
            add "taida_sprite" at pokemon_attack_left, taida_pos
        elif battle_state == "select_action":
            add "taida_sprite" at taida_pos
        else:
            add "taida_sprite" at taida_pos
    
    frame:
        pos (1500, 680)
        xysize (380, 130)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (15, 15)
        at battle_entrance_right
        
        vbox:
            spacing 8
            xalign 0.0
            yalign 0.5
            
            text "Дзинзо" size 28 color "#000000" xalign 0.0
            hbox:
                text "Ур.???" size 25 color "#000000" xalign 1.0
            
            hbox:
                spacing 10
                text "HP" size 18 color "#000000"
                bar:
                    value AnimatedValue(mishanya_hp, 100, 2.0)
                    range 100
                    ysize 18
                    left_bar "#00FF00"
                    right_bar "#808080"

            text "???/???" size 20 color "#000000" xalign 1.0

        if battle_state == "enemy_turn":
            add "dzinzo_sprite" at pokemon_attack_right, dzinzo_pos
        elif battle_state == "enemy_skip":
            add "dzinzo_sprite" at dzinzo_hit_effect, dzinzo_pos
        elif battle_state == "select_action":
            add "dzinzo_sprite" at dzinzo_pos
        else:
            add "dzinzo_sprite" at dzinzo_pos
    

    frame:
        xpos 0.5
        ypos 0.15
        xysize (1200, 100)
        background "#FFFFFF"
        anchor (0.5, 0.5)
        padding (20, 20)
        at ui_fade_in
        
        vbox:
            xalign 0.5
            yalign 0.5
            
            if battle_message:
                text battle_message style "message_text"
            elif battle_state == "select_action":
                text MSG_TAIDA_DEFAULT style "message_text"
            else:
                text " " style "message_text"
    
    if show_battle_buttons and battle_state == "select_action":
        frame:
            xpos 0.95
            ypos 0.95
            xysize (500, 180)
            background "#FFFFFF"
            anchor (1.0, 1.0)
            padding (15, 15)
            at ui_fade_in
            
            vbox:
                spacing 15
                xalign 0.5
                yalign 0.5
                
                hbox:
                    spacing 15
                    xalign 0.5
                    
                    textbutton "УДАР":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#FF6347"
                        hover_background "#FF4500"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(start_attack)
                    
                    textbutton "СУМКА":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#4169E1"
                        hover_background "#1E90FF"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_bag)
                
                hbox:
                    spacing 15
                    xalign 0.5
                    
                    textbutton "МАГИЯ":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#32CD32"
                        hover_background "#00FF00"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_magic)
                    
                    textbutton "БЕЖАТЬ":
                        xysize (220, 70)
                        text_size 26
                        text_color "#FFFFFF"
                        background "#FFD700"
                        hover_background "#FFA500"
                        text_outlines [(1, "#000000", 0, 0)]
                        action Function(try_escape)
    
    if battle_state == "attacking":
        timer get_message_time(battle_message) action Function(enemy_attack)
    elif battle_state == "enemy_turn":
        timer get_message_time(battle_message) action Function(defeat_kostyan)
    elif battle_state == "defeated":
        timer get_message_time(battle_message) action Function(start_kostyan_defeat)
    elif battle_state == "kostyan_defeated":
        timer 3.0 action Function(end_battle)
    elif battle_message == MSG_ESCAPE_FAILED:
        timer get_message_time(battle_message) action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]
    elif battle_message in BAG_MESSAGES:
        timer get_message_time(battle_message) + 1.0 action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]
    elif battle_message in MAGIC_MESSAGES:
        timer get_message_time(battle_message) + 1.0 action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]
    elif battle_message in TAIDA_BATTLE_MESSAGES:
        timer get_message_time(battle_message) action Function(enemy_attack)
    elif battle_state == "enemy_skip":
        timer get_message_time(battle_message) action [SetVariable("battle_message", ""), SetVariable("show_battle_buttons", True), SetVariable("battle_state", "select_action")]

init python:
    def get_message_time(message):
        if not message:
            return 2.0
        
        time = 2.0 + len(message) * 0.05
        return max(2.0, min(10.0, time))

    def start_attack():
        global battle_state, battle_message, show_battle_buttons, mishanya_hp, taida_battle_index, dzinzo_battle_index
        
        battle_state = "attacking"
        show_battle_buttons = False
        
        # Проверяем, есть ли ещё сообщения для боя
        if taida_battle_index < len(TAIDA_BATTLE_MESSAGES) and dzinzo_battle_index < len(DZINZO_BATTLE_MESSAGES):
            battle_message = TAIDA_BATTLE_MESSAGES[taida_battle_index]
            mishanya_hp -= 2  # Наносим урон
            taida_battle_index += 1
        else:
            # Если сообщения закончились, начинается настоящий бой
            battle_message = MSG_DZINZO_ATTACK
        
        renpy.restart_interaction()
    
    def try_escape():
        global battle_message, show_battle_buttons
        
        show_battle_buttons = False
        battle_message = MSG_ESCAPE_FAILED
        
        renpy.restart_interaction()

    def try_bag():
        global battle_message, show_battle_buttons, bag_message_index
        
        show_battle_buttons = False
        battle_message = BAG_MESSAGES[bag_message_index]
        
        bag_message_index = min(bag_message_index + 1, len(BAG_MESSAGES) - 1)
        
        renpy.restart_interaction()
    
    def try_magic():
        global battle_message, show_battle_buttons, magic_message_index, mishanya_hp
        
        show_battle_buttons = False
        
        battle_message = MAGIC_MESSAGES[magic_message_index]
        
        if magic_message_index < len(MAGIC_MESSAGES) - 1:
            mishanya_hp -= 2
        
        magic_message_index = min(magic_message_index + 1, len(MAGIC_MESSAGES) - 1)
        
        renpy.restart_interaction()
        
    def enemy_attack():
        global kostyan_hp, battle_message, battle_state, dzinzo_battle_index
        
        if dzinzo_battle_index < len(DZINZO_BATTLE_MESSAGES):
            battle_state = "enemy_skip"
            battle_message = DZINZO_BATTLE_MESSAGES[dzinzo_battle_index]
            dzinzo_battle_index += 1
        else:
            battle_state = "enemy_turn"
            battle_message = MSG_DZINZO_ATTACK
            kostyan_hp -= 999
            
            if kostyan_hp <= 0:
                kostyan_hp = 0
        
        renpy.restart_interaction()
    
    def defeat_kostyan():
        global battle_message, battle_state, show_battle_buttons
        
        if kostyan_hp <= 0:
            battle_message = MSG_TAIDA_DEFEATED
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
    
    def reset_battle():
        global kostyan_hp, mishanya_hp, battle_state, battle_message, show_battle_buttons
        global bag_message_index, magic_message_index, taida_battle_index, dzinzo_battle_index, magic_used
        
        kostyan_hp = 100
        mishanya_hp = 100
        battle_state = "select_action"
        battle_message = ""
        show_battle_buttons = True
        bag_message_index = 0
        magic_message_index = 0
        taida_battle_index = 0
        dzinzo_battle_index = 0
        magic_used = False
        
        renpy.restart_interaction()