from random import randint
class BeatSequence:
    def __init__(self):
        self._beats = []
    
    def execute(self, cast, script, callback):
        pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]
        self._create_sequence(pads)

    def _create_sequence(self, pads):
        for i in range(10):
            index = randint(1, 4)
            self._beats.append(pads[index])

