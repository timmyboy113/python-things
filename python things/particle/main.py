import pygame,random
from pygame.locals import *

xmax = 1000    #width of window
ymax = 600     #height of window

class Smoke():
    def __init__(self, startx, starty, col):
        self.x = startx
        self.y = random.randint(0, starty)
        self.col = col
        self.sx = startx
        self.sy = starty

    def move(self):
        if self.y < 0:
            self.x = self.sx
            self.y = self.sy
        else:
            self.y -= 1
        self.x += random.randint(-1, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    black = (0,0,0)
    grey = (145,145,145)
    light_grey = (192,192,192)
    dark_grey = (183, 183, 183)

    clock = pygame.time.Clock()

    particles = []
    for part in range(6000):
        if part % 2 > 0: col = grey
        #elif part % 5 > 0: col = dark_grey
        elif part % 3 > 0: col = dark_grey
        else: col = light_grey
        particles.append( Smoke(0, 500, col) )

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(black)
        for p in particles:
            p.move()
            pygame.draw.circle(screen, p.col, (p.x, p.y), 15)

        pygame.display.flip()
        clock.tick(80)
    pygame.quit()

if __name__ == "__main__":
    main()