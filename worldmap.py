__author__ = 'EUNGI'

from pico2d import *
import game_framework
import title_state

name = "WorldMapState"

map = None
hero = None

class Map:
    def __init__(self):
        self.image = load_image('page\\worldmap.png')
        self.font = load_font("fir", 20)


    def draw(self):
        self.image.draw(400,300)
        self.font.draw(100,100,"HEEEEEEEEEEEEEEEEEEE")

class Hero:
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 100, 100
        self.frame = 0
        self.speed = 10

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.speed
        if self.x > 700:
            self.speed = -10
        elif self.x < 100:
            self.speed = 10
        delay(0.1)

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             game_framework.change_state(title_state)
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
        #     if Boy.state == Boy.LEFT_RUN or Boy.state == Boy.RIGHT_RUN:
        #         print("Boy.state == 0 or 1")
        #         Boy.handle_dash_run(boy)
        #     elif Boy.state == Boy.LEFT_STAND or Boy.state == Boy.RIGHT_STAND:
                # print("Boy.state == 2 or 3")
                # Boy.handle_again_run(boy)
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
        #     print("h")
        #     if Boy.pos == 0:
        #         Boy.pos = 1
        #         Boy.pouse(boy)
        #     else:
        #         Boy.pos = 0

def enter():
    global map, hero
    map = Map()
    hero = Hero()


def exit():
    global map, hero
    del(map)
    del(hero)

def pause():
    pass

def resume():
    pass

def update():
    hero.update()

def draw():
    clear_canvas()
    map.draw()
    hero.draw()
    update_canvas()
    delay(0.02)




