from constants import *
from game.scripting.action import Action

class DrawPadAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        pad = cast.get_first_actor(PAD_GROUP)
        body = pad.get_body()
        color = pad.get_color()
        self._video_service.draw_rectangle(body, color)