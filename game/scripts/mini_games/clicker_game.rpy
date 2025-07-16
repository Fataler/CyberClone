init python:
    import random
    
    class ClickerGame:
        def __init__(self):
            self.score = 0
            self.target_score = 100
            self.is_completed = False
            self.message_shown = {10: False, 40: False, 60: False}
            self.current_message = ""
            self.message_timer = 0.0
            self.click_animations = []
            
        def click(self):
            if self.is_completed:
                return
                
            self.score += 1
            
            self.add_click_animation()
            
            self.check_score_messages()
            
            if self.score >= self.target_score:
                self.is_completed = True
                
        def add_click_animation(self):
            """Анимация +1"""
            x_offset = random.randint(-100, 100)
            y_offset = random.randint(-50, 50)
            
            animation = {
                'x': x_offset,
                'y': y_offset,
                'alpha': 1.0,
                'timer': 1.0
            }
            self.click_animations.append(animation)
            
        def update_animations(self, dt):
            for anim in self.click_animations[:]:
                anim['timer'] -= dt
                anim['alpha'] = max(0.0, anim['timer'])
                anim['y'] -= dt * 100
                
                if anim['timer'] <= 0:
                    self.click_animations.remove(anim)
                    
        def check_score_messages(self):
            if self.score == 10 and not self.message_shown[10]:
                self.show_message("Неплохо! Продолжай кликать!")
                self.message_shown[10] = True
            elif self.score == 40 and not self.message_shown[40]:
                self.show_message("Ого! Ты на полпути к победе!")
                self.message_shown[40] = True
            elif self.score == 60 and not self.message_shown[60]:
                self.show_message("Отлично! Еще немного!")
                self.message_shown[60] = True
                
        def show_message(self, text):
            self.current_message = text
            self.message_timer = 2.0
            
        def update_message_timer(self, dt):
            if self.message_timer > 0:
                self.message_timer -= dt
                if self.message_timer <= 0:
                    self.current_message = ""

screen clicker_game():
    modal True
    
    key "dismiss" action NullAction()
    
    default game = ClickerGame()
    default sprite_scale = 1.0
    default animation_timer = 0.0
    
    if True:
        timer 0.016 repeat True action Function(game.update_animations, 0.016)
        timer 0.016 repeat True action Function(game.update_message_timer, 0.016)
    
    add "#2a2a2a"
    
    if not game.is_completed:
        frame:
            background None
            xalign 0.5
            yalign 0.1
            
            text "[game.score]":
                size 80
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]
                xalign 0.5

        button:
            background Frame("#4a9eff", 10, 10)
            xsize 200
            ysize 200
            xalign 0.5
            yalign 0.5
            action [
                Function(game.click),
                SetScreenVariable("sprite_scale", 0.9),
                SetScreenVariable("animation_timer", 0.1)
                # Function(renpy.play, "audio/click_sound.ogg", channel="sound")
            ]
            at sprite_click_animation(sprite_scale)
            
            text "CLICK":
                size 40
                color "#ffffff"
                bold True
                xalign 0.5
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            
            for anim in game.click_animations:
                text "+1":
                    size 60
                    color "#00ff00"
                    bold True
                    xalign 0.5
                    yalign 0.5
                    xoffset anim['x']
                    yoffset anim['y']
                    outlines [(2, "#000000", 0, 0)]
                    at flying_text_with_alpha(anim['alpha'])
        
        if game.current_message:
            frame:
                background Frame("#000000aa", 20, 20)
                xalign 0.5
                yalign 0.8
                xpadding 30
                ypadding 15
                
                text game.current_message:
                    size 50
                    color "#ffffff"
                    xalign 0.5
                    at message_appear
    
    else:
        frame:
            background "#000000cc"
            xfill True
            yfill True
            
            vbox:
                spacing 50
                xalign 0.5
                yalign 0.5
                
                text "ПОБЕДА!":
                    size 100
                    color "#ffff00"
                    bold True
                    xalign 0.5
                    outlines [(3, "#000000", 0, 0)]
                    at victory_text
                
                text "Поздравляем! Вы набрали [game.target_score] очков!":
                    size 60
                    color "#ffffff"
                    xalign 0.5
                    text_align 0.5
                    outlines [(2, "#000000", 0, 0)]
                
                textbutton "Далее":
                    text_size 70
                    xalign 0.5
                    action Return(True)
                    at victory_button
    
    if not game.is_completed:
        textbutton "Выйти":
            text_size 40
            xalign 0.05
            yalign 0.05
            action Return(False)
    
    if animation_timer > 0.0:
        timer animation_timer action [
            SetScreenVariable("sprite_scale", 1.0),
            SetScreenVariable("animation_timer", 0.0)
        ]

transform sprite_click_animation(scale_val):
    anchor (0.5, 0.5)
    zoom scale_val
    linear 0.1 zoom 1.0

transform flying_text_with_alpha(alpha_val):
    alpha alpha_val

transform message_appear:
    alpha 0.0 yoffset 20
    ease 0.3 alpha 1.0 yoffset 0

transform victory_text:
    zoom 0.5 alpha 0.0
    ease 0.5 zoom 1.2 alpha 1.0
    ease 0.2 zoom 1.0

transform victory_button:
    alpha 0.0 yoffset 30
    pause 0.5
    ease 0.3 alpha 1.0 yoffset 0

label test_clicker_game:
    $ result = renpy.call_screen("clicker_game")
    if result:
        "Отлично! Вы прошли кликер!"
    else:
        "Вы вышли из игры."
    return 