init -1 python:
    import functools as ft
    
    character_previous_attributes = {}

    def get_character_pose(character_name, current_attrs):
        """Автоматическое определение текущей позы персонажа через layeredimage"""
        for attr in current_attrs:
            talk_attrs = (character_name, attr, f'talk_{attr}')
            closed_attrs = (character_name, attr, f'closed_{attr}')
            
            if renpy.has_image(talk_attrs) and renpy.has_image(closed_attrs):
                return attr
        
        return None

    def talking_callback(event, character_name, interact=True, **kwargs):
        global character_previous_attributes
        
        if not interact:
            return
            
        if preferences.text_cps > 0:
            if event == 'show':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        attrs_str = f'{current_pose} talk_{current_pose}'
                        renpy.show(f'{character_name} {attrs_str}')
                    
            elif event == 'slow_done':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        attrs_str = f'{current_pose} closed_{current_pose}'
                        renpy.show(f'{character_name} {attrs_str}')
                        
                renpy.restart_interaction()
                
            elif event == 'end':
                if renpy.showing(character_name):
                    current_attrs = renpy.get_attributes(character_name)
                    current_pose = get_character_pose(character_name, current_attrs)
                    
                    if current_pose:
                        attrs_str = f'{current_pose} closed_{current_pose}'
                        renpy.show(f'{character_name} {attrs_str}')


image alice_standing_mouth_talk:
    choice:
        'images/mouthOpen.png'
        pause 0.1
        'images/mouthClosed.png'
        pause 0.15
    repeat


image alice_sitting_mouth_talk:
    choice:
        'images/mouthOpen_sit.png'
        pause 0.1
        'images/mouthClosed_sit.png'
        pause 0.15
    repeat

layeredimage alice:    
    group pose:
        attribute standing default:
            'images/test.png'
        attribute sitting:
            'images/test_sit.png'
    
    group mouth:
        attribute silence default:
            'images/mouthClosed.png'
        attribute closed_standing:
            'images/mouthClosed.png'
        attribute closed_sitting:
            'images/mouthClosed_sit.png'
        attribute talk_standing:
            'alice_standing_mouth_talk'
        attribute talk_sitting:
            'alice_sitting_mouth_talk'

define alice = Character('Алиса', color='#ffb3ba', image='alice',
                        callback=ft.partial(talking_callback, character_name='alice'))