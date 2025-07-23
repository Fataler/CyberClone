#images 

## Определения фоновых изображений


## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")

image bg_black_t_10 = Solid("#0000001a")
image bg_black_t_20 = Solid("#00000033")
image bg_black_t_30 = Solid("#0000004d")
image bg_black_t_40 = Solid("#00000066")
image bg_black_t_50 = Solid("#00000080")
image bg_black_t_60 = Solid("#00000099")
image bg_black_t_70 = Solid("#000000b3")
image bg_black_t_80 = Solid("#000000cc")
image bg_black_t_90 = Solid("#000000e6")

image d1 = "images/d1.png"

image bg_menu_main = "gui/menu/bg.png"

init:
    image avatar_circle = AlphaMask("gui/menu/avatar_square.jpg", im.Scale("gui/menu/alpha_mask.png", 320, 320))


## Эффекты
transform darken:
    matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

transform lighten:
    matrixcolor TintMatrix("#ffffff") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное затемнение
transform fade_to_dark:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное осветление
transform fade_to_light:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)

# Цветные заглушки для титров
