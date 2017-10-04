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
        pass
        
    def mouseUp(self, button, pos):
       pass
        
    def mouseMotion(self, buttons, pos, rel):
        print buttons, pos, rel

    def draw(self):

       self.screen.fill((255,255,255))
       pygame.draw.circle(self.screen, (randrange(0,255),randrange(0,255),randrange(0,255)), (self.one,self.two) ,20)
       i = randrange(0,2)
       k = randrange(0,2)

       if self.one >= self.w or self.two >= self.h or self.one <= 0 or self.two <= 0:
           self.one = 400
           self.two = 300

       else:
     
           if i == 1:
               self.one += randrange(0,10)
           else:
               self.one -= randrange(0,10)

           if k == 1:
               self.two += randrange(0,10)
           else:
               self.two -= randrange(0,10)




       
s = Starter()
s.mainLoop(60)
