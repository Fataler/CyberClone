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
            'images/taida/Taida_mini_neutral.png'
        attribute thinking:
            'images/taida/Taida_mini_thinking.png'

    group emotion if_any "idle":
        attribute neutral default: #нецтральный
            'images/taida/Taida_mini_neutral.png'
        attribute cry: #плачет
            'images/taida/Taida_mini_cry.png'
        attribute dream: #мечтательный
            'images/taida/Taida_mini_dream.png'
        attribute surprised: #удивлен
            'images/taida/Taida_mini_surprised.png'
        attribute sad_angry: #грусть + злость
            'images/taida/Taida_mini_sad_angry.png'
        attribute angry: #злость
            'images/taida/Taida_mini_angry.png'
        attribute sad: #печальный
            'images/taida/Taida_mini_sad.png'
        attribute fear: #испуганный
            'images/taida/Taida_mini_fear.png'
        attribute crazy: #безумие
            'images/taida/Taida_mini_crazy.png'
        attribute happy: #счастливый
            'images/taida/Taida_mini_happy.png'
        attribute tricky: #хитрость
            'images/taida/Taida_mini_tricky.png'
        attribute neutral_happy: #нейтральный счастливый
            'images/taida/Taida_mini_neutral_happy.png'
        attribute thinking: #думаю
            'images/taida/Taida_mini_thinking.png'
        attribute asharasen: #ашарашен
            'images/taida/Taida_mini_asharasen.png'
        attribute calm: #спокойный
            'images/taida/Taida_mini_calm.png'
        attribute depressed: #депрессивный
            'images/taida/Taida_mini_depressed.png'


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
