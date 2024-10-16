from settings import *
from tetris import *
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN_RES) # Window Creation
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)
        self.text = Text(self)
    
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.animation_trigger = False
        pg.time.set_timer(self.user_event, ANIMATION_TIME_INTERVAL)
        
    
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)
        
    def draw(self):
        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RESOLUTION))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()
        
    def check_events(self):
        self.animation_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.animation_trigger = True
                
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
if __name__ == '__main__':
    app = App()
    app.run()