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
define t = Character('Тайда', color='#2e5686', image='t', callback=speaker('t'))

define t_f = Character('Тайда', color='#2e5686', image='t_f', callback=speaker('t'))

define t_t = Character(None, color='#2e5686', image='t')
                        
define d = Character('Дзинзо', color='#3f3931', image='d', callback=speaker('d'))

define d_t = Character(None, color='#3f3931', image='d')

define u = Character('Юми', color='#681744', image='u', callback=speaker('u'))

define k = Character('Кацуми', color='#171658', image='k', callback=speaker('k'))

define h = Character('Хикару', color='#66161a', image='h', callback=speaker('h'))

define den = Character('Ден', color='#7e7719', image='den', callback=speaker('den'))

define i = Character('Изуми-сенсей', color='#431755', image='i', callback=speaker('i'))

define dad = Character('Папа', color='#0f4244', image='dad', callback=speaker('dad'))

define mom = Character('Мама', color='#15350b', image='mom', callback=speaker('mom'))

define teacher = Character('Учитель', color='#ffdfba', image='teacher')

#region Taida mini
layeredimage side t:
    group pose:
        attribute idle default:
            'images/taida/Taida_mini_neutral.png'
        attribute thinking_smile:
            'images/taida/Taida_mini_thinking_smile.png'
        attribute angry:
            'images/taida/Taida_mini_angry.png'
        attribute asharashen:
            'images/taida/Taida_mini_asharashen.png'
        attribute dream:
            'images/taida/Taida_mini_dream.png'
        attribute crazy:
            'images/taida/Taida_mini_crazy.png'
        attribute cry:
            'images/taida/Taida_mini_cry.png'
        attribute depressed:
            'images/taida/Taida_mini_depressed.png'
        attribute thinking:
            'images/taida/Taida_mini_dream.png'
        attribute fear:
            'images/taida/Taida_mini_fear.png'
        attribute dream_happy:
            'images/taida/Taida_mini_dream_happy.png'
        attribute neutral_happy:
            'images/taida/Taida_mini_neutral_happy.png'
        attribute sad:
            'images/taida/Taida_mini_sad.png'
        attribute sad_angry:
            'images/taida/Taida_mini_sad_angry.png'
        attribute surprised:
            'images/taida/Taida_mini_surprised.png'
        attribute tricky:
            'images/taida/Taida_mini_tricky.png'

    group emotion if_any "idle":
        attribute idle default:
            'images/taida/Taida_mini_neutral.png'
        attribute thinking_smile:
            'images/taida/Taida_mini_thinking_smile.png'
        attribute angry:
            'images/taida/Taida_mini_angry.png'
        attribute asharashen:
            'images/taida/Taida_mini_asharashen.png'
        attribute dream:
            'images/taida/Taida_mini_dream.png'
        attribute crazy:
            'images/taida/Taida_mini_crazy.png'
        attribute cry:
            'images/taida/Taida_mini_cry.png'
        attribute depressed:
            'images/taida/Taida_mini_depressed.png'
        attribute thinking:
            'images/taida/Taida_mini_dream.png'
        attribute fear:
            'images/taida/Taida_mini_fear.png'
        attribute dream_happy:
            'images/taida/Taida_mini_dream_happy.png'
        attribute neutral_happy:
            'images/taida/Taida_mini_neutral_happy.png'
        attribute sad:
            'images/taida/Taida_mini_sad.png'
        attribute sad_angry:
            'images/taida/Taida_mini_sad_angry.png'
        attribute surprised:
            'images/taida/Taida_mini_surprised.png'
        attribute tricky:
            'images/taida/Taida_mini_tricky.png'

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('t', 'taida_talk_idle', Null())
        attribute talk if_any "thinking":
            WhileSpeaking('t', 'taida_talk_thinking', Null())
        attribute talk if_any "asharashen":
            WhileSpeaking('t', 'taida_talk_asharashen', Null())

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

