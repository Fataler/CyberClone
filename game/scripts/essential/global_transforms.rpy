transform _appear(time = 1.0, delay = 0.0):
    alpha 0
    pause delay
    linear time alpha 1

transform _disappear(time = 1.0, delay = 0.0):
    alpha 1
    pause delay
    linear time alpha 0

transform _shake(time = 1.0, delay = 0.0):
    xoffset 0
    yoffset 0
    parallel:
        linear 0.1 xoffset 10
        pause 0.1
        linear 0.1 xoffset -10
        pause 0.1
        linear 0.1 xoffset 10
        pause 0.1
        linear 0.1 xoffset 0