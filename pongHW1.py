import pygame
import random
screen = pygame.display.set_mode((640, 480))
running = True

clock = pygame.time.Clock()

x=random.randint(0,640)
y=random.randint(0,480)

dirx=1
diry=1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,255),(x+dirx,y+diry,15,15))
    pygame.display.flip()
 
    y += diry 
    if y == 0 or y == height-1: diry *= -1 
     

    clock.tick(1)

pygame.quit()