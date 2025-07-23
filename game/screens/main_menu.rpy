## Экран главного меню
init:
    image bg_white = Solid("#ffffff")
    image menu_background_image:
        "gui/menu_bg.png"
        anchor (0.5, 0.5)
        xsize 1.10
        ysize 1.10
    image menu_tower_image:
        "gui/menu_tower.png"
        anchor (0.5, 0.5)
        xsize 1.25
        ysize 1.25
    image menu_clouds_image:
        "gui/menu_clouds.png"
        anchor (0.5, 0.5)
        xsize 1.35
        ysize 1.35

screen main_menu():
    on "show" action Function(renpy.play, sfx_chains, channel="sfx")
    on "replace" action Function(renpy.play, sfx_chains, channel="sfx")

    tag menu

    #add Parallax("menu_background_image", 3)
    add "bg_menu_main"
    #add Parallax("menu_clouds_image", 15)

    add Parallax("gui/menu/logo.png", 0.2):
        anchor (0.5, 0.5)
        xpos 423
        ypos 340
        

    add Parallax("gui/menu/guys_shadow.png", 0.8):
        anchor (0.5, 0.5)
        xpos 1191
        ypos 682

    add Parallax("gui/menu/guys.png", 0.3):
        anchor (0.5, 0.5)
        xpos 1131
        ypos 680

    imagebutton:
        idle Transform("avatar_circle", size=(160, 160))
        action OpenURL('https://t.me/viendesu_official')
        anchor (0.5, 0.5)
        xpos 0.09
        ypos 0.87
        at hover_scale

    #vbox at menu_items_appear:
    style_prefix "main_menu"

    #spacing gui.navigation_spacing
    
    textbutton _("Начать") action Start():
        xpos 1171
        ypos 281
        text_size 93

    textbutton _("Загрузить") action ShowMenu("load"):
        xpos 640
        ypos 610
        text_size 59

        
    
    textbutton _("Достижения") action ShowMenu("achievements_screen"):
        xpos 500
        ypos 851
        text_size 59

    textbutton _("Настройки") action ShowMenu("preferences"):
        xpos 1636
        ypos 481
        text_size 59

    textbutton _("Об игре") action [Function(unlock_achievement, THANK_YOU),ShowMenu("about")]:
        xpos 1655
        ypos 797
        text_size 59

    if renpy.variant("pc"):
        textbutton _("Выход") action Quit(confirm=not main_menu):
            xpos 440
            ypos 999
            text_size 50

    if show_main_menu_fade:
        add "bg_white" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

style main_menu_button:
    #size_group "navigation"
    anchor (0.5, 0.5)
    properties gui.button_properties("main_menu")
    #xminimum 400
    #xalign 0.5

style main_menu_button_text is gui_button_text

style main_menu_button_text:
    properties gui.text_properties("main_menu")
    color gui.interface_text_color
    hover_color gui.hover_color
    size 80
    xalign 0.5
    font gui.interface_text_font

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")

transform hover_scale:
    anchor (0.5, 0.5)
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1

transform menu_alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform alpha_in(time=0.5):
    alpha 0
    linear time alpha 1

transform alpha_out(time=0.5):
    alpha 1
    linear time alpha 0
