from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import *



class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

        self.one = 50
        self.two = 50
		
    def update(self):
        pass
        
    def keyUp(self, key):
        print key

        if key == 275:
            self.one += 5

        if key == 276:
            self.one -= 5

        if key == 274:
            self.two += 5

        if key == 273:
            self.two -= 5
        
    def mouseUp(self, button, pos):
       pass
        
    def mouseMotion(self, buttons, pos, rel):
        print buttons, pos, rel

        if buttons[0] == 1:
            self.one = pos[0]
            self.two = pos[1]

    def draw(self):
       pygame.draw.circle(self.screen, (0,255,255), (self.one,self.two) ,5)

    


       
s = Starter()
s.mainLoop(100)
