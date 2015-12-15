from pico2d import *
import game_framework
import worldmap
from title_back import Background
from title_btn import ButtonNew, ButtonLoad, ButtonOpening, ButtonQuit

name = "TitleState"
background = None
btnNew = None
btnLoad = None
btnOpen = None
btnQuit = None
bgm = None


def enter():
    global background, btnNew, btnLoad, btnOpen, btnQuit
    background = Background()
    btnNew = ButtonNew()
    btnLoad = ButtonLoad()
    btnOpen = ButtonOpening()
    btnQuit = ButtonQuit()
    global bgm
    bgm = load_wav("page\\testwav.wav")
    bgm.repeat_play()

def exit():
    global background, btnNew, btnLoad, btnOpen, btnQuit
    global bgm
    del(background)
    del(btnNew)
    del(btnLoad)
    del(btnOpen)
    del(btnQuit)
    del(bgm)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        btnNew.handle(event)
        btnLoad.handle(event)
        btnOpen.handle(event)
        btnQuit.handle(event)
        print("title_state handle_events()")
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                # escape로 종료되는건 개발 기간 동안만 설정해둘것 완성 후에는 quit 버튼으로만 종료
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(worldmap)


def draw(frame_time):
    clear_canvas()
    background.draw()
    btnNew.draw()
    btnLoad.draw()
    btnOpen.draw()
    btnQuit.draw()
    update_canvas()

def update(frame_time):
    stateChangeCheck()

def pause():
    pass

def resume():
    pass

def stateChangeCheck():
    if btnNew.stateChange == True:
        game_framework.change_state(worldmap)
    elif btnLoad.stateChange == True:
        print("btnLoad clicked")
    elif btnOpen.stateChange == True:
        print("btnLoad clicked")
    elif btnQuit.stateChange == True:
        game_framework.quit()