#region Taida full
layeredimage t_f:
    group pose:
        attribute ear default:
            Null()
        attribute thinking:
            Null()
        attribute hz:
            Null()

    group emotion if_any "ear":
        attribute neutral default: #нейтральный
            'images/taida/Taida_pose3_neutral.png'
        attribute cry: #плачет
            'images/taida/Taida_pose3_cry.png'
        attribute dream: #мечтательный
            'images/taida/Taida_pose3_dream.png'
        attribute surprised: #удивлен
            'images/taida/Taida_pose3_surprised.png'
        attribute sad_angry: #грусть + злость
            'images/taida/Taida_pose3_sad_angry.png'
        attribute angry: #злость
            'images/taida/Taida_pose3_angry.png'
        attribute sad: #печальный
            'images/taida/Taida_pose3_sad.png'
        attribute fear: #испуганный
            'images/taida/Taida_pose3_fear.png'
        attribute crazy: #безумие
            'images/taida/Taida_pose3_crazy.png'
        attribute happy: #счастливый
            'images/taida/Taida_pose3_happy.png'
        attribute tricky: #хитрость
            'images/taida/Taida_pose3_tricky.png'
        attribute neutral_happy: #нейтральный счастливый
            'images/taida/Taida_pose3_neutral_happy.png'
        attribute thinking: #думаю
            'images/taida/Taida_pose3_thinking.png'
        attribute asharashen: #ашарашен
            'images/taida/Taida_pose3_asharasen.png'
        attribute calm: #спокойный
            'images/taida/Taida_pose3_calm.png'
        attribute depressed: #депрессивный
            'images/taida/Taida_pose3_depressed.png'

    group emotion if_any "thinking":
        attribute neutral default: #нейтральный
            'images/taida/Taida_pose2_neutral.png'
        attribute cunning: #хитрый
            'images/taida/Taida_pose2_cunning.png'
        attribute neutral_4stena: #4 стена нейтральный
            'images/taida/Taida_pose2_neutral_4stena.png'
        attribute asharashen: #ашарашен
            'images/taida/Taida_pose2_osharashen.png'
        attribute genius: #гений
            'images/taida/Taida_pose2_shine_genious.png'
        attribute sleepy: #сонный
            'images/taida/Taida_pose2_sleepy.png'
        attribute thinking: #думает
            'images/taida/Taida_pose2_thinking.png'
        attribute thinking_hard: #сильно думает
            'images/taida/Taida_pose2_thinking_sad.png'
        attribute tired: #устал
            'images/taida/Taida_pose2_tired.png'

    group emotion if_any "hz":
        attribute neutral default: #нейтральный
            'images/taida/Taida_pose1_neutral.png'
        attribute cry_4stena: #плачет 4 стена
            'images/taida/Taida_pose1_cry_4stena.png'
        attribute cry_sad: #плачет подавленно
            'images/taida/Taida_pose1_cry_sad.png'
        attribute cry_why: #плачет вопросительно
            'images/taida/Taida_pose1_cry_why.png'
        attribute happy: #счастлив
            'images/taida/Taida_pose1_happy.png'
        attribute smile: #улыбается
            'images/taida/Taida_pose1_hz.png'
        attribute dissatisfied: #недоволен
            'images/taida/Taida_pose1_nedovolen.png'
        attribute neutral_4stena: #нейтральный 4 стена
            'images/taida/Taida_pose1_neutral_4stena.png'
        attribute glad: #радуется
            'images/taida/Taida_pose1_neutral_happy.png'
        attribute wtf: #wtf
            'images/taida/Taida_pose1_wtf.png'


    group mouth if_any "ear":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_ear', Null())
    
    group mouth if_any "thinking":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_thinking', Null())

    group mouth if_any "hz":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_hz', Null())

    group dress if_any "ear":
        attribute school default:
            Null()
        attribute summer_norm:
            "images/taida/.png"
        attribute summer_strem:
            "images/taida/.png"  

    group dress if_any "thinking":
        attribute school default:
            "images/taida/Taida_pose2_shkolnoe.png"
        attribute summer_norm:
            "images/taida/Taida_pose2_norm.png"
        attribute summer_strem:
            "images/taida/Taida_pose2_strem.png"            

    group dress if_any "hz":
        attribute school default:
            "images/taida/Taida_pose1_shkolnoe"
        attribute summer_norm:
            "images/taida/Taida_pose1_norm.png"
        attribute summer_strem:
            "images/taida/Taida_pose1_strem.png"  

image taida_talk_ear:
    'images/taida/Taida_pose3_rot1.png'
    pause 0.1
    'images/taida/Taida_pose3_rot2.png'
    pause 0.1
    'images/taida/Taida_pose3_rot3.png'
    repeat

image taida_talk_thinking:
    'images/taida/Taida_pose2_rot1.png'
    pause 0.1
    'images/taida/Taida_pose2_rot2.png'
    pause 0.1
    'images/taida/Taida_pose2_rot3.png'
    repeat

image taida_talk_hz:
    'images/taida/Taida_pose1_rot1.png'
    pause 0.1
    'images/taida/Taida_pose1_rot2.png'
    pause 0.1
    'images/taida/Taida_pose1_rot3.png'
    repeat
#endregion

#region Dzinzo

image side d = LayeredImageProxy("d", Transform(crop=(0, 0, 600, 460), xoffset=-80))

