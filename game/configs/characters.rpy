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
define t = Character('Тайда', color='#05681b', image='t', callback=speaker('t_f'))

define t_f = Character('Тайда', color='#05681b', image='t_f', callback=speaker('t_f'))

define t_t = Character(None, color='#05681b', image='t')
                        
define d = Character('Дзиндзо', color='#2d0231', image='d', callback=speaker('d'))

define d_t = Character(None, color='#2d0231', image='d')

define d_f = Character('Дзиндзо', color='#2d0231', image='d_f', callback=speaker('d_f'))

define u = Character('Юми', color='#681744', image='u', callback=speaker('u'))

define k = Character('Кацуми', color='#171658', image='k', callback=speaker('k'))

define h = Character('Хикару', color='#66161a', image='h', callback=speaker('h'))

define den = Character('Ден', color='#7e7719', image='den', callback=speaker('den'))

define i = Character('Изуми-сенсей', color='#01565c', image='i', callback=speaker('i'))

define dad = Character('Папа', color='#21202c', image='dad', callback=speaker('dad'))

define mom = Character('Мама', color='#23301f', image='mom', callback=speaker('mom'))

define teacher = Character('Учитель', color='#726351', image='teacher', callback=speaker('teacher'))

define seller = Character('Продавщица', color='#964a04', image='seller', callback=speaker('seller'))

define stranger = Character('Одноклассник', color='#6b3b0f')

define b_1 = Character('Отец Юми', color='#21202c', image='umi_dad', callback=speaker('umi_dad'))

define b_2 = Character('Батя', color='#21202c', image='umi_dad', callback=speaker('umi_dad'))

define together = Character('Все', color='#420303')

define story_teller = Character(None, kind=nvl, color="#1a1a1f")
#endregion

#region Taida

image side t = LayeredImageProxy("t_f", Transform(crop=(0, 0, 600, 460), xoffset=0))

layeredimage t_f:
    at auto_flip("t_f")

    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute ear: #pose3
            Null()
        attribute ear_school default: #pose3_school
            Null()
        attribute thinking: #pose2
            Null()
        attribute hz: #pose1
            Null()

    group emotion if_any "ear":
        attribute neutral default: #нейтральный
            'images/taida/Taida_pose3_neutral.png'
        attribute careless: #беззаботный
            'images/taida/Taida_pose3_careless.png'
        attribute cute: #милый
            'images/taida/Taida_pose3_cute.png'
        attribute shy: #shy
            'images/taida/Taida_pose3_cute_cry.png'
        attribute embarrassed: #smushen
            'images/taida/Taida_pose3_embarrassed.png'
        attribute happy:
            'images/taida/Taida_pose3_neposredstvenniy.png'
        attribute neutral_4stena:
            'images/taida/Taida_pose3_Neutral_4stena.png'
        attribute silly:
            'images/taida/Taida_pose3_neutral_silly.png'
        attribute confused:
            'images/taida/Taida_pose3_oooops.png'
        attribute surprised:
            'images/taida/Taida_pose3_surprised.png'

    group emotion if_any "ear_school":
        attribute neutral default: #нейтральный
            'images/taida/Taida_pose3_shkolnoe_neutral.png'
        attribute cry: #плачет
            'images/taida/Taida_pose3_shkolnoe_cry.png'
        attribute dream: #мечтательный
            'images/taida/Taida_pose3_shkolnoe_dream.png'
        attribute surprised: #удивлен
            'images/taida/Taida_pose3_shkolnoe_surprised.png'
        attribute angry: #грусть + злость
            'images/taida/Taida_pose3_shkolnoe_sad_angry.png'
        attribute cry_angry: #злость
            'images/taida/Taida_pose3_shkolnoe_angry.png'
        attribute sad: #печальный
            'images/taida/Taida_pose3_shkolnoe_sad.png'
        attribute fear: #испуганный
            'images/taida/Taida_pose3_shkolnoe_fear.png'
        attribute crazy: #безумие
            'images/taida/Taida_pose3_shkolnoe_crazy.png'
        attribute happy: #счастливый
            'images/taida/Taida_pose3_shkolnoe_happy.png'
        attribute tricky: #хитрость
            'images/taida/Taida_pose3_shkolnoe_tricky.png'
        attribute smile: #нейтральный счастливый
            'images/taida/Taida_pose3_shkolnoe_neutral_happy.png'
        attribute think: #думаю
            'images/taida/Taida_pose3_shkolnoe_thinking.png'
        attribute asharashen: #ашарашен
            'images/taida/Taida_pose3_shkolnoe_asharashen.png'
        attribute calm: #спокойный
            'images/taida/Taida_pose3_shkolnoe_calm.png'
        attribute depressed: #депрессивный
            'images/taida/Taida_pose3_shkolnoe_depressed.png'

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
        attribute think: #думает
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

    group dress if_any "ear":
        attribute school default:
            Null()
        attribute summer_norm:
            "images/taida/Taida_pose3_norm.png"
        attribute summer_strem:
            "images/taida/Taida_pose3_strem.png"  

    group dress if_any "ear_school":
        attribute school default:
            Null()

    group dress if_any "thinking":
        attribute school default:
            "images/taida/Taida_pose2_shkolnoe.png"
        attribute summer_norm:
            "images/taida/Taida_pose2_norm.png"
        attribute summer_strem:
            "images/taida/Taida_pose2_strem.png"
        attribute naked:
            Null()

    group dress if_any "hz":
        attribute school  default:
            "images/taida/Taida_pose1_shkolnoe.png"
        attribute summer_norm:
            "images/taida/Taida_pose1_norm.png"
        attribute summer_strem:
            "images/taida/Taida_pose1_strem.png"
        attribute naked:
            Null()

    group mouth if_any "ear":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_ear', Null())
    
    group mouth if_any "ear_school":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_ear_school', Null())
    
    group mouth if_any "thinking":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_thinking', Null())

    group mouth if_any "hz":
        attribute talk:
            WhileSpeaking('t_f', 'taida_talk_hz', Null())

    group effects if_any "genius":
        attribute stars:
            "taida_stars"

image taida_talk_ear:
    'images/taida/Taida_pose3_rot1.png'
    pause 0.1
    'images/taida/Taida_pose3_rot2.png'
    pause 0.1
    'images/taida/Taida_pose3_rot3.png'
    repeat

image taida_talk_ear_school:
    'images/taida/Taida_pose3_ear_school_rot1.png'
    pause 0.1
    'images/taida/Taida_pose3_ear_school_rot2.png'
    pause 0.1
    'images/taida/Taida_pose3_ear_school_rot3.png'
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

image taida_stars:
    'images/taida/Taida_pose2_shine_genious_star1.png'
    pause 0.4
    'images/taida/Taida_pose2_shine_genious_star2.png'
    pause 0.4
    'images/taida/Taida_pose2_shine_genious_star3.png'
    pause 0.4
    'images/taida/Taida_pose2_shine_genious_star2.png'
    pause 0.4
    repeat

#endregion

#region Dzinzo

image side d = LayeredImageProxy("d_f", Transform(crop=(0, 0, 700, 460), xoffset=-80))

layeredimage d_f:
    at auto_flip("d_f")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()
    
    group pose:
        attribute pose1 default:
            Null()
        attribute pose2:
            Null()
        attribute pose3:
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
        attribute asharashen:
            "images/Dindzo/Dzindzo_pose2_osharashen.png"
        attribute pupupu:
            "images/Dindzo/Dzindzo_pose2_pupupu.png"

    group emotion if_any "pose3":
        attribute neutral default:
            "images/Dindzo/Dzindzo_bez_prikolov_thinking.png"
        attribute smile:
            "images/Dindzo/Dzindzo_bez_prikolov_neutral.png"

    group mouth if_any "pose1":
        attribute talk:
            WhileSpeaking('d', 'dzinzo_talk_pose1', Null())
    
    group mouth if_any "pose2":
        attribute talk:
            WhileSpeaking('d', 'dzinzo_talk_pose2', Null())

    group mouth if_any "pose3":
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
    at auto_flip("u")
    yoffset 1
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

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
        attribute happy:
            "images/Umi/Umi_pose1_laught.png"
        attribute happy_4stena:
            "images/Umi/Umi_pose1_laught_4stena.png"
        attribute surprised:
            "images/Umi/Umi_pose1_surprised.png"
        attribute thinking:
            "images/Umi/Umi_pose1_thinking.png"
    
    group emotion if_any "closed":
        attribute neutral default:
            "images/Umi/Umi_pose2_alluring.png"
        attribute cute:
            "images/Umi/Umi_pose2_confused.png"
        attribute cry_2:
            "images/Umi/Umi_pose2_cry.png"
        attribute asharashen:
            "images/Umi/Umi_pose2_cry_asharashen.png"
        attribute cry:
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
        attribute sad:
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
    at auto_flip("k")

    group direction:
        attribute right:
            Null()
        attribute left default:
            Null()

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
        attribute worried:
            "images/Katsumi/Katsumi_pose1_concerned.png"
        attribute confused:
            "images/Katsumi/Katsumi_pose1_confused.png"
        attribute angry:
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
        attribute smug:
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
    at auto_flip("h")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute idle default:
            Null()
        attribute explain:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Hikaru/hikaru_handonhand_neutral.png"
        attribute angry:
            "images/Hikaru/hikaru_handonhand_besit.png"
        attribute cunning:
            "images/Hikaru/hikaru_handonhand_cunning.png"
        attribute shy:
            "images/Hikaru/hikaru_handonhand_cute.png"
        attribute happy:
            "images/Hikaru/hikaru_handonhand_happy.png"
        attribute smile:
            "images/Hikaru/hikaru_handonhand_neutral_happy.png"
        attribute surprised:
            "images/Hikaru/hikaru_handonhand_oooops.png"
        attribute smug:
            "images/Hikaru/hikaru_handonhand_samodovolen.png"

    group emotion if_any "explain":
        attribute neutral default:
            "images/Hikaru/Hikaru_explains_nedovolen.png"
        attribute neutral_talk:
            "images/Hikaru/Hikaru_explains_nedovolen_ochen.png"
        attribute asharashen:
            "images/Hikaru/Hikaru_explains_osharashen.png"
        attribute sad:
            "images/Hikaru/Hikaru_explains_rasstroen.png"
        attribute surprised:
            "images/Hikaru/Hikaru_explains_surprised.png"
        attribute thinking:
            "images/Hikaru/Hikaru_explains_thinking.png"


    group dress if_any "idle":
        attribute school default:
            "images/Hikaru/hikaru_handonhand_shkolnoe.png"
        attribute summer:
            "images/Hikaru/hikaru_handonhand_letnee.png"
        
    group dress if_any "explain":
        attribute school default:
            "images/Hikaru/Hikaru_explains_shkolnoe.png"
        attribute summer:
            "images/Hikaru/Hikaru_explains_letnee.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('h', 'h_talk_idle', Null())
        attribute talk if_any "explain":
            WhileSpeaking('h', 'h_talk_explain', Null())

