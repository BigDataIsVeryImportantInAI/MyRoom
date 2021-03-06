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
    relative_str_position_x = 40
    relative_str_position_y = 1
    def __init__(self, x, y, name="noname"):
        self.x = x
        self.y = y
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.name = name
        self.mouseon_image = load_image("page\\world_geo\\btn_geo_on.png")
        self.mouseoff_image = load_image("page\\world_geo\\btn_geo.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2
        self.font = load_font("font\\ConsolaMalgun.ttf", 12)

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)
        self.font.draw(
            self.x - Geography_Btn.relative_str_position_x, self.y - Geography_Btn.relative_str_position_y, self.name)

    def click_left(self):
        print(self.name + " clicked")

def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()

    global  world_background, geo_btn
    world_background = Background()
    geo_btn = Geography_Btn(635, 135, "아루바 만")
    while(running):
        world_background.draw()
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