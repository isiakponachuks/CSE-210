# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tetris"

# DIALOG
PRESS_KEY_TO_START = "PRESS ANY KEY TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
MSG_HOW_TO_PAUSED_GAME = "Press p to pause game"
GAME_PAUSED = "PAUSED"
PRESS_KEY_TO_CONTINUE = "PRESS A KEY TO CONTINUE"
WAS_GOOD_GAME = "GAME OVER"

FPS = 25 # FRAME RATE

# SCREEN
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BOX_SIZE = 20
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLANK = '.'

# FRAME RATE MOVEMENT - HOLDING DOWN KEYS
MOVE_SIDE_WAYS_FREQ = 0.15
MOVE_DOWN_FREQ = 0.1

# PADDING LEFT, RIGHT, and TOP
MARGIN_WIDTH = int((WINDOW_WIDTH - BOARD_WIDTH * BOX_SIZE) / 2)
TOP_MARGIN = WINDOW_HEIGHT - (BOARD_HEIGHT * BOX_SIZE) - 5

# COLORS        R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

# BOARD GAME COLORS
BORDER_COLOR = BLUE
BACK_GROUND_COLOR = BLACK
TEXT_COLOR = WHITE
TEXT_SHADOW_COLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color


# FONT
FONT_FILE = "freesansbold.ttf"
FONT_SMALL = 18
FONT_LARGE = 100

# SOUND
TETRIS_0_MUSIC = "tetris/assets/sounds/0_tetris.mid"
TETRIS_1_MUSIC = "tetris/assets/sounds/1_tetris.mid"

# ********* TEXT *********
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# ********* KEYS *********
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# ********* SCENES *********
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER_SCENE = 4

# ********* LEVELS *********
BASE_LEVELS = 5


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# ********* PHASES *********
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

# ********* STATS *********
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# ********* HUD *********
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# TETRIS SIZE
TEMPLATE_WIDTH = 5
TEMPLATE_HEIGHT = 5

# TETRIS - GEOMETRIC SHAPES (composed of four squares, connected orthogonally.)
S_SHAPE_TETRIS = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]


Z_SHAPE_TETRIS = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]


I_SHAPE_TETRIS = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]


O_SHAPE_TETRIS = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]


J_SHAPE_TETRIS = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]


L_SHAPE_TETRIS = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]


T_SHAPE_TETRIS = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]


SHAPES = {'S': S_SHAPE_TETRIS, 
          'Z': Z_SHAPE_TETRIS,
          'J': J_SHAPE_TETRIS,
          'L': L_SHAPE_TETRIS,
          'I': I_SHAPE_TETRIS,
          'O': O_SHAPE_TETRIS,
          'T': T_SHAPE_TETRIS}
