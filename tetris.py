from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        
    ## ! Check the error for the deletion of the full rows
    def check_full_lines(self):
        row = FIELD_HEIGHT - 1
        for y in range(FIELD_HEIGHT - 1, -1, -1):
            for x in range(FIELD_WIDTH):
                self.field_array[row][x] = self.field_array[y][x]
                
                if self.field_array[y][x]:
                    self.field_array[row][x].position = vector(x, y)
            
            
            if sum(map(bool, self.field_array[y])) < FIELD_WIDTH:
                row -= 1
            else:
                for x in range(FIELD_WIDTH):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0
        
    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.position.x), int(block.position.y)
            self.field_array[y][x] = block
        
    def get_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]
        
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            self.put_tetromino_blocks_in_array()
            self.tetromino = Tetromino(self)
        
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        if pressed_key == pg.K_DOWN:
            self.tetromino.move(direction='down')
        if pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        if pressed_key == pg.K_UP:
            self.tetromino.rotate()
        
    def draw_grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, 'white',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        
    def update(self):
        if self.app.animation_trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()
    
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)