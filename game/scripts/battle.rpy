label start_pokemon_battle:
    window hide
    
    $ kostyan_hp = 100
    $ mishanya_hp = 100
    $ battle_state = "select_action"
    $ battle_message = ""
    $ show_battle_buttons = True
    $ magic_used = False
    
    # play music "audio/bg/battle_theme.ogg" fadein 1.0
    
    show screen pokemon_battle with Dissolve(1.0)
    
    pause

    hide screen pokemon_battle with Dissolve(0.5)
    window show
    
    "Ну что ж, битва завершена..."
    
    return

label test_pokemon_battle:
    "Сейчас начнется битва!"
    
    call start_pokemon_battle

    scene bg_black with Dissolve(1)
    
    "Битва закончилась. Возвращаемся к истории."
    
    return 