#!/usr/bin/python
from visual import *
import random
from math import sqrt, atan2
            
def collisions(scene):
    #check for colision against other balls
    for a in range(0, len(scene.objects)):
        for b in range(a+1, len(scene.objects)):
            dx = scene.objects[a].pos.x - scene.objects[b].pos.x
            dy = scene.objects[a].pos.y - scene.objects[b].pos.y
            #quick and dirty check to find that objects that are not going to collide
            if dx > 1: continue
            if dy > 1: continue
            #full collision check 
            distance = (dx*dx)+(dy*dy) # dont need sqrt atm as distance to check is 1
            if(distance < 1):
                diff = scene.objects[a].pos-scene.objects[b].pos
                diff = diff/sqrt(diff.x**2 +diff.y**2)    
                a_comp= diff*(scene.objects[a].velocity.x * diff.x + scene.objects[a].velocity.y * diff.y)
                b_comp= diff*(scene.objects[b].velocity.x * diff.x + scene.objects[b].velocity.y * diff.y)
                scene.objects[a].velocity= scene.objects[a].velocity - a_comp + b_comp
                scene.objects[b].velocity= scene.objects[b].velocity - b_comp + a_comp                
                #place second ball so not touching first
                mid_point= (scene.objects[a].pos + scene.objects[b].pos)/2                                
                angle = math.atan2(dy, dx)
                scene.objects[a].pos= mid_point+diff/2*1.0005
                scene.objects[b].pos= mid_point-diff/2*1.0005


    #check for collision against area bounds            
    for check in scene.objects:
        if(check.pos.x < -12):
            check.velocity = vector(abs(check.velocity.x), check.velocity.y, 0)            
        elif(check.pos.x > 12):
            check.velocity = vector(-abs(check.velocity.x), check.velocity.y, 0)            
        elif(check.pos.y < -12):
            check.velocity = vector(check.velocity.x, abs(check.velocity.y), 0)
        elif(check.pos.y > 12):
            check.velocity = vector(check.velocity.x, -abs(check.velocity.y), 0)

random.seed()
scene = display(title='Bouncy Balls', width=500, height=500, center=(0,0,0), background=(0,0,0))
scene.autoscale = 0
delta=0.1
scene.range = (-25, -25, -25)

for i in range(0, 30):
    ball = sphere(pos=(random.randint(-10, 10), random.randint(-10, 10), 0),color=(1, 1, 1),radius=0.5)
    ball.speed = float(random.randint(1, 5))/2
    ball.velocity = vector(cos(radians(i*60)), sin(radians(i*60)), 0)

while 1:
    rate(60)
    for ball in scene.objects:
        ball.pos = ball.pos + (ball.velocity*delta*ball.speed)
    collisions(scene)