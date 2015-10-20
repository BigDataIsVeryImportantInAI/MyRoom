import game_framework
import main_state
from pico2d import *


name = "TitleState"
back = None
menutitle = None
menubtn = None
btnnew = None
btnload = None
btnopen = None
btnquit = None
bgm = None

def enter():
    global back
    global menutitle
    global menubtn
    global btnnew
    global btnload
    global btnopen
    global btnquit
    back = load_image('page\\back.png')
    menutitle = load_image('page\\menutitle.png')
    menubtn = load_image('page\\menubtn.png')
    btnnew = load_image('page\\menu_mo_new.png')
    btnload = load_image('page\\menu_mo_load.png')
    btnopen = load_image('page\\menu_mo_open.png')
    btnquit = load_image('page\\menu_mo_quit.png')
    global bgm
    bgm = load_music('page\\menupage.wav')
    bgm.play(-1)

def exit():
    global back
    global menutitle
    global menubtn
    global btnnew
    global btnload
    global btnopen
    global btnquit
    global bgm
    del(back)
    del(menutitle)
    del(menubtn)
    del(btnnew)
    del(btnload)
    del(btnopen)
    del(btnquit)
    del(bgm)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y
            print(x, y)
            for eventEnt in event:
                print(eventEnt)


        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #game_framework.change_state(main_state)
                game_framework.quit()


def draw():
    clear_canvas()
    back.draw(400,300)
    menutitle.draw_to_origin(0,599 - menutitle.h)
    menubtn.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h)
    update_canvas()
    delay(0.01)

def update():
    pass

def pause():
    pass

def resume():
    pass






