__author__ = 'EUNGI'

from pico2d import *
from ClickableImage import ClickableImage
import game_framework
import worldmap

btnNew = None
btnLoad = None
btnOpeng = None
btnQuit = None
# 버튼 바로 아래에다 다른 버튼을 집어넣기 위한 변수
BTN_IMAGE_Y_SIZE = 48


class ButtonNew(ClickableImage):
    # 다른 버튼들의 이미지 초기화에도 같이 쓰임
    buttonNewX = 0
    buttonNewY = 0
    def __init__(self):
        self.x = get_canvas_width() / 2
        self.y = get_canvas_height() / 2
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_new_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_new.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2
        ButtonNew.buttonNewX = self.x
        ButtonNew.buttonNewY = self.y
        self.stateChange = False

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button New is clicked")
        self.stateChange = True

class ButtonLoad(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - BTN_IMAGE_Y_SIZE
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_load_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_load.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2
        self.stateChange = False

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Load is clicked")
        self.stateChange = True

class ButtonOpening(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - (BTN_IMAGE_Y_SIZE*2)
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_opening_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_opening.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2
        self.stateChange = False

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Opening is clicked")
        self.stateChange = True

class ButtonQuit(ClickableImage):
    def __init__(self):
        self.x = ButtonNew.buttonNewX
        self.y = ButtonNew.buttonNewY - (BTN_IMAGE_Y_SIZE*3)
        self.win_heigth = get_canvas_height()
        self.focus = 0
        self.mouseon_image = load_image("page\\title\\btn_quit_on.png")
        self.mouseoff_image = load_image("page\\title\\btn_quit.png")
        self.x_start = self.x - self.mouseon_image.w/2
        self.y_start = self.win_heigth - self.y - self.mouseon_image.h/2
        self.x_end = self.x + self.mouseon_image.w/2
        self.y_end = self.win_heigth - self.y + self.mouseon_image.h/2
        self.stateChange = False

    def draw(self):
        if self.focus:
            self.mouseon_image.draw(self.x, self.y)
        else:
            self.mouseoff_image.draw(self.x, self.y)

    def click_left(self):
        print("Button Quit is clicked")
        self.stateChange = True

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