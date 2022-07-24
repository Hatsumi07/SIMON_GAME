from game.scripting.action import Action
import time
from random import randint
from constants import *

class PlayPadAction(Action):
    def __init__(self, audio_service):
        print("CREATING PLAY PAD ACTION")
        self._audio_service = audio_service
        print("setting time of playpadaction creation")
        self._start = time.time()
        print(self._start)
        self._pads = None
        self._index = randint(0, 3)
        self._pad = None

    def execute(self, cast, script, callback):
        print("EXECUTING PLAY PAD ACTION")
        pads_to_play = cast.get_first_actor("pads_to_play")
        print(time.time())
        elapsed = time.time() - self._start
        print(elapsed)
        self._pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]
        self._pad = self._pads[self._index]
        print("playing pad")
        if elapsed >= 2:
            print("conditional")
            if self._pad.is_pressed():
                print("Release button")
                self._pad.released()
                print("new start time set")
                callback.on_next(PLAYER_TURN)
                print("finish audio")
                print("adding pad object to pads to be played list")
                pads_to_play.set_pads(self._pad)
            else:
                print("Press button")
                self._pad.pressed(self._audio_service)

        
            
