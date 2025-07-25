################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu():
    on "show" action Function(renpy.play, sfx_chains, channel="sfx")
    on "replace" action Function(renpy.play, sfx_chains, channel="sfx")

    modal True

    add "bg_menu_main" at menu_board_drop

    frame:
        style_prefix "pause_menu"
        background None #"#00000080"
        at menu_board_drop
        xanchor 0.5
        xpos 0.5

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            #xpos 0
            #ypos 210
            xalign 0.5
            yalign 0.5

            text "ПАУЗА" size 60 xalign 0.5 color gui.accent_color style "pause_menu_button_text"
            
            textbutton _("Сохранить") action [Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action [Hide("pause_menu"), MainMenu()]
            textbutton _("Вернуться") action Return()

style pause_menu_button is main_menu_button:
    xalign 0.5
    yalign 0.5

style pause_menu_button_text is main_menu_button_text:
    xalign 0.5
    yalign 0.5
    size 50

transform pause_menu_board_drop(start_pos = -900):
    ypos start_pos
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform pause_menu_board_hide(height = -900):
    ypos 0
    easeout 0.15 ypos -50
    easein 0.2 ypos 0
    easeout 0.5 ypos height

transform pause_menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0