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
    pygame.draw.rect(screen,(0,0,255),(x+dirx,y+diry,20,20))
    pygame.display.flip()
 
    y += diry
    x += dirx 
    if y == 0 or y == 460: diry *= -1 
    if x == 0 or x == 620: dirx *= -1  

    clock.tick(50)

pygame.quit()