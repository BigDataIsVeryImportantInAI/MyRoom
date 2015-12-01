__author__ = 'EUNGI'
from pico2d import *

title_background = None

class Background:
    def __init__(self):
        self.canvas_width, self.canvas_heigth = get_canvas_width(), get_canvas_height()
        self.back_image = load_image("page\\title\\back.png")
        self.title_image = load_image("page\\title\\title.png")
        #title이미지를 화면 상단에 딱 붙여서 나오게 계산
        self.title_image_y = self.canvas_heigth - 1 - self.title_image.h/2


    def draw(self):
        self.back_image.draw(self.canvas_width/2, self.canvas_heigth/2)
        self.title_image.draw(self.canvas_width/2, self.title_image_y)



def test_unit():
    open_canvas(1200, 800)
    clear_canvas()
    global title_background
    title_background = Background()

    title_background.draw()

    update_canvas()
    delay(1.5)
    close_canvas()


if __name__ == "__main__":
    test_unit()