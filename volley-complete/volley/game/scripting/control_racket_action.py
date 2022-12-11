from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        rackets = cast.get_actors(RACKET_GROUP)
        racket1 = rackets[0]
        racket2 = rackets[1]

        if self._keyboard_service.is_key_down(LEFT1): 
            racket1.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT1): 
            racket1.swing_right() 
        else: 
            racket1.stop_moving()
         

        if self._keyboard_service.is_key_down(LEFT2):
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT2):
            racket2.swing_right() 
        else:
           racket2.stop_moving()