__author__ = 'EUNGI'

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

class Beacon:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.nameOfBeacon = name
        self.image_red = load_image('page\\beacon_red.png')
        self.image_blue = load_image('page\\beacon_blue.png')

    def draw(self):
        global font
        self.image_red.draw(self.x, self.y)
        font.draw(self.x - (4 * len(self.nameOfBeacon)), self.y, self.nameOfBeacon)

class Hero:
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 508, 600-320
        self.frame = 0
        self.speed = 10

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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y
            print(x, y)
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
    battle0 = Beacon(563, 600-350, "Aruva Caves")
    battle1 = Beacon(432, 600-513, "Wetlands")
    battle2 = Beacon(488, 600-221, "Sanctuary")
    battle3 = Beacon(240, 600-294, "Forest")
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




