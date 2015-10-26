__author__ = 'EUNGI'

from ClickableImage import ClickableImage
from pico2d import *
import game_framework
import worldmap
import sys
import types
import ctypes
import math
import json

from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *


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
    pass

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
    a = draw_rectangle(100, 100, 200, 200)
    renderer = get_current_renderer()
    xypoint = list()
    for i in range(0, 5):
        xypoint.append(hex_corner(400,300,50,i))
    # for i in range(0,5):
    #     xypoint = hex_corner(400,300,50,i)
    #     SDL_RenderDrawPoints(renderer, xypoint, 100)
    #     print("%d, %d", xypoint.x, xypoint.y)
    # SDL_RenderDrawLines(renderer, xypoint[0], 2)
    for i in range(0, 5):
        xypoint1 = hex_corner(400,300,50,1)
        xypoint2 = hex_corner(400,300,50,2)
        xypoint3 = hex_corner(400,300,50,3)
        xypoint4 = hex_corner(400,300,50,4)
        xypoint5 = hex_corner(400,300,50,5)
        xypoint6 = hex_corner(400,300,50,6)
    SDL_RenderDrawLine(renderer, xypoint1.x, xypoint1.y, xypoint2.x, xypoint2.y)
    SDL_RenderDrawLine(renderer, xypoint2.x, xypoint2.y, xypoint3.x, xypoint3.y)
    SDL_RenderDrawLine(renderer, xypoint3.x, xypoint3.y, xypoint4.x, xypoint4.y)
    SDL_RenderDrawLine(renderer, xypoint4.x, xypoint4.y, xypoint5.x, xypoint5.y)
    SDL_RenderDrawLine(renderer, xypoint5.x, xypoint5.y, xypoint6.x, xypoint6.y)
    SDL_RenderDrawLine(renderer, xypoint6.x, xypoint6.y, xypoint1.x, xypoint1.y)
    update_canvas()




