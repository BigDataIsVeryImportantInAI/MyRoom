from pico2d import load_image
import game_framework
import title_state
from ClickableImage import ClickableImage
from pico2d import *


name = "StartState"
logo_time = 0.0
logo_Image = None

class LogoImage(ClickableImage):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = load_image('page\\logopage.png')
        self.x_start = self.x - self.image.w/2
        self.y_start = 600 - self.y - self.image.h/2
        self.x_end = self.x + self.image.w/2
        self.y_end = 600 - self.y + self.image.h/2

    def draw(self):
        self.image.draw(self.x, self.y)

    def click_left(self):
        global logo_time
        logo_time = 5.0


def enter():
    open_canvas()
    hide_lattice()
    global logo_Image
    logo_Image = LogoImage(400,300)


def exit():
    global logo_Image
    del(logo_Image)
    close_canvas()

def update():
    global logo_time

    if(logo_time > 0.5):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global logo_Image
    clear_canvas()
    logo_Image.draw()
    update_canvas()




def handle_events():
    global logo_Image
    events = get_events()
    for event in events:
        logo_Image.handle(event)


def pause(): pass


def resume(): pass




