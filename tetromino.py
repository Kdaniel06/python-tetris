from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = vector(position) + INIT_POSITION_OFFSET
        self.alive = True
        
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, '#e55381', (1, 1, TILE_SIZE - 2, TILE_SIZE - 2), border_radius=5)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position * TILE_SIZE 
        
    def is_alive(self):
        if not self.is_alive:
            self.kill()
        
    def rotate(self, pivot_position):
        translated = self.position - pivot_position
        rotated = translated.rotate(90)
        return rotated + pivot_position
        
    def set_rect_position(self):
        self.rect.topleft = self.position * TILE_SIZE
        
    def update(self):
        self.is_alive()
        self.set_rect_position()
        
    def is_collide(self, position):
        x, y = int(position.x), int(position.y)
        if 0 <= x < FIELD_WIDTH and y < FIELD_HEIGHT and (
            y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True
        
    

## The name of the pieces in tetris is tetromino
class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing  = False
        
    def rotate(self):
        pivot_position = self.blocks[0].position
        new_block_position = [block.rotate(pivot_position) for block in self.blocks]
        
        if not self.is_collide(new_block_position):
            for i, block in enumerate(self.blocks):
                block.position = new_block_position[i]
        
    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))
        
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.position + move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)
        
        if not is_collide:
            for block in self.blocks:
                block.position += move_direction
        elif direction == 'down':
            self.landing = True
    
    def update(self):
        self.move('down')