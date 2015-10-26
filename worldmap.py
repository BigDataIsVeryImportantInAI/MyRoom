__author__ = 'EUNGI'

from ClickableImage import ClickableImage
from pico2d import *
import game_framework
import title_state

name = "WorldMapState"

map = None
battle0, battle1, battle2, battle3 = None, None, None, None
hero = None
font = None

class Map:
    def __init__(self):
        self.image = load_image('page\\worldmap.png')
        self.gio = load_image('page\\geographic.png')


    def draw(self):
        global font
        self.image.draw(400,300)
        self.gio.draw(675,135)
        font.draw(645,135,"HanGleT^T")

class Beacon(ClickableImage):
    def __init__(self, x, y, name, where):
        self.focus = 0
        self.x = x
        self.y = y
        self.nameOfBeacon = name
        self.where = where
        self.image_red = load_image('page\\beacon_red.png')
        self.image_blue = load_image('page\\beacon_blue.png')
        self.x_start = self.x - self.image_red.w/2
        self.y_start = 600 - self.y - self.image_red.h/2
        self.x_end = self.x + self.image_red.w/2
        self.y_end = 600 - self.y + self.image_red.h/2

    def draw(self):
        global font
        self.image_red.draw(self.x, self.y)
        font.draw(self.x - (4 * len(self.nameOfBeacon)), self.y, self.nameOfBeacon)

    def click_left(self):
        print('left')
        global hero
        # 주인공이 있는 곳과 인근 비콘의 거리가 1이여야만 이동 가능
        if abs(hero.where - self.where) == 1:
            hero.where = self.where
            hero.x = self.x - 55
            hero.y = self.y + 30


class Hero:
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 508, 600-320
        self.frame = 0
        self.speed = 10
        self.where = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        # self.x += self.speed
        if self.x > 700:
            self.speed = -10
        elif self.x < 100:
            self.speed = 10
        delay(0.1)

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80, self.x, self.y)


def handle_events():
    global running
    global battle0, battle1, battle2, battle3
    events = get_events()
    for event in events:
        battle0.handle(event)
        battle1.handle(event)
        battle2.handle(event)
        battle3.handle(event)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(worldmap)
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
    global font
    font = load_font('font\\HANYGO230.ttf', 14)
    global map, battle0, battle1, battle2, battle3, hero
    map = Map()
    battle0 = Beacon(563, 600-350, "Aruva Caves", 0)
    battle1 = Beacon(432, 600-513, "Wetlands", -1)
    battle2 = Beacon(488, 600-221, "Sanctuary", 1)
    battle3 = Beacon(240, 600-294, "Forest", 2)
    hero = Hero()


def exit():
    global map, battle0, battle1, battle2, battle3, hero
    del(map, battle1, battle2, battle3)
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
    battle0.draw()
    battle1.draw()
    battle2.draw()
    battle3.draw()
    hero.draw()
    update_canvas()
    delay(0.02)




