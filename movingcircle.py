import pygame
import random
import math


def c2p(x,y):
    r=math.sqrt(x*x + y*y)

    if x==0:
        theta=math.pi/2
    else: 
        theta=math.atan(y/x)

    c2p=[r,theta,math.degrees(theta)]
    return c2p

print(c2p(0,1))


def p2c(r,theta):
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    p2c=[x,y]
    return p2c


def angle2c(x,y,p,q):
    angle=math.atan((q-y)/(p-x))
    return angle
    

print(p2c(1,math.pi/6))

screen = pygame.display.set_mode((640, 480))
running = True

clock = pygame.time.Clock()

x=random.randint(0,620)
y=random.randint(0,460)
p=random.randint(0,630)
q=random.randint(0,470)

speed = 1
angle = 0.5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pv,qv = p2c(speed,angle)

    if angle2c(x,y,p,q)>angle:
        angle+=0.1
        p += pv
        q += qv
    else:
        p += pv
        q += qv

    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0,0,255),[round(p),round(q)],4)
    pygame.draw.circle(screen,(255,0,0),[round(x),round(y)],20)
    


        
    pygame.display.flip()
 

    clock.tick(60)

pygame.quit()