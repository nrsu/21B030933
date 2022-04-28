from turtle import position
import pygame
def line(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), d)
    else:   
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), d)
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    size_of_rect = (0,0)
    baseLayer = pygame.Surface((size_of_rect))

    clock = pygame.time.Clock()
    d = {
    'line' : True,
    'rect': False,
    'circle': False,
    'erase': False
    }

    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
    w = 2
    draw_line = False
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    d['line'] = True
                    for k, v in d.items():
                        if k != 'line':
                            d[k] = False
                if event.key == pygame.K_r:
                    d['rect'] = True
                    for k, v in d.items():
                        if k != 'rect':
                            d[k] = False
                if event.key == pygame.K_c:
                    d['circle'] = True
                    for k, v in d.items():
                        if k != 'circle':
                            d[k] = False
                if event.key == pygame.K_e:
                    d['erase'] = True
                    for k, v in d.items():
                        if k != 'erase':
                            d[k] = False
        if d['rect']:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                size_of_rect = (abs(currentX - prevX), abs(currentY - prevY))
                screen.blit(baseLayer, (0, 0))
                cor=prevX-currentX
                cor1=prevY-currentY
                if cor>0 and cor1>0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(currentX, currentY, size_of_rect[0], size_of_rect[1]))
                if cor<0 and cor1<0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(prevX, prevY, size_of_rect[0], size_of_rect[1]))
                if cor<0 and cor1>0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(currentX-size_of_rect[0], currentY, size_of_rect[0], size_of_rect[1]))
                if cor>0 and cor1<0:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(prevX-size_of_rect[0], prevY, size_of_rect[0], size_of_rect[1]))
                pygame.display.flip()
                
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        
    
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX, prevY, currentX, currentY)

                pygame.draw.rect(screen, (255,255, 255),pygame.Rect(r), 1)
        if d['line'] == 1:#debug
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False
            if event.type == pygame.MOUSEMOTION:
                currentX =  event.pos[0]
                currentY =  event.pos[1] 
            if isMouseDown:
                pygame.draw.line(screen, (200, 200,200), (prevX, prevY), (currentX, currentY))
            prevX = currentX
            prevY = currentY
        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

main()
