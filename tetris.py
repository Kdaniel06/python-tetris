from settings import *
import math
from tetromino import Tetromino
import pygame.freetype as ft

class Text:
    def __init__(self, app):
        self.app = app 
        self.font = ft.Font(FONT_PATH)
        self.num_font = ft.Font(NUMS_PATH)
        
        
    def draw(self):
        self.font.render_to(self.app.screen, (WIN_WIDTH * 0.595, WIN_HEIGHT * 0.02),
                            text='TETRIS', fgcolor='white', 
                            size=TILE_SIZE * 1.65, bgcolor='black')
        
        self.font.render_to(self.app.screen, (WIN_WIDTH * 0.65, WIN_HEIGHT * 0.22),
                            text='next', fgcolor='#e55381', 
                            size=TILE_SIZE * 1.4, bgcolor='black')
        
        self.font.render_to(self.app.screen, (WIN_WIDTH * 0.64, WIN_HEIGHT * 0.67),
                            text='score', fgcolor='white', 
                            size=TILE_SIZE * 1.65, bgcolor='black')
        
        self.num_font.render_to(self.app.screen, (WIN_WIDTH * 0.64, WIN_HEIGHT * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white', 
                            size=TILE_SIZE * 1.8)

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        
        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
        
    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0
        
        
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
                self.full_lines += 1
        
    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.position.x), int(block.position.y)
            self.field_array[y][x] = block
        
    def get_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]
    
    def is_game_over(self):
        if self.tetromino.blocks[0].position.y == INIT_POSITION_OFFSET[1]:
            pg.time.wait(300)
            return True
        
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)
        
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
            self.get_score()
        self.sprite_group.update()
    
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)