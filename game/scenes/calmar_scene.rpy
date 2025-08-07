transform squid_rapid_jump:
    parallel:
        block:
            ease 0.425 xoffset -200
            ease 0.425 xoffset 200
            ease 0.425 xoffset -50
            ease 0.425 xoffset 50
            ease 0.3 xoffset 0
            repeat
    parallel:
        block:
            ease 0.15 yoffset -40
            ease 0.15 yoffset 0
            repeat
    parallel:
        block:
            ease 0.45 rotate 7
            ease 0.45 rotate -7
            repeat

transform squid_quick_spin:
    rotate 0
    ease 1.2 rotate 360
    rotate 0

transform squid_shake:
    parallel:
        block:
            ease 0.275 xoffset -50
            ease 0.275 xoffset 50
            ease 0.275 xoffset -25
            ease 0.275 xoffset 25
            ease 0.15 xoffset 0
            repeat
    parallel:
        block:
            ease 0.25 yoffset -12
            ease 0.25 yoffset 0
            ease 0.25 yoffset -8
            ease 0.25 yoffset 0
            repeat
    parallel:
        block:
            ease 0.25 rotate 10
            ease 0.25 rotate -10
            repeat

transform squid_finale:
    parallel:
        block:
            ease 0.35 xoffset -35
            ease 0.35 xoffset 35
            ease 0.2 xoffset -25
            ease 0.2 xoffset 25
            ease 0.225 xoffset 0
            repeat
    parallel:
        block:
            ease 0.12 yoffset -20
            ease 0.12 yoffset 0
            ease 0.09 yoffset -10
            ease 0.09 yoffset 0
            repeat
    parallel:
        block:
            ease 0.45 rotate 10
            ease 0.45 rotate -15
            repeat
    parallel:
        block:
            ease 0.6 zoom 1.1
            ease 0.6 zoom 1.0
            repeat


image dz_calmar_bg = "images/CG/CG_Dznidzo_calmar_2.png"
image dz_calmar:
    "images/CG/CG_Dznidzo_calmar.png"
    anchor (0.5, 0.50)
    xpos 0.5
    ypos 0.55

label dz_calmar_scene:
    scene bg_square
    with dissolve

    pause 0.5

    show dz_calmar_bg with dissolve

    pause 0.5

    stop music
    play music music_meatball_parade

    show dz_calmar at squid_rapid_jump 
    with dissolve

    t_t "Дзиндзо бегал по всей площади, совал листовки в руки, пел дурацкие песни про жареного кальмара в сотне вариантов текста, который генерировал на ходу."

    show dz_calmar at squid_rapid_jump:
        xzoom -1
    with Dissolve(0.1)

    t_t hz cry_sad "Но хуже всего было то, что он надел совершенно идиотский костюм в виде кальмара и периодически..." 

    show dz_calmar at squid_shake:
        xzoom 1
    with Dissolve(0.1)

    t_t hz cry_sad "...когда мимо проходила особенно крупная толпа, начинал плясать, чтобы привлечь их внимание."

    show dz_calmar at squid_shake:
        xzoom -1
    with Dissolve(0.1)

    t_t "То и дело Дзиндзо поворачивался в мою сторону и победно подмигивал мне."

    show dz_calmar at squid_quick_spin
    with Dissolve(0.1)

    $ renpy.pause(1, hard=True)

    show dz_calmar at squid_rapid_jump:
        xzoom -1
    with Dissolve(0.2)

    t_t cry_why "С лицом лица я наблюдал за этим, раскрыть себя означало угробить весь план."

    t_t hz cry_sad "Пришлось поступиться своей репутацией в нашем и так не очень большом городке, где большинство людей хоть не лично, но шапочно знакомы."

    show dz_calmar at squid_rapid_jump:
        xzoom -1
    with Dissolve(0.2)

    t_t thinking thinking_hard "Надо сказать, свою задачу он выполнил на ура:" 

    show dz_calmar at squid_quick_spin
    with Dissolve(0.1)

    $ renpy.pause(1, hard=True)

    show dz_calmar at squid_finale:
        xzoom -1
    with Dissolve(0.2)

    t_t thinking thinking_hard "В скором времени на площади возникло такое столпотворение, что хозяйка лавки быстро продала все свои запасы и закрыла лавку. "
    
    # мини игра раздача листовок
    hide dz_calmar_bg
    hide dz_calmar with Dissolve(2)

    stop music fadeout 2
    pause 2

    return