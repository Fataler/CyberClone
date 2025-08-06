transform guitar_bounce:
    parallel:
        block:
            ease 0.2 yoffset -25
            ease 0.2 yoffset 0
            ease 0.15 yoffset -15
            ease 0.15 yoffset 0
            pause 0.3
            repeat
    parallel:
        block:
            ease 0.35 xoffset -10
            ease 0.35 xoffset 10
            repeat

transform guitar_sway:
    parallel:
        block:
            ease 1.0 xoffset -20
            ease 1.0 xoffset 20
            repeat
    parallel:
        block:
            ease 0.5 yoffset -8
            ease 0.5 yoffset 0
            repeat
    parallel:
        block:
            ease 1.5 rotate 2
            ease 1.5 rotate -2
            repeat

transform guitar_performance:
    parallel:
        block:
            ease 0.6 xoffset -25
            ease 0.6 xoffset 25
            ease 0.4 xoffset -15
            ease 0.4 xoffset 15
            ease 0.8 xoffset 0
            repeat
    parallel:
        block:
            ease 0.3 yoffset -12
            ease 0.3 yoffset 0
            ease 0.2 yoffset -8
            ease 0.2 yoffset 0
            pause 0.2
            repeat
    parallel:
        block:
            ease 1.4 rotate 4
            ease 1.4 rotate -4
            ease 1.2 rotate 3
            ease 1.2 rotate -3
            repeat
    parallel:
        block:
            ease 0.8 zoom 1.05
            ease 0.8 zoom 1.0
            ease 0.6 zoom 1.03
            ease 0.6 zoom 1.0
            repeat

image bg_dzinzo_rock = "images/CG/CG_Dznidzo_guitar.png"

image dzinzo_rock:
    "images/CG/CG_Dznidzo_guitar_2.png"
    anchor (0.5, 0.50)
    xpos 0.5
    ypos 0.55

label dzinzo_rock_scene:
    scene bg_garage
    with dissolve

    pause 0.2

    show bg_dzinzo_rock with dissolve

    pause 0.2

    play music music_rock fadeout 1

    show dzinzo_rock at guitar_performance 
    with dissolve

    d_t neutral "Схватив первую попавшуюся гитару в руки, я крутанул её пару раз и начал играть на ней, попутно постукивая ногой по барабанной установке."

    show dzinzo_rock at guitar_bounce:
        xzoom -1
    with Dissolve(0.5)

    pause 4

    show dzinzo_rock at guitar_performance:
        xzoom 1
    with Dissolve(0.5)

    pause 4

    hide dzinzo_rock
    hide bg_dzinzo_rock 
    with Dissolve(2)

    stop music fadeout 2
    pause 2

    return