layeredimage d:
    group pose:
        attribute pose1 default:
            Null()
        attribute pose2:
            Null()

    group emotion if_any "pose1":
        attribute neutral default:
            "images/Dindzo/Dzindzo_pose1_neutral.png"
        attribute happy:
            "images/Dindzo/Dzindzo_pose1_happy.png"
        attribute very_happy:
            "images/Dindzo/Dzindzo_pose1_very_happy.png"
        attribute surprised:
            "images/Dindzo/Dzindzo_pose1_surprised.png"
        attribute thinking:
            "images/Dindzo/Dzindzo_pose1_thinking.png"
        attribute cunning:
            "images/Dindzo/Dzindzo_pose1_cunning.png"
        attribute relief:
            "images/Dindzo/Dzindzo_pose1_relief.png"
    
    group emotion if_any "pose2":
        attribute neutral default:
            "images/Dindzo/Dzindzo_pose2_neutral.png"
        attribute sad:
            "images/Dindzo/Dzindzo_pose2_sad.png"
        attribute melancholy:
            "images/Dindzo/Dzindzo_pose2_melancholy.png"
        attribute osharashen:
            "images/Dindzo/Dzindzo_pose2_osharashen.png"
        attribute pupupu:
            "images/Dindzo/Dzindzo_pose2_pupupu.png"

    group mouth if_any "pose1":
        attribute talk:
            WhileSpeaking('d', 'dzinzo_talk_pose1', Null())
    
    group mouth if_any "pose2":
        attribute talk:
            WhileSpeaking('d', 'dzinzo_talk_pose2', Null())

    group dress if_any "pose1":
        attribute school default:
            "images/Dindzo/Dzindzo_pose1_shkolnoe.png"
        attribute summer:
            "images/Dindzo/Dzindzo_pose1_letnee.png"
    
    group dress if_any "pose2":
        attribute school default:
            "images/Dindzo/Dzindzo_pose2_shkolnoe.png"
        attribute summer:
            "images/Dindzo/Dzindzo_pose2_letnee.png"

image dzinzo_talk_pose1:
    "images/Dindzo/Dzindzo_pose1_rot1.png"
    pause 0.1
    "images/Dindzo/Dzindzo_pose1_rot2.png"
    pause 0.1
    "images/Dindzo/Dzindzo_pose1_rot3.png"
    repeat

image dzinzo_talk_pose2:
    "images/Dindzo/Dzindzo_pose2_rot1.png"
    pause 0.1
    "images/Dindzo/Dzindzo_pose2_rot2.png"
    pause 0.1
    "images/Dindzo/Dzindzo_pose2_rot3.png"
    repeat

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

#region Katsumi
layeredimage k:
    group pose:
        attribute pose1 default:
            Null()
        attribute pose2:
            Null()

    group emotion if_any "pose1":
        attribute neutral default:
            "images/Katsumi/Katsumi_pose1_neutral.png"
        attribute happy:
            "images/Katsumi/Katsumi_pose1_happy.png"
        attribute concerned:
            "images/Katsumi/Katsumi_pose1_concerned.png"
        attribute confused:
            "images/Katsumi/Katsumi_pose1_confused.png"
        attribute irritated:
            "images/Katsumi/Katsumi_pose1_irritated.png"
        attribute cunning:
            "images/Katsumi/Katsumi_pose1_cunning.png"
        attribute neutral_4stena:
            "images/Katsumi/Katsumi_pose1_neutral_4stena.png"
    
    group emotion if_any "pose2":
        attribute neutral default:
            "images/Katsumi/Katsumi_pose2_neutral.png"
        attribute annoyed:
            "images/Katsumi/Katsumi_pose2_annoyed.png"
        attribute cunning:
            "images/Katsumi/Katsumi_pose2_cunning.png"
        attribute asharashen:
            "images/Katsumi/Katsumi_pose2_ashrashen.png"
        attribute didnt_understand:
            "images/Katsumi/Katsumi_pose2_didnt_understand.png"
        attribute self_confident:
            "images/Katsumi/Katsumi_pose2_self_confident.png"
        attribute neutral_4stena:
            "images/Katsumi/Katsumi_pose2_neutral_4stena.png"

    group mouth if_any "pose1":
        attribute talk:
            WhileSpeaking('k', 'katsumi_talk_pose1', Null())
    
    group mouth if_any "pose2":
        attribute talk:
            WhileSpeaking('k', 'katsumi_talk_pose2', Null())

image katsumi_talk_pose1:
    "images/Katsumi/Katsumi_pose1_rot1.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose1_rot2.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose1_rot3.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose1_rot4.png"
    repeat

image katsumi_talk_pose2:
    "images/Katsumi/Katsumi_pose2_rot1.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose2_rot2.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose2_rot3.png"
    pause 0.1
    "images/Katsumi/Katsumi_pose2_rot4.png"
    repeat

#endregion

#region Hikaru
layeredimage h:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Hikaru/neutral.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('h', 'h_talk_idle', Null())
"""
image mom_talk_idle:
    "images/mom/Mom_rot_1.png"
    pause 0.1
    "images/mom/Mom_rot_2.png"
    pause 0.1
    "images/mom/Mom_rot_3.png"
    repeat
"""
#endregion

#region Den
layeredimage den:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Den/neutral.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('den', 'den_talk_idle', Null())
"""
image mom_talk_idle:
    "images/mom/Mom_rot_1.png"
    pause 0.1
    "images/mom/Mom_rot_2.png"
    pause 0.1
    "images/mom/Mom_rot_3.png"
    repeat
"""
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

#region Teacher
layeredimage teacher:
    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Teacher/normal.png"
        attribute serious:
            "images/Teacher/brow.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('teacher', 'teacher_talk_idle', Null())
"""
image mom_talk_idle:
    "images/mom/Mom_rot_1.png"
    pause 0.1
    "images/mom/Mom_rot_2.png"
    pause 0.1
    "images/mom/Mom_rot_3.png"
    repeat
"""
#endregion