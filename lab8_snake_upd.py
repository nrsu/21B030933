import pygame 
from random import randrange
widlen=600
size=50
x=randrange(size, widlen-size, size)
y=randrange(size, widlen-size, size)
apple=randrange(size, widlen-size, size), randrange(size, widlen-size, size)
length=1
snake=[(x, y)]
dx=0
dy=0
timer=0
fps=60
direction={'W': True, 'A': True, 'S': True, 'D': True}
score=0
levelcounter=0
speedcount=0
applecount=0
snakespeed=10
applepos=[()]
timerbool=True
pygame.init()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
surface=pygame.display.set_mode((widlen, widlen))
clock=pygame.time.Clock()
img=pygame.image.load('1.jpg').convert()
run=True
while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    surface.blit(img, (0, 0))
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = font_level.render(f'LEVEL: {levelcounter}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))
    surface.blit(render_level, (5, 35))
    for i, j in snake:
        pygame.draw.rect(surface, (0, 255, 0), (i, j, size-1, size-1))
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, size, size))
    speedcount+=1
    if speedcount%snakespeed==0:
        x+=dx*size
        y+=dy*size
        snake.append((x, y))
        snake=snake[-length:]
    
    timer+=1
    if timer%60==0:
        #print(type(snake))
        #print(type(apple))
        applepos.append(apple)
        if (len(applepos)-1)%10==0:
            if len(set(applepos))==2:
                apple=randrange(size, widlen-size, size), randrange(size, widlen-size, size)
                applepos.clear()
                applepos.append((1, 1))
            else:
                applepos.clear()
                applepos.append((1, 1))
    if snake[-1]!=apple:
        for i in snake:
            if i==apple:
                apple=randrange(size, widlen-size, size), randrange(size, widlen-size, size)
    if snake[-1]==apple:
        apple=randrange(size, widlen-size, size), randrange(size, widlen-size, size)
        applecount+=1
        if applecount<5:
            score+=1
            length+=1
        if applecount>=5:
            appleweight=randrange(1, 4, 1)
            applecount+=appleweight
            score+=appleweight
            length+=appleweight

        if applecount%3==0:
            levelcounter+=1
            snakespeed-=1
            snakespeed=max(snakespeed, 4)

    if x < 0 or x > widlen - size or y < 0 or y > widlen - size or len(snake) != len(set(snake)):
        if x < 0 or x > widlen - size or y < 0 or y > widlen - size or len(snake) != len(set(snake)):
            pass
        surface.blit(img, (0, 0))
        gameover = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        surface.blit(gameover, (widlen // 2 - 200, widlen // 3))
        pygame.display.flip()
    pygame.display.flip()
    clock.tick(fps)
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if direction['W']:
            dx, dy = 0, -1
            direction = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if direction['S']:
            dx, dy = 0, 1
            direction = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if direction['A']:
            dx, dy = -1, 0
            direction = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if direction['D']:
            dx, dy = 1, 0
            direction = {'W': True, 'S': True, 'A': False, 'D': True, }
