transform light_jumping(amplitude=3, period=0.1):
    yoffset 0
    xoffset 0
    block:
        ease period yoffset -amplitude
        ease period xoffset -amplitude
        ease period yoffset -amplitude
        ease period xoffset amplitude
        ease period yoffset amplitude
        ease period xoffset amplitude
        ease period yoffset amplitude
        ease period xoffset -amplitude
        repeat

layeredimage p_1:
    always:
        at delay_appear(1.5, 1)
        "images/CG dz+u/cg1 c.png"
    always:
        at delay_appear(2, 1)
        "images/CG dz+u/cg1 b.png"
    always:
        at delay_appear(2.5, 1)
        "images/CG dz+u/cg1 a.png"
    always:
        at delay_appear(3, 1)
        "images/CG dz+u/cg1 d.png"
    always:
        at light_jumping()
        "a_border"

layeredimage p_2:
    always:
        at delay_appear(1.5)
        "images/CG dz+u/cg2 a.png"
    always:
        at delay_appear(2)
        "images/CG dz+u/cg2 b.png"  
    always:
        at delay_appear(2.5)
        "images/CG dz+u/cg2 c.png"
    always:
        at light_jumping()
        "a_border"

layeredimage p_3:
    always:
        at delay_appear(1.5)
        "images/CG dz+u/cg3 a.png"
    always:
        at delay_appear(2)
        "images/CG dz+u/cg3 b.png"
    always:
        at delay_appear(2.5)
        "images/CG dz+u/cg3 c.png"
    always:
        at light_jumping()
        "a_border"

layeredimage p_4:
    always:
        at delay_appear(1.5)
        "images/CG dz+u/cg4 a.png"
    always:
        at delay_appear(2)
        "images/CG dz+u/cg4 b.png"
    always:
        at light_jumping()
        "a_border"

label park_scene:
    play music music_amu fadeout 1.0 fadein 1.0
    
    scene paper_bg
    with dissolve
    
    show p_1 at slide_from_right_top
    with None
    pause 2.5
    
    "Текст"
    
    show p_2 at slide_from_right_bottom
    show p_1 at slide_to_left
    
    pause 2.5
    
    hide p_1 with dissolve

    "Текст"

    show p_3 at slide_from_right_top
    show p_2 at slide_to_left
    with None
    pause 2.5
    
    hide p_2 with dissolve
    
    "Текст"

    show p_4 at slide_from_right_bottom
    show p_3 at slide_to_left
    with None
    pause 2.5
    
    hide p_3
    
    "Текст"

    show p_4 at slide_to_left
    with None

    pause 1.5
    
    scene bg_black
    with dissolve

    stop music
    
    return
    
    