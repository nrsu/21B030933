import pygame
pygame.init()
screen=pygame.display.set_mode((800, 800))
x=40
y=40
run=True
clock=pygame.time.Clock()
while run==True:
    for action in pygame.event.get(): 
        if action.type==pygame.QUIT: 
            run=False 
    pressed=pygame.key.get_pressed()
    if y>25:
        if pressed[pygame.K_UP]: y -= 20
    if y<775:
        if pressed[pygame.K_DOWN]: y += 20
    if x>25:
        if pressed[pygame.K_LEFT]: x -= 20
    if x<775:
        if pressed[pygame.K_RIGHT]: x += 20
    screen.fill((255, 255, 255))
    ball=((255, 0, 0))
    pygame.draw.circle(screen, ball, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)