import pygame

screen = pygame.display.set_mode((1000,700))
screen.fill((255, 255, 255))
draw_on = False
last_pos = (0, 0)
color=(0, 0, 0)
radius = 10

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

try:
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos,  radius)
            last_pos = e.pos
        if e.type==pygame.KEYDOWN:
            color=(255, 255, 255)
        if e.type==pygame.KEYUP:
            color=(0,0,0)
        pygame.display.flip()
except StopIteration:
    pass

pygame.quit()