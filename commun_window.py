__author__ = 'EUNGI'
from pico2d import *

class CommunicationWindow:
    def __init__(self):
        self.canvas_width, self.canvas_heigth = get_canvas_width(), get_canvas_height()
        self.faceImage = load_image("face\\face002.png")
        self.cwin_faceImage = load_image("page\\commun\\cwin_face.png")
        self.cwinImage = load_image("page\\commun\\cwin.png")


    def draw(self):
        self.faceImage.draw(400,300)

    def draw_window_withface(self):
        pass

    def draw_window(self):
        pass



def test_unit():
    open_canvas()
    clear_canvas()

    cWindow = CommunicationWindow()
    cWindow.draw()

    update_canvas()
    delay(1)
    close_canvas()

if __name__ == "__main__":
    test_unit()