image h_talk_idle:
    "images/Hikaru/hikaru_handonhand_rot1.png"
    pause 0.1
    "images/Hikaru/hikaru_handonhand_rot2.png"
    pause 0.1
    "images/Hikaru/hikaru_handonhand_rot3.png"
    repeat

image h_talk_explain:
    "images/Hikaru/Hikaru_explains_rot1.png"
    pause 0.1
    "images/Hikaru/Hikaru_explains_rot2.png"
    pause 0.1
    "images/Hikaru/Hikaru_explains_rot3.png"
    repeat

#endregion

#region Den
layeredimage den:
    at auto_flip("den")
    yoffset 1
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute idle default:
            Null()
        attribute awesome:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Den/Den_achovsmisle_neutral.png"
        attribute cry:
            "images/Den/Den_achovsmisle_cry.png"
        attribute sad:
            "images/Den/Den_achovsmisle_neutral_sad.png"
        attribute nervous:
            "images/Den/Den_achovsmisle_ooooops.png"
        attribute asharashen:
            "images/Den/Den_achovsmisle_osharashen.png"

    group emotion if_any "awesome":
        attribute neutral default:
            "images/Den/Den_krutoi_neutral.png"
        attribute happy:
            "images/Den/Den_krutoi_happy.png"
        attribute tricky:
            "images/Den/Den_krutoi_pervert.png"
        attribute surprised:
            "images/Den/Den_krutoi_pupupu.png"
        attribute sad:
            "images/Den/Den_krutoi_sad.png"
        attribute shy:
            "images/Den/Den_krutoi_shy.png"
        attribute wink:
            "images/Den/Den_krutoi_wink.png"

    group dress if_all("idle", "right"):
        attribute school default:
            "images/Den/Den_achovsmisle_shkolnoe.png"
        attribute summer:
            "images/Den/Den_achovsmisle_letnee_vpravo.png"

    group dress if_all("idle", "left"):
        attribute school default:
            "images/Den/Den_achovsmisle_shkolnoe.png"
        attribute summer:
            Transform("images/Den/Den_achovsmisle_letnee_vlevo.png", xzoom=-1, xoffset=-110)
        
    group dress if_all("awesome", "right"):
        attribute school default:
            "images/Den/Den_krutoi_shkolnoe.png"
        attribute summer:
            "images/Den/Den_krutoi_letnee_vpravo.png"

    group dress if_all("awesome", "left"):
        attribute school default:
            "images/Den/Den_krutoi_shkolnoe.png"
        attribute summer:
            Transform("images/Den/Den_krutoi_letnee_vlevo.png", xzoom=-1, xoffset=10)

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('den', 'den_talk_idle', Null())
        attribute talk if_any "awesome":
            WhileSpeaking('den', 'den_talk_awesome', Null())

image den_talk_idle:
    "images/Den/Den_achovsmisle_rot1.png"
    pause 0.1
    "images/Den/Den_achovsmisle_rot2.png"
    pause 0.1
    "images/Den/Den_achovsmisle_rot3.png"
    repeat

image den_talk_awesome:
    "images/Den/Den_krutoi_rot1.png"
    pause 0.1
    "images/Den/Den_krutoi_rot2.png"
    pause 0.1
    "images/Den/Den_krutoi_rot3.png"
    repeat

#endregion

#region Dad
layeredimage dad:
    at auto_flip("dad")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

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
    at auto_flip("mom")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

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
    at auto_flip("i")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute intersted:
            "images/Izumi/Izumi_neutral.png"
        attribute angry:
            "images/Izumi/Izumi_angry.png"
        attribute asharashen:
            "images/Izumi/Izumi_asharasen.png"
        attribute calm:
            "images/Izumi/Izumi_calm.png"
        attribute dreamy:
            "images/Izumi/Izumi_dreamy.png"
        attribute neutral default:
            "images/Izumi/Izumi_interested.png"
        attribute neutral_2:
            "images/Izumi/Izumi_neutral_2.png"
        attribute happy:
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
    at auto_flip("teacher")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/Teacher/Teacher_neutral.png"
        attribute angry:
            "images/Teacher/Teacher_angry.png"
        attribute smile:
            "images/Teacher/Teacher_neutral_happy.png"
        attribute surprised:
            "images/Teacher/Teacher_surprised.png"
        attribute happy:
            "images/Teacher/Teacher_sus_happy.png"
        attribute sad:
            "images/Teacher/Teacher_vzdoh.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('teacher', 'teacher_talk_idle', Null())

image teacher_talk_idle:
    "images/teacher/Teacher_rot1.png"
    pause 0.1
    "images/teacher/Teacher_rot2.png"
    pause 0.1
    "images/teacher/Teacher_rot3.png"
    repeat

#endregion

#region Seller
layeredimage seller:
    at auto_flip("seller")
    
    group direction:
        attribute right default:
            Null()
        attribute left:
            Null()

    group pose:
        attribute idle default:
            Null()

    group emotion if_any "idle":
        attribute neutral default:
            "images/TraderKalmar/TraderKalmar.png"

    group mouth:
        attribute talk if_any "idle":
            WhileSpeaking('seller', 'seller_talk_idle', Null())

image seller_talk_idle:
    "images/TraderKalmar/TraderKalmar_rot1.png"
    pause 0.1
    "images/TraderKalmar/TraderKalmar_rot2.png"
    pause 0.1
    "images/TraderKalmar/TraderKalmar_rot3.png"
    repeat

#endregion