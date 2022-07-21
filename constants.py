from pathlib import Path
from game.casting.color import Color
from game.casting.point import Point

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Batter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH


# FONT
FONT_FILE = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
RED_PAD_SOUND = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/sounds/red.mp3"
GREEN_PAD_SOUND = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/sounds/green.mp3"
BLUE_PAD_SOUND = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/sounds/blue.mp3"
YELLOW_PAD_SOUND = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/sounds/yellow.mp3"
WELCOME_SOUND = "C:/Users/carol/OneDrive/Documents/Spring Semester 2022/cse210/week10/batter-complete/batter/assets/sounds/start.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
GREY = Color(30, 30, 30)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


#PADS
PAD_GROUP = "pads"
PAD_DELAY = 0.5
PAD_RATE = 4

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

#COLORS
WHITE = Color(255, 255, 255)
RED = Color(250, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)


PAD_WIDTH = 200
PAD_HEIGHT = 200
PAD_MARGIN = 5
PAD_SIZE = Point(PAD_WIDTH, PAD_HEIGHT)

RED_PAD_POSITION = Point(int(CENTER_X - PAD_MARGIN - PAD_WIDTH), int(CENTER_Y - PAD_MARGIN - PAD_HEIGHT))
BLUE_PAD_POSITION = Point(int(CENTER_X - PAD_MARGIN - PAD_WIDTH), int(CENTER_Y + PAD_MARGIN))
GREEN_PAD_POSITION = Point(int(CENTER_X + PAD_MARGIN), int(CENTER_Y + PAD_MARGIN))
YELLOW_PAD_POSITION = Point(int(CENTER_X + PAD_MARGIN), int(CENTER_Y - PAD_MARGIN - PAD_HEIGHT))
