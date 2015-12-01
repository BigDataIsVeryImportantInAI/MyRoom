from pico2d import *
import game_framework
import worldmap
from title_back import Background

name = "TitleState"
btn = None
background = None
menutitle = None
menubtn = None
bgm = None

class MenuBtn:
    MOUSEON = None
    def __init__(self):
        self.btnNew = load_image('page\\menu_mo_new.png')
        self.btnLoad = load_image('page\\menu_mo_load.png')
        self.btnOpen = load_image('page\\menu_mo_open.png')
        self.btnQuit = load_image('page\\menu_mo_quit.png')
        MenuBtn.MOUSEON = 4;

    def drawNew(self):
        self.btnNew.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h + 48*3)
    def drawLoad(self):
        self.btnLoad.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h + 48*2)
    def drawOpen(self):
        self.btnOpen.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h + 48*1)
    def drawQuit(self):
        self.btnQuit.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h + 48*0)

    handle_btn = [drawNew, drawLoad, drawOpen, drawQuit]
    def draw(self):
        if MenuBtn.MOUSEON == 4:
            return
        else :
            self.handle_btn[MenuBtn.MOUSEON](self)
    def clickNew(self):
        game_framework.change_state(worldmap)
    def clickQuit(self):
        pass
    def clickQuit(self):
        pass
    def clickQuit(self):
        pass

    handle_click = [clickNew, clickQuit, clickQuit, clickQuit]
    def click(self):
        if MenuBtn.MOUSEON == 4:
            return
        else:
            self.handle_click[MenuBtn.MOUSEON](self)


def enter():
    global btn
    btn = MenuBtn()
    global background
    global menutitle
    global menubtn
    background = Background()
    menutitle = load_image('page\\menutitle.png')
    menubtn = load_image('page\\menubtn.png')
    global bgm
    bgm = load_wav("page\\testwav.wav")
    bgm.repeat_play()

def exit():
    global btn
    global background
    global menutitle
    global menubtn
    global bgm
    del(btn)
    del(background)
    del(menutitle)
    del(menubtn)
    del(bgm)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            global btn
            btn.click()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y
            # 399-menubtn.w/2,599-menutitle.h-menubtn.h + 48*3
            print(x, y)
            if x > 399-menubtn.w/2 and x < 399-menubtn.w/2 + 160 and y > menutitle.h + 48*0 and y < menutitle.h + 48*0+48:
                MenuBtn.MOUSEON = 0
                print(MenuBtn.MOUSEON)
            elif x > 399-menubtn.w/2 and x < 399-menubtn.w/2 + 160 and y > menutitle.h + 48*1 and y < menutitle.h + 48*1+48:
                MenuBtn.MOUSEON = 1
                print(MenuBtn.MOUSEON)
            elif x > 399-menubtn.w/2 and x < 399-menubtn.w/2 + 160 and y > menutitle.h + 48*2 and y < menutitle.h + 48*2+48:
                MenuBtn.MOUSEON = 2
                print(MenuBtn.MOUSEON)
            elif x > 399-menubtn.w/2 and x < 399-menubtn.w/2 + 160 and y > menutitle.h + 48*3 and y < menutitle.h + 48*3+48:
                MenuBtn.MOUSEON = 3
                print(MenuBtn.MOUSEON)
            else:
                MenuBtn.MOUSEON = 4
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(worldmap)


def draw(frame_time):
    clear_canvas()
    background.draw()
    # menutitle.draw_to_origin(0,599 - menutitle.h)
    menubtn.draw_to_origin(399-menubtn.w/2,599-menutitle.h-menubtn.h)
    btn.draw()
    update_canvas()
    delay(0.01)

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass






