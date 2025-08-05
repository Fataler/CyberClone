transform ybeat(amplitude=30, period=0.54, hit=0.08):
    yoffset 0
    linear hit yoffset amplitude
    linear hit yoffset 0
    pause period - hit*2
    repeat

transform xbeat(amplitude=30, period=0.54, hit=0.08):
    xoffset 0
    linear hit xoffset amplitude
    linear hit xoffset 0
    pause period - hit*2
    repeat

image assembling_bg = "images/CG RGG/bg.png"

transform blink:
    alpha 0
    linear 0.5 alpha 1
    pause 1
    linear 0.5 alpha 0
    repeat

image a_1_stars:
    "images/CG RGG/cg1 c.png"
    

image a_border:
    "images/CG RGG/border.png"
    anchor (0.5, 0.5)
    pos(0.5, 0.5)
    zoom 1.05

layeredimage a_4:
    always:
        "images/CG RGG/cg1 a.png"
    always:
        at ybeat()
        "images/CG RGG/cg1 b.png"
    always:
        at blink()
        "a_1_stars"
    always:
        
        at ybeat()
        "a_border"

layeredimage a_1:
    always:
        "images/CG RGG/cg2 a.png"
    always:
        "images/CG RGG/cg2 b.png"
    always:
        at ybeat()
        "images/CG RGG/cg2 c.png"
    always:
        at blink
        "images/CG RGG/cg2 d.png"
    always:
        at ybeat()
        "a_border"

layeredimage a_6:
    
        
    at ybeat()
    always:
        image:
            "images/CG RGG/cg3 c.png"
            pause 0.54
            "images/CG RGG/cg3 a.png"
            pause 0.54
            "images/CG RGG/cg3 b.png"
            pause 0.54
            repeat
    always:
        "images/CG RGG/cg3 d.png"
    always:
        "images/CG RGG/cg3 e.png"
    always:
        "images/CG RGG/cg3 f.png"
    always:
        "images/CG RGG/cg3 g.png"
    always:
        "images/CG RGG/cg3 h.png"
    always:
        
        at ybeat()
        "a_border"

layeredimage a_2:
    always:
        at ybeat()
        "images/CG RGG/cg4 a.png"
    always:
        "images/CG RGG/cg4 b.png"
    always:
        at blink
        "images/CG RGG/cg4 c.png"
    always:
        
        at ybeat()
        "a_border"

layeredimage a_3:
    always:
        "images/CG RGG/cg5 a.png"
    always:
    
        at ybeat()
        "images/CG RGG/cg5 b.png"
    always:
        at blink
        "images/CG RGG/cg5 c.png"
    always:
        
        at ybeat()
        "a_border"

layeredimage a_5:
    always:
        
        at ybeat()
        "images/CG RGG/cg6 a.png"
    always:
        at blink
        "images/CG RGG/cg6 b.png"
    always:
        at ybeat()
        "a_border"

transform slide_from_right_top:
    anchor (0.5, 0.5)
    size (960, 540)
    xpos 1.5
    ypos 0.3
    ease 2.0 xpos 0.5

transform slide_from_right_bottom:
    anchor (0.5, 0.5)
    size (960, 540)
    xpos 1.5
    ypos 0.5
    ease 2.0 xpos 0.5

transform slide_from_left_center:
    anchor (0.5, 0.5)
    size (960, 540)
    xpos 1.5
    ypos 0.5
    ease 2.0 xpos 0.5

transform slide_to_left:
    ease 2.0 xpos -0.5

label assembling_scene:
    play music music_assembling fadein 0.5 fadeout 0.5
    scene assembling_bg
    with dissolve
    
    show a_1 at slide_from_right_top
    with None
    pause 2.5
    
    "Искуственный интеллект натренирован на 96\%."
    
    show a_2 at slide_from_right_bottom
    show a_1 at slide_to_left
    with None
    pause 2.5
    
    hide a_1
    
    "Материнская плата успешно сконфигурирована."
    
    show a_3 at slide_from_right_top
    show a_2 at slide_to_left
    with None
    pause 2.5
    
    hide a_2
    
    "Рассчеты завершены. Погрешность 0.005\%."

    show a_4 at slide_from_right_bottom
    show a_3 at slide_to_left
    with None
    pause 2.5
    
    hide a_3
    
    "Чай разогрет! Печеньки поданы!\n (А также, изучена вся доступная информация из городской библиотеки по сборке шарнирных прототипов.)"
    
    show a_5 at slide_from_right_top
    show a_4 at slide_to_left
    with None
    pause 2.5
    
    hide a_4
    
    "{size=180}IT'S ALIVE!!!"
    
    show a_6 at slide_from_left_center
    show a_5 at slide_to_left
    with None
    pause 5
    
    hide a_5

    show a_6 at slide_to_left
    with None

    pause 1.5
    
    scene bg_black
    with dissolve

    stop music
    
    return