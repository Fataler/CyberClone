image ctc_rotate:
    "gui/bubble.png"
    size (32, 32)
    anchor (0.5, 0.5)
    alpha 1
    linear 2 alpha 0.6
    linear 2 alpha 1
    repeat

define ctc_indicator = Animation("ctc_rotate")

image ctc_mind:
    "gui/ctc_mind.png"
    size (32, 32)
    anchor (0.5, 0.5)
    alpha 1
    linear 2 alpha 0.6
    linear 2 alpha 1
    repeat

define ctc_mind_indicator = Animation("ctc_mind")

define robot_bin = robot_say
define robot = Character("")

define H = Character("Хикару", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

define K = Character("Кацуми", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

#region Izumi
define izumi = Character('Изуми', color='#ffb3ba', image='izumi',
                        callback=ft.partial(talking_callback, character_name='izumi'))
#endregion

#region Taida  
define taida = Character('Тайда', color='#4a9eff', image='taida',
                        callback=ft.partial(layered_talking_callback, character_name='taida'))

layeredimage taida:
    group pose:
        attribute idle default:
            'images/taida/GG_mini_1.png'
        attribute thinking:
            'images/taida/GG_mini_thinking.png'

    group emotion if_any "idle":
        attribute neutral default: #нейтральное
            'images/taida/GG_mini_5.png'
        attribute cry: #плач
            'images/taida/GG_mini_1.png'
        attribute dream: #сон
            'images/taida/GG_mini_2.png'
        attribute surprised: #удивлен
            'images/taida/GG_mini_3.png'
        attribute sad_angry: #грусть + злость
            'images/taida/GG_mini_4.png'
        attribute angry: #злость
            'images/taida/GG_mini_6.png'
        attribute sad: #печаль
            'images/taida/GG_mini_7.png'
        attribute fear: #страх
            'images/taida/GG_mini_8.png'
        attribute crazy: #безумие
            'images/taida/GG_mini_9.png'
        attribute happy: #счастье
            'images/taida/GG_mini_10.png'
        attribute tricky: #хитрость
            'images/taida/GG_mini_11.png'
        attribute neutral_happy: #нейтральное счастье
            'images/taida/GG_mini_12.png'
        attribute thinking: #думаю
            'images/taida/GG_mini_13.png'
        attribute asharasen: #ашарашен
            'images/taida/GG_mini_14.png'
        attribute calm: #спокойно
            'images/taida/GG_mini_15.png'
        attribute depressed: #депрессия
            'images/taida/GG_mini_16.png'


    group emotion if_any "thinking":
        attribute neutral default:
            Null()
        attribute confused:
            'images/taida/GG_mini_13.png'
        attribute focused:
            'images/taida/GG_mini_14.png'

    group mouth:
        attribute talk if_any "idle":
            'taida_talk_idle'
        attribute talk if_any "thinking":
            'taida_talk_thinking'

image taida_talk_idle:
    'images/taida/GG_mini_rot_1.png'
    pause 0.1
    'images/taida/GG_mini_rot_2.png'
    pause 0.1
    'images/taida/GG_mini_rot_3.png'
    pause 0.1
    repeat

image taida_talk_thinking:
    'images/taida/GG_mini_rot_1.png'
    pause 0.1
    'images/taida/GG_mini_rot_2.png'
    pause 0.1
    'images/taida/GG_mini_rot_3.png'
    pause 0.1
    repeat

#endregion
