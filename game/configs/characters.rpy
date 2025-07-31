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

#region characters
define t = Character('Тайда', color='#4a9eff', image_small='t',
                        callback=ft.partial(layered_talking_callback, character_name='t'))
                        
define d = Character('Дзинзо', color='#ffdfba', image='d',
                        callback=ft.partial(layered_talking_callback, character_name='d'))

define u = Character('Юми', color='#ffdfba', image='u',
                        callback=ft.partial(layered_talking_callback, character_name='u'))

define k = Character('Кацуми', color='#ffdfba', image='k',
                        callback=ft.partial(layered_talking_callback, character_name='k'))

define h = Character('Хикару', color='#bae1ff', image='h',
                        callback=ft.partial(layered_talking_callback, character_name='h'))

define d = Character('Ден', color='#ffdfba', image='den',
                        callback=ft.partial(layered_talking_callback, character_name='den'))

define i = Character('Изуми', color='#ffb3ba', image='i', 
                        callback=ft.partial(layered_talking_callback, character_name = "i"))

define dad = Character('Папа', color='#ffdfba', image='dad',
                        callback=ft.partial(layered_talking_callback, character_name='dad'))

define mom = Character('Мама', color='#ffdfba', image='mom',
                        callback=ft.partial(layered_talking_callback, character_name='mom'))


#endregion

#region Taida  

layeredimage t:
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
        attribute asharashen: #ашарашен
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

#region Dzinzo

#region Umi

layeredimage u:
    group pose:
        attribute open default:
            Null()
        attribute closed:
            Null()
        attribute greeting:
            "images/Umi/Umi_pose3_smile.png"

    group emotion if_any "open":
        attribute neutral default:
            "images/Umi/Umi_pose1_neutral.png"
        attribute angry:
            "images/Umi/Umi_pose1_angry.png"
        attribute cute:
            "images/Umi/Umi_pose1_cute.png"
        attribute embarrassed:
            "images/Umi/Umi_pose1_embrassed.png"
        attribute laugh:
            "images/Umi/Umi_pose1_laught.png"
        attribute laugh_wall:
            "images/Umi/Umi_pose1_laught_4stena.png"
        attribute surprised:
            "images/Umi/Umi_pose1_surprised.png"
        attribute thinking:
            "images/Umi/Umi_pose1_thinking.png"
    
    group emotion if_any "closed":
        attribute alluring default:
            "images/Umi/Umi_pose2_alluring.png"
        attribute confused:
            "images/Umi/Umi_pose2_confused.png"
        attribute cry:
            "images/Umi/Umi_pose2_cry.png"
        attribute cry_embarrassed:
            "images/Umi/Umi_pose2_cry_asharashen.png"
        attribute sad_cry:
            "images/Umi/Umi_pose2_sad_cry.png"
        attribute touched:
            "images/Umi/Umi_pose2_touched.png"
        attribute tricky:
            "images/Umi/Umi_pose2_tricky.png"
    
    group emotion if_any "greeting":
        attribute smile default:
            "images/Umi/Umi_pose3_smile.png"
        attribute confused:
            "images/Umi/Umi_pose3_confused.png"
        attribute offended:
            "images/Umi/Umi_pose3_offended.png"
        attribute offended_sad:
            "images/Umi/Umi_pose3_offended_sad.png"

    group mouth if_any "open":
        attribute talk:
            "umi_talk_open"
    
    group mouth if_any "closed":
        attribute talk:
            "umi_talk_closed"

    group mouth if_any "greeting":
        attribute talk:
            "umi_talk_greeting"

    group dress if_any "open":
        attribute school default:
            "images/Umi/Umi_pose1_shkolnoe.png"
        attribute summer:
            "images/Umi/Umi_pose1_letnee.png"
    
    group dress if_any "closed":
        attribute school default:
            "images/Umi/Umi_pose2_shkolnoe.png"
        attribute summer:
            "images/Umi/Umi_pose2_letnee.png"

    group dress if_any "greeting":
        attribute school default:
            Null()

image umi_talk_open:
    "images/Umi/Umi_pose1_rot1.png"
    pause 0.1
    "images/Umi/Umi_pose1_rot2.png"
    pause 0.1
    "images/Umi/Umi_pose1_rot3.png"
    repeat

image umi_talk_closed:
    "images/Umi/Umi_pose2_rot1.png"
    pause 0.1
    "images/Umi/Umi_pose2_rot2.png"
    pause 0.1
    "images/Umi/Umi_pose2_rot3.png"
    repeat

image umi_talk_greeting:
    "images/Umi/Umi_pose3_rot1.png"
    pause 0.1
    "images/Umi/Umi_pose3_rot2.png"
    pause 0.1
    "images/Umi/Umi_pose3_rot3.png"
    repeat

#endregion

#region Dad
layeredimage dad:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/dad/Dad.png"

    group mouth:
        attribute talk if_any "idle":
            "dad_talk_idle"

image dad_talk_idle:
    "images/dad/Dad_rot_1.png"
    pause 0.1
    "images/dad/Dad_rot_2.png"
    pause 0.1
    "images/dad/Dad_rot_3.png"
    repeat
#endregion

#region Mom
layeredimage mom:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/mom/Mom.png"

    group mouth:
        attribute talk if_any "idle":
            "mom_talk_idle"

image mom_talk_idle:
    "images/mom/Mom_rot_1.png"
    pause 0.1
    "images/mom/Mom_rot_2.png"
    pause 0.1
    "images/mom/Mom_rot_3.png"
    repeat

#endregion

#region Izumi

layeredimage i:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Izumi/Izumi_neutral.png"
        attribute angry:
            "images/Izumi/Izumi_angry.png"
        attribute asharasen:
            "images/Izumi/Izumi_asharasen.png"
        attribute calm:
            "images/Izumi/Izumi_calm.png"
        attribute dreamy:
            "images/Izumi/Izumi_dreamy.png"
        attribute interested:
            "images/Izumi/Izumi_interested.png"
        attribute neutral_2:
            "images/Izumi/Izumi_neutral_2.png"
        attribute neutral_3:
            "images/Izumi/Izumi_neutral_3.png"
        attribute smug:
            "images/Izumi/Izumi_smug.png"
        attribute thinking:
            "images/Izumi/Izumi_thinking.png"
        attribute tricky:
            "images/Izumi/Izumi_tricky.png"
        attribute very_angry:
            "images/Izumi/Izumi_very_angry.png"
    
    group mouth:
        attribute talk if_any "idle":
            "izumi_talk_idle"

image izumi_talk_idle:
    "images/Izumi/Izumi_rot_1.png"
    pause 0.1
    "images/Izumi/Izumi_rot_2.png"
    pause 0.1
    "images/Izumi/Izumi_rot_3.png"
    repeat

#endregion