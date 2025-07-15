transform profile_slide_in:
    yoffset 100
    alpha 0.0
    ease 0.8 yoffset 0 alpha 1.0

transform card_appear:
    zoom 0.8
    alpha 0.0
    ease 1.0 zoom 1.0 alpha 1.0

transform avatar_spin:
    rotate 0
    ease 2.0 rotate 360

transform stat_grow:
    xzoom 0.0
    ease 1.5 xzoom 1.0

define ICONS = {
    "Интересы": "🎯",
    "Хобби": "⚡", 
    "Не любит": "❌",
    "Любимый предмет": "📚",
    "Характер": "🎭",
    "Навыки": "⭐"
}

screen student_profile(character_name="Ученик", character_description="Описание персонажа", character_sprite="#FF6B6B", character_stats=None):
    tag profile
    modal True
    
    add "#1a1a2e" at profile_slide_in
    
    frame:
        xysize (1920, 1080)
        background None
        
        add Solid("#16213e") alpha 0.8
    
    frame:
        pos (160, 80)
        xysize (1600, 920)
        background Frame("gui/frame.png", 20, 20)
        at card_appear
        
        add Solid("#0f4c75") alpha 0.9
        
        hbox:
            spacing 40
            xpos 40
            ypos 40
            
            vbox:
                spacing 20
                xysize (450, 840)
                
                frame:
                    xysize (400, 400)
                    background Frame("gui/frame.png", 10, 10)
                    xalign 0.5
                    
                    add Solid("#3282b8") alpha 0.3
                    
                    if isinstance(character_sprite, str) and character_sprite.startswith("#"):
                        add Solid(character_sprite) xysize (360, 360) xalign 0.5 yalign 0.5
                    else:
                        add character_sprite xysize (360, 360) xalign 0.5 yalign 0.5
                
                text character_name:
                    size 36
                    color "#ffe75e"
                    xalign 0.5
                    text_align 0.5
                    font "gui/fonts/TippytoesRegular.ttf"
                    outlines [(2, "#000000", 0, 0)]
                
                frame:
                    xysize (300, 60)
                    background "#3282b8"
                    xalign 0.5
                    
                    text "КЛАСС 7-А":
                        size 24
                        color "#ffffff"
                        xalign 0.5
                        yalign 0.5
                        font "gui/fonts/TippytoesRegular.ttf"
                
                frame:
                    xysize (400, 200)
                    background "#1e3d59"
                    
                    text character_description:
                        size 20
                        color "#ffffff"
                        text_align 0.5
                        xalign 0.5
                        yalign 0.5
                        xsize 360
                        slow_cps 30
            
            vbox:
                spacing 30
                xysize (1050, 840)
                
                frame:
                    xysize (800, 80)
                    background "#ffe75e"
                    xalign 0.5
                    
                    text "ПРОФИЛЬ УЧЕНИКА":
                        size 32
                        color "#0f4c75"
                        xalign 0.5
                        yalign 0.5
                        font "gui/fonts/TippytoesRegular.ttf"
                        outlines [(2, "#ffffff", 0, 0)]
                
                if character_stats:
                    vbox:
                        spacing 20
                        
                        for info_name, info_value in character_stats.items():
                            frame:
                                xysize (900, 70)
                                background "#1e3d59"
                                at stat_grow
                                
                                hbox:
                                    spacing 20
                                    xpos 20
                                    yalign 0.5
                                    
                                    # Иконка
                                    text ICONS.get(info_name, "📝"):
                                        size 32
                                        yalign 0.5
                                    
                                    text f"{info_name}:":
                                        size 24
                                        color "#ffe75e"
                                        xsize 200
                                        yalign 0.5
                                        font "gui/fonts/TippytoesRegular.ttf"
                                    
                                    text str(info_value):
                                        size 22
                                        color "#ffffff"
                                        yalign 0.5
                                        xsize 720
                else:
                    frame:
                        xysize (900, 300)
                        background "#1e3d59"
                        
                        vbox:
                            spacing 20
                            xalign 0.5
                            yalign 0.5
                            
                            text "Неизвестно":
                                size 32
                                color "#ffe75e"
                                xalign 0.5
                                font "gui/fonts/TippytoesRegular.ttf"
    
    frame:
        pos (800, 950)
        background "#3282b8"
        at button_fade_in
        
        button:
            xysize (320, 80)
            background None
            hover_background "#ffe75e"
            action Function(close_student_profile)
            
            text "ЗАКРЫТЬ":
                size 28
                color "#ffffff"
                hover_color "#0f4c75"
                xalign 0.5
                yalign 0.5
                font "gui/fonts/TippytoesRegular.ttf"
                outlines [(2, "#000000", 0, 0)]

transform text_slide_in:
    xoffset -500
    alpha 0.0
    ease 1.2 xoffset 0 alpha 1.0

transform sprite_slide_in:
    xoffset -300
    alpha 0.0
    ease 1.5 xoffset 0 alpha 1.0

transform data_slide_in:
    xoffset 300
    alpha 0.0
    ease 1.8 xoffset 0 alpha 1.0

transform button_fade_in:
    alpha 0.0
    ease 2.0 alpha 1.0

init python:
    def close_student_profile():
        renpy.hide_screen("student_profile")
        renpy.return_statement()

label show_student_profile(character_name="Ученик", character_description="Обычный школьник", character_sprite="#FF6B6B", character_stats=None):
    
    window hide
    
    show screen student_profile(character_name, character_description, character_sprite, character_stats) with Dissolve(0.8)
    
    pause

    hide screen student_profile with Dissolve(0.5)
    window show
    
    return

label test_student_profile:
    "Сейчас покажу стильный профиль ученика!"
    
    call show_student_profile("Костян Петров", 
        "Умный и немного замкнутый программист.",
        "#4A90E2",
        {"Характер": "Интроверт, аналитик", "Навыки": "Программирование, математика", "Интересы": "IT технологии, игры", "Не любит": "Физкультуру, толпы"})
    
    "Первый профиль показан!"
    
    return

label test_another_profile:
    "Сейчас покажу профиль спортивного ученика!"
    
    call show_student_profile("Мишаня Иванов", 
        "Лидер и капитан. Энергичный, но не очень любит учебу.",
        "#E74C3C",
        {"Характер": "Экстраверт, лидер", "Навыки": "Спорт, организация", "Интересы": "Футбол, тусовки", "Не любит": "Домашку, скуку"})
    
    "Второй профиль показан!"
    
    return 