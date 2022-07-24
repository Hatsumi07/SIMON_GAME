from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):

    def __init__(self, use_keyboard, keyboard_service, next_scene):
        self._use_keyboard = use_keyboard
        self._keyboard_service = keyboard_service
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        if self._use_keyboard == True:
            if self._keyboard_service.is_key_pressed(ENTER):
                callback.on_next(self._next_scene)
        else:
            callback.on_next(self._next_scene)