__author__ = 'EUNGI'

from ClickableImage import ClickableImage
from pico2d import *
import game_framework
import worldmap
import math

from sdl2 import *

map = None
tiles = []
tilecol = []
hero = None

class Tile(ClickableImage):
    TILE_SIZE = 40

    def __init__(self, x, y):
        self.focus = 0
        self.tileCenter_x = x
        self.tileCenter_y = y
        self.vertexs = []   #헥사 타일의 모서리 xy좌표 6개
        #헥사 타일의 모서리 위에서부터 시계방향으로
        for i in range(0, 6):
            self.point = hex_corner(self.tileCenter_x, self.tileCenter_y, Tile.TILE_SIZE, i)
            self.vertexs.append(self.point)

    def draw(self):
        draw_hexagon(self.vertexs)

    def click_left(self):
        pass

class Map:
    def __init__(self):
        self.background = load_image('map\\stage1_background.PNG')

    def draw(self):
        self.background.draw(400,300)

class Unit(ClickableImage):
    MOVE_TO_CENTER_Y = 12
    def __init__(self):
        self.focus = 0
        self.x = tiles[5][3].tileCenter_x
        self.y = tiles[5][3].tileCenter_y
        self.frame = 0
        self.image = load_image('char\\race2\\worksheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 64, 80, 64, 80,self.x, self.y + Unit.MOVE_TO_CENTER_Y)

    def update(self):
        self.frame = (self.frame + 1) % 4
        delay(0.1)

    def click_left(self):
        pass

def hex_corner(x, y, size, i):
    angle_deg = 60 * i   + 30
    angle_rad = math.pi / 180 * angle_deg
    # SDL_Render.
    return SDL_Point(int(x + size * math.cos(angle_rad)), int(y + size * math.sin(angle_rad)))

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def enter():
    global  tiles, tilecol, hero, map
    height = Tile.TILE_SIZE * 2
    nexttile_width = math.sqrt(3)/2 * height
    for j in range(0, 12):
        if j % 2 == 0:
            tilecol = [Tile(0 + (math.sqrt(3)/4 * height) + (i * nexttile_width), 0 + (j * height * 3/4)) for i in range(0, 12)]
        else:
            tilecol = [Tile(0 + (i * nexttile_width), 0 + (j * height * 3/4)) for i in range(0, 12)]
        tiles.append(tilecol)
    hero = Unit()
    map = Map()

def exit():
    pass


def pause():
    pass


def resume():
    pass


def update():
    hero.update()


def draw():
    clear_canvas()
    map.draw()
    for tilecol in tiles:
        for tile in tilecol:
            tile.draw()
    hero.draw()
    update_canvas()




