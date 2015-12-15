__author__ = 'EUNGI'

from ClickableImage import ClickableImage
from pico2d import *
import game_framework
import title_state
import battlemap
from worldmap_back import Background, Geography_Btn
from worldmap_beacon import Beacon
from worldmap_hero import Hero

name = "WorldMapState"

map = None
geo_btn = None
battle0, battle1, battle2, battle3 = None, None, None, None
hero = None
font = None

class Beacon(ClickableImage):
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    WIDTH_BTN_TO_BEACON = 60

    def __init__(self, x, y, name, where):
        self.focus = 0
        self.x = x
        self.y = y
        self.frame = 0
        self.nameOfBeacon = name
        self.where = where
        self.image_beacon = load_image('page\\beacon_sheet.png')
        self.image_bluebtn = load_image('page\\beacon_btn_blue_sheet.png')
        self.image_redbtn = load_image('page\\beacon_btn_red_sheet.png')
        self.image_greenbtn = load_image('page\\beacon_btn_green_sheet.png')
        self.image_red = load_image('page\\beacon_red.png')
        self.image_blue = load_image('page\\beacon_blue.png')
        self.x_start = self.x - self.image_red.w/2
        self.y_start = 600 - self.y - self.image_red.h/2
        self.x_end = self.x + self.image_red.w/2
        self.y_end = 600 - self.y + self.image_red.h/2

    def draw(self):
        global font
        self.image_red.draw(self.x, self.y)
        #focus되지 않으면 0~27높이의 그림을 focus되면 30~55높이의 그림을 출력
        # self.image_beacon.clip_draw(0 + (self.focus * 30), 0, 127, 27 + (self.focus * 28), self.x, self.y)
        # self.image_bluebtn.clip_draw(0, 0, 0, 0, self.x - Beacon.WIDTH_BTN_TO_BEACON, self.y)
        font.draw(self.x - (4 * len(self.nameOfBeacon)), self.y, self.nameOfBeacon)

    def click_left(self):
        print('left')
        global hero
        # 주인공이 있는 곳과 인근 비콘의 거리가 1이여야만 이동 가능
        if abs(hero.where - self.where) == 1:
            hero.where = self.where
            hero.x = self.x - 55
            hero.y = self.y + 30

    def update(self, frame_time):
        pass

class Hero:
    def __init__(self):
        self.image = load_image('char\\race2\\worksheet.png')
        self.x, self.y = 508, 600-320
        self.frame = 0
        self.speed = 10
        self.where = 0

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80, self.x, self.y)

    def move(self):
        pass



def enter():
    global font
    font = load_font('font\\HANYGO230.ttf', 14)
    global map, geo_btn, battle0, battle1, battle2, battle3, hero
    map = Background()
    geo_btn = Geography_Btn()
    battle0 = Beacon(563, 600-350, "Aruva Caves", 0)
    battle1 = Beacon(432, 600-513, "Wetlands", -1)
    battle2 = Beacon(488, 600-221, "Sanctuary", 1)
    battle3 = Beacon(240, 600-294, "Forest", 2)
    hero = Hero()


def exit():
    global map, geo_btn, battle0, battle1, battle2, battle3, hero
    # battle클래스의 핸들이벤트가 del후에도 콜되서 멈춤
    # del(map, battle0, battle1, battle2, battle3)
    del(hero)

def pause():
    pass

def resume():
    pass

def update(frame_time):
    hero.update()

def draw(frame_time):
    clear_canvas()
    map.draw()
    geo_btn.draw()
    battle0.draw()
    battle1.draw()
    battle2.draw()
    battle3.draw()
    hero.draw()
    update_canvas()


def handle_events(frame_time):
    global running
    global battle0, battle1, battle2, battle3
    events = get_events()
    for event in events:
        geo_btn.handle(event)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(battlemap)
        battle0.handle(event)
        battle1.handle(event)
        battle2.handle(event)
        battle3.handle(event)
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

