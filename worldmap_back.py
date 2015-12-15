__author__ = 'EUNGI'
from pico2d import *
from ClickableImage import ClickableImage

world_background = None
geo_btn = None

class Background:
    def __init__(self):
        self.image_back = load_image("page\\worldmap.png")

    def draw(self):
        self.image_back.draw(400,300)


class Geography_Btn(ClickableImage):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.focus = 0
        self.image_geo = load_image("page\\geographic_sheet.png")
        self.x_start = self.x - self.image_geo.w/2
        self.y_start = 800 - self.y - self.image_geo.h/2
        self.x_end = self.x + self.image_geo.w/2
        self.y_end = 800 - self.y + self.image_geo.h/2

    def draw(self):
        if self.focus:
            self.image_geo.clip_draw(0, 0, 127, 27, self.x, self.y)
        else:
            self.image_geo.clip_draw(0, 30, 127, 25, self.x, self.y)
        print(self.focus)






def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()

    global  world_background, geo_btn
    world_background = Background()
    world_background.draw()
    while(running):
        geo_btn = Geography_Btn()
        geo_btn.draw()

        update_canvas()
        events = get_events()
        for event in events:
            geo_btn.handle(event, 0.1)
            if event.type == SDL_QUIT:
                close_canvas()
                running = False


if __name__ == "__main__":
    test_unit()