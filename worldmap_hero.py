__author__ = 'EUNGI'
from pico2d import *

hero = None

class Hero:
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 508, 600-320
        self.frame = 0
        self.speed = 10
        self.where = 0

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80, self.x, self.y)

    def move(self):
        pass




def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()

    global  world_background, geo_btn
    while(running):

        update_canvas()
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                close_canvas()
                running = False


if __name__ == "__main__":
    test_unit()