import pygame as pg 

vector = pg.math.Vector2

FPS = 60
FIELD_COLOR = (12, 10, 62)
BG_COLOR = (24, 89, 117)

TILE_SIZE = 30
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RESOLUTION = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

FONT_PATH = 'assets/Fonts/Freedom.ttf'
NUMS_PATH = 'assets/Fonts/BabyPlums.ttf'

# Offsets for the tetrominoes
INIT_POSITION_OFFSET = vector(FIELD_WIDTH // 2 - 1, 0) 
NEXT_POSITION_OFFSET = vector(FIELD_WIDTH * 1.3, FIELD_HEIGHT * 0.45)

# Tetrominoes moves
MOVE_DIRECTIONS = {'left': vector(-1, 0), 'right': vector(1, 0), 'down': vector(0, 1)}

ANIMATION_TIME_INTERVAL = 150 # milliseconds


FIELD_SCALE_WIDTH, FIELD_SCALE_HEIGHT = 1.7, 1.0
WIN_RES = WIN_WIDTH, WIN_HEIGHT = FIELD_RESOLUTION[0] * FIELD_SCALE_WIDTH, FIELD_RESOLUTION[1] * FIELD_SCALE_HEIGHT

# Get a pivot point in the origin and draw the tetrominoes from it
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (-1, -1), (0, -1)],
    'S': [(0, 0), (0, -1), (1, -1), (-1, 0)],
    'J': [(0, 0), (0, -1), (0, -2), (-1, 0)],
    'L': [(0, 0), (0, -1), (0, -2), (1, 0)],
    'I': [(0, 0), (0, -1), (0, -2), (0, 1)]
}