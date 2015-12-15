__author__ = 'EUNGI'
from pico2d import *
from ClickableImage import ClickableImage
import time

global beacon

class Beacon(ClickableImage):
    relative_str_position_x = 40
    relative_str_position_y = 1
    relative_btn_position_x = 53
    # 0.2초 마다 한 액션을 보여줄 생각
    TIME_PER_ACTION = 5.0
    def __init__(self, x, y, name="noname", where=0):
        self.x = x
        self.y = y
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.frame = 0
        self.name = name
        self.where = where
        self.clicked = False
        self.font = load_font("font\\ConsolaMalgun.ttf", 12)
        # self.frame
        self.mouseon_image = load_image("page\\world_beacon\\btn_bcn_on.png")
        self.mouseoff_image = load_image("page\\world_beacon\\btn_bcn.png")
        self.blue_image = load_image("page\\world_beacon\\beacon_btn_blue_sheet.png")
        self.red_image = load_image("page\\world_beacon\\beacon_btn_red_sheet.png")
        self.green_image = load_image("page\\world_beacon\\beacon_btn_green_sheet.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)
        self.blue_image.clip_draw(0, self.frame * 14, 15, 14,self.x-Beacon.relative_btn_position_x, self.y)
        self.font.draw(
            self.x - Beacon.relative_str_position_x, self.y - Beacon.relative_str_position_y, self.name)

    def update(self, frame_time):
        self.frame = int((Beacon.TIME_PER_ACTION * frame_time) % 4)

    def click_left(self):
        print(self.name + " clicked")
        self.clicked = True




def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()

    global beacon
    beacon = Beacon(400,400)

    current_time = time.time()
    while(running):
        frame_time = time.time() - current_time
        clear_canvas()

        beacon.draw()
        beacon.update(frame_time)

        update_canvas()
        events = get_events()
        for event in events:
            beacon.handle(event)
            if event.type == SDL_QUIT:
                close_canvas()
                running = False


if __name__ == "__main__":
    test_unit()



