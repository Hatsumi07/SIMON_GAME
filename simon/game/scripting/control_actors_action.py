from tkinter import LEFT
from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from constants import *
import pyray

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, mouse_service, audio_service, video_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        print("CREATING CONTROL ACTORS ACTION")
        self._mouse_service = mouse_service
        self._audio_service = audio_service
        self._video_service = video_service
        self._is_right = None



    def execute(self, cast, script, callback):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.set_normal_screen()
        print("EXECUTING CONTROL ACTORS ACTION")
        actor = cast.get_first_actor("pads_to_play")
        print("calling pads to play actor")
        pads_to_play = actor.get_pads()
        print("                    LENGTH OF PADS TO BE PLAYED : " + str(len(pads_to_play)))
        stats = cast.get_first_actor(STATS_GROUP)
        for pad_to_play in pads_to_play:
            print("                    starting pads to play LOOP")
            pads = [cast.get_first_actor("pad1"), cast.get_first_actor("pad2"), cast.get_first_actor("pad3"), cast.get_first_actor("pad4")]
            for pad in pads:
                print("                    starting pads LOOP")
                mouse_coordinate = self._mouse_service.get_coordinates()
                x = mouse_coordinate.get_x()
                y = mouse_coordinate.get_y()
                pad_x = pad.get_x()
                pad_y = pad.get_y()
                end_x = pad.get_end_x()
                end_y = pad.get_end_y()
                if (pad_x <= x and x <= end_x) and (pad_y <= y and y <= end_y):
                    print("Checking for mouse service")
                    if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
                        pad.pressed(self._audio_service)
        
                    if pyray.is_mouse_button_released(pyray.MOUSE_BUTTON_LEFT):
                        pad.released()
                        print("         CHECKING INPUT")
                        if pad.get_id == pad_to_play.get_id:
                            print("               PAD IS RIGHT")
                            self._is_right = True
                    
                        else:
                            print("               PAD IS WRONG")
                            self._is_right = False
                            break

                else:
                    print("mouse on rest")
                    pad.released()
        if self._is_right == True:
            callback.on_next(IN_PLAY)
            stats.add_points(+1)
        elif self._is_right == False:
            self._video_service.set_red_screen()
            stats.add_points(-1)

            
