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
define t = Character('Тайда', color='#4a9eff', image='t', callback=speaker('t'))

define t_t = Character('', color='#4a9eff', image='t')
                        
define d = Character('Дзинзо', color='#ffdfba', image='d',
                        callback=speaker('d'))

define u = Character('Юми', color='#ffdfba', image='u',
                        callback=speaker('u'))

define k = Character('Кацуми', color='#ffdfba', image='k',
                        callback=speaker('k'))

define h = Character('Хикару', color='#bae1ff', image='h',
                        callback=speaker('h'))

define d = Character('Ден', color='#ffdfba', image='den',
                        callback=speaker('den'))

define i = Character('Изуми', color='#ffb3ba', image='i', 
                        callback=speaker('i'))

define dad = Character('Папа', color='#ffdfba', image='dad',
                        callback=speaker('dad'))

define mom = Character('Мама', color='#ffdfba', image='mom',
                        callback=speaker('mom'))

#region Taida
layeredimage side t:
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

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('t', 'taida_talk_idle', Null())
        attribute talk if_any "thinking":
            WhileSpeaking('t', 'taida_talk_thinking', Null())

image taida_talk_idle:
    'images/taida/GG_mini_rot_1.png'
    pause 0.1
    'images/taida/GG_mini_rot_2.png'
    pause 0.1
    'images/taida/GG_mini_rot_3.png'
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
#endregion

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
            WhileSpeaking('u', 'umi_talk_open', Null())
    
    group mouth if_any "closed":
        attribute talk:
            WhileSpeaking('u', 'umi_talk_closed', Null())

    group mouth if_any "greeting":
        attribute talk:
            WhileSpeaking('u', 'umi_talk_greeting', Null())

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
            WhileSpeaking('dad', 'dad_talk_idle', Null())

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
            WhileSpeaking('mom', 'mom_talk_idle', Null())

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
            WhileSpeaking('i', 'izumi_talk_idle', Null())

image izumi_talk_idle:
    "images/Izumi/Izumi_rot_1.png"
    pause 0.1
    "images/Izumi/Izumi_rot_2.png"
    pause 0.1
    "images/Izumi/Izumi_rot_3.png"
    repeat

#endregion