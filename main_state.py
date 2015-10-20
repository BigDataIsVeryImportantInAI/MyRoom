import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    state = None
    dash = 0
    pos = 0
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.dash_frames = 0
        self.speed = 5
        Boy.state = self.RIGHT_RUN
        #self.state = self.RIGHT_RUN

        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_left_run(self):
        # fill here
        if Boy.dash == 0:
            self.x -= self.speed
        else:
            self.x -= self.speed*3
        self.run_frames += 1
        self.dash_frames += 1
        if self.dash_frames % 12 > 10:
            self.speed = 5
        if self.x < 0:
            Boy.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames > 100:
            Boy.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        # fill here
        self.stand_frames += 1
        if self.stand_frames > 50:
            Boy.state = self.LEFT_RUN
            self.run_frames = 0
            self.speed = 5
            self.dash_frames = 0

    def handle_right_run(self):
        # fill here
        if Boy.dash == 0:
            self.x += self.speed
        else:
            self.x += self.speed*3
        self.run_frames += 1
        self.dash_frames += 1
        if self.dash_frames % 12 > 10:
            self.speed = 5
        if self.x > 800:
            Boy.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames > 100:
            Boy.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        # fill here
        self.stand_frames += 1
        if self.stand_frames > 50:
            Boy.state = self.RIGHT_RUN
            self.run_frames = 0
            self.speed = 5
            self.dash_frames = 0

    def handle_again_run(self):
        if Boy.state == 2 or 3:
            self.stand_frames = 49

    def handle_dash_run(self):
        Boy.dash = 0
        self.speed = 30
        self.dash_frames = 0


    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[Boy.state](self)
        #print(Boy.state)

    def draw(self):
        self.image.clip_draw(self.frame * 100, Boy.state * 100, 100, 100, self.x, self.y)

    def pouse(self):
        while(Boy.pos):
            delay(0.1)
            handle_events()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if Boy.state == Boy.LEFT_RUN or Boy.state == Boy.RIGHT_RUN:
                #print("Boy.state == 0 or 1")
                Boy.handle_dash_run(boy)
            elif Boy.state == Boy.LEFT_STAND or Boy.state == Boy.RIGHT_STAND:
                #print("Boy.state == 2 or 3")
                Boy.handle_again_run(boy)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            print("h")
            if Boy.pos == 0:
                Boy.pos = 1
                Boy.pouse(boy)
            else:
                Boy.pos = 0

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global  boy, grass
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass

def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    delay(0.05)





