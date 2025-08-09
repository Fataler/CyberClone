image umi_cg = "images/CG/CG_Umi_gym_2.png"
image bg_cg = "images/CG/CG_Umi_gym.png"

style continue_style is gui_text

label umi_cg_scene:

    scene bg_robo_class_room
    with dissolve
    show bg_cg at g_appear(0.5)
    pause 0.5

    show umi_cg at g_appear(0.5, 0.3)
    pause 0.5
    show umi_cg with hpunch
    pause 5

    t_t "Перед нами открылась картина лежащей на полу девушки и подноса с разбитыми чашками. "

    hide bg_cg
    hide umi_cg
    with dissolve

    return