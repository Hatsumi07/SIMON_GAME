from random import randint

class BeatSequence:
    def __init__(self, pads):
        self._beats = []
        self._create_sequence(pads)
        

    def _create_sequence(self, pads):
        for i in range(10):
            index = randint(0, 3)
            self._beats.append(pads[index])
    
    def beats_list(self):
        return self._beats
