__author__ = 'EUNGI'

from ClickableImage import ClickableImage
from pico2d import *
import game_framework
import worldmap
import math

from sdl2 import *

tile = []
tilecol = []

class Tile:
    TILE_SIZE = 40

    def __init__(self, x, y):
        self.tileCenter_x = x
        self.tileCenter_y = y
        self.vertexs = []   #헥사 타일의 모서리 xy좌표 6개
        #헥사 타일의 모서리 위에서부터 시계방향으로
        for i in range(0, 6):
            self.point = hex_corner(self.tileCenter_x, self.tileCenter_y, Tile.TILE_SIZE, i)
            self.vertexs.append(self.point)

    def draw(self):
        draw_hexagon(self.vertexs)

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
    global  tile, tilecol
    height = Tile.TILE_SIZE * 2
    for i in range(0, 20):
        tilecol[i] = Tile(i * 100, 0)
    # tile = Tile(100, 100)
    # tile1 = Tile(100 + math.sqrt(3)/2 * height  , 100)
    # tile2 = Tile(100 + math.sqrt(3)/4 * height, 100 + height * 3/4)

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    pass

def draw():

    clear_canvas()
    for tile in tilecol:
        tile.draw()

    update_canvas()




