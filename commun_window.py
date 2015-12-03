__author__ = 'EUNGI'
from pico2d import *

class CommunicationWindow:
    def __init__(self):
        self.image = load_image("face\\face002.png")


    def draw(self):
        self.image.draw(400,300)



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