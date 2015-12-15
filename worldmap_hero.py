__author__ = 'EUNGI'
from pico2d import *
import time

hero = None

class Hero:
    # 0.2초 마다 한 액션을 보여줄 생각
    TIME_PER_ACTION = 5.0
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 508, 600-320
        self.frame = 0
        self.speed = 10
        self.where = 0

    def update(self, frame_time):
        self.frame = int((Hero.TIME_PER_ACTION * frame_time) % 4)

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80, self.x, self.y)

    def move(self):
        pass




def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()

    global hero
    hero = Hero()
    current_time = time.time()
    while(running):
        frame_time = time.time() - current_time
        clear_canvas()

        hero.draw()
        hero.update(frame_time)

        update_canvas()
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                close_canvas()
                running = False


if __name__ == "__main__":
    test_unit()