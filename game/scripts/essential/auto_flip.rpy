init -1 python:
    def check_flip_direction(tag, trans, st, at):
        attributes = renpy.get_attributes(tag)
        
        if attributes and 'left' in attributes:
            trans.xzoom = -1.0 
        else:
            trans.xzoom = 1.0
        
        return None

    def make_flip_function(tag):
        def flip_func(trans, st, at):
            return check_flip_direction(tag, trans, st, at)
        return flip_func

init -1:
    transform auto_flip(tag):
        function make_flip_function(tag)