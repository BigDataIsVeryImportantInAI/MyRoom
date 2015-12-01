from pico2d import load_image
import game_framework
import title_state
from ClickableImage import ClickableImage
from pico2d import *


name = "StartState"
logo_time = 0.0
logo_Image = None

CANVAS_WIDTH = 1200
CANVAS_HIGHT = 800

class LogoImage():
    def __init__(self):
        self.x = CANVAS_WIDTH/2
        self.y = CANVAS_HIGHT/2
        self.image = load_image('page\\logo\\logopage.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def click_left(self):
        global logo_time
        logo_time = 5.0


def enter():
    open_canvas(CANVAS_WIDTH, CANVAS_HIGHT)
    hide_lattice()
    global logo_Image
    logo_Image = LogoImage()


def exit():
    global logo_Image
    del(logo_Image)
    close_canvas()

def update(frame_time):
    global logo_time

    logo_time += frame_time
    if(logo_time > 2):
        logo_time = 0
        # game_framework.quit()
        game_framework.push_state(title_state)

def draw(frame_time):
    global logo_Image
    clear_canvas()
    logo_Image.draw()
    update_canvas()

def handle_events(frame_time):
    global logo_Image
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            # game_framework.quit()
            game_framework.push_state(title_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # game_framework.quit()
            game_framework.push_state(title_state)



def pause(): pass

def resume(): pass
