class PadsToPlay:
    def __init__(self):
        print("CREATING PADS TO PLAY ACTOR")
        self._to_play = [] #list of pads increasing from 1 to 1

    def set_pads(self, pad):
        self._to_play.append(pad)
        print("pad added to list of pads to be played")

    def get_pads(self):
        return self._to_play