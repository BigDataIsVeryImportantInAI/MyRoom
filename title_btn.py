__author__ = 'EUNGI'

from pico2d import *
from ClickableImage import ClickableImage
import game_framework
import worldmap

btnNew = None
btnLoad = None
btnOpeng = None
btnQuit = None

class ButtonNew(ClickableImage):
    buttonNewX = 0
    buttonNewY = 0
    def __init__(self):
        self.x = get_canvas_width() / 2
        self.y = get_canvas_height() / 2
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_new_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_new.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = 800 - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = 800 - self.y + self.mouseon_image.h/2
        ButtonNew.buttonNewX = self.x
        ButtonNew.buttonNewY = self.y

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button New is clicked")
        game_framework.change_state(worldmap)

class ButtonLoad(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - 48
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_load_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_load.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = 800 - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = 800 - self.y + self.mouseon_image.h/2

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Load is clicked")

class ButtonOpening(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - (48*2)
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_opening_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_opening.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = 800 - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = 800 - self.y + self.mouseon_image.h/2

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Opening is clicked")

class ButtonQuit(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - (48*3)
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_quit_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_quit.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = 800 - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = 800 - self.y + self.mouseon_image.h/2

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Quit is clicked")

#테스트 하기 위해 click_left 함수를 pass로 바꿀것!
def test_unit():
    running = True
    open_canvas(1200, 800)
    clear_canvas()
    global btnNew, btnLoad, btnOpeng, btnQuit
    btnNew = ButtonNew()
    btnLoad = ButtonLoad()
    btnOpeng = ButtonOpening()
    btnQuit = ButtonQuit()

    while(running):
        btnNew.draw()
        btnLoad.draw()
        btnOpeng.draw()
        btnQuit.draw()

        update_canvas()
        events = get_events()
        for event in events:
            btnNew.handle(event, 0.1) #0.1은 더미 프레임 타임
            btnLoad.handle(event, 0.1)
            btnOpeng.handle(event, 0.1)
            btnQuit.handle(event, 0.1)
            if event.type == SDL_QUIT:
                close_canvas()
                running = False

if __name__ == "__main__":
    test_unit()