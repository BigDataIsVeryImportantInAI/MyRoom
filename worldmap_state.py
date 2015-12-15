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
bcn0, bcn1, bcn2, bcn3 = None, None, None, None
hero = None

def enter():
    global map, geo_btn, bcn0, bcn1, bcn2, bcn3, hero
    map = Background()
    geo_btn = Geography_Btn(635, 135, "아루바 만")
    bcn0 = Beacon(563, 600-350, "Aruva Caves", 0)
    bcn1 = Beacon(432, 600-513, "Wetlands", 1)
    bcn2 = Beacon(488, 600-221, "Sanctuary", 2)
    bcn3 = Beacon(240, 600-294, "Forest", 3)
    hero = Hero()


def exit():
    global map, geo_btn, bcn0, bcn1, bcn2, bcn3, hero
    del(map, bcn0, bcn1, bcn2, bcn3)
    del(hero)

def pause():
    pass

def resume():
    pass

def update(frame_time):
    hero.update(frame_time)
    bcn0.update(frame_time)
    bcn1.update(frame_time)
    bcn2.update(frame_time)
    bcn3.update(frame_time)

def draw(frame_time):
    clear_canvas()
    map.draw()
    geo_btn.draw()
    bcn0.draw()
    bcn1.draw()
    bcn2.draw()
    bcn3.draw()
    hero.draw()
    update_canvas()

    stateChangeCheck()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        geo_btn.handle(event)
        bcn0.handle(event)
        bcn1.handle(event)
        bcn2.handle(event)
        bcn3.handle(event)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(battlemap)


def stateChangeCheck():
    pass