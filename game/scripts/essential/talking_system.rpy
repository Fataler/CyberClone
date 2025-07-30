init -1 python:
    import functools as ft
    
    talk_key = 'talk_'

    def get_character_pose(character_name, current_attrs): #legacy
        for attr in current_attrs:
            if not attr.startswith(talk_key):
                talk_attr = f'{talk_key}{attr}'
                if renpy.has_image((character_name, talk_attr)):
                    return attr
            elif attr.startswith(talk_key):
                base_attr = attr[len(talk_key):]
                if renpy.has_image((character_name, base_attr)):
                    return base_attr
        
        return None

    def talking_callback(event, character_name, interact=True, **kwargs): #legacy
        """Callback для персонажей с talk_pose структурой (alice, izumi)"""
        if not interact:
            return
            
        if preferences.text_cps > 0:
            if event == 'begin':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        talk_attr = f'{talk_key}{current_pose}'
                        renpy.show(f'{character_name} {talk_attr}')
                    
            elif event == 'slow_done' or event == 'end':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        renpy.show(f'{character_name} {current_pose}')
                        
                renpy.restart_interaction()

    def layered_talking_callback(event, character_name, interact=True, **kwargs):
        if not interact:
            return
            
        if preferences.text_cps > 0:
            if event == 'begin' or event == 'show':
                if renpy.showing(character_name):
                    renpy.show(f'{character_name} talk')
                    
            elif event == 'slow_done' or event == 'end':
                if renpy.showing(character_name):
                    renpy.show(f'{character_name} -talk')
                        
                renpy.restart_interaction()


image alice_standing:
    Composite(
        (970, 1080),
        (0, 0), 'images/test.png',
        (0, 0), 'images/mouthOpen.png'
    )

image alice_standing_mouth_closed:
    Composite(
        (970, 1080),
        (0, 0), 'images/test.png',
        (0, 0), 'images/mouthClosed.png'
    )

image alice_sitting:
    Composite(
        (970, 1000),
        (0, 0), 'images/test_sit.png',
        (0, 0), 'images/mouthOpen_sit.png'
    )

image alice_standing_mouth_talk:
    choice:
        'alice_standing'
        pause 0.1
        'alice_standing_mouth_closed'
        pause 0.15
    repeat

image alice_sitting_mouth_talk:
    choice:
        'alice_sitting'
        pause 0.1
        'images/mouthClosed_sit.png'
        pause 0.15
    repeat

image izumi_talk_stand:
    'images/izumi/1.png'
    pause 0.1
    'images/izumi/2.png'
    pause 0.1
    'images/izumi/3.png'
    pause 0.1
    repeat

layeredimage alice:
    group pose:
        attribute standing default:
            'alice_standing'
        attribute sitting:
            'alice_sitting'
        attribute talk_standing:
            'alice_standing_mouth_talk'
        attribute talk_sitting:
            'alice_sitting_mouth_talk'

define alice = Character('Алиса', color='#ffb3ba', image='alice',
                        callback=ft.partial(talking_callback, character_name='alice'))