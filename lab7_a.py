import pygame
from datetime import datetime

tm=datetime.now()
sec=tm.second
min=tm.minute

pygame.init()

screen=pygame.display.set_mode((1200, 800))
back=pygame.image.load('back.jpg').convert()
right=pygame.image.load('Right.jpg').convert()
left=pygame.image.load('Left.jpg').convert()

sur1=pygame.Surface((1200, 800))
sur1.set_colorkey((0, 0, 0))
sur=pygame.Surface((1200, 800))
sur.set_colorkey((0, 0, 0))

pygame.display.flip()
run=True
cnt=sec*6
sangle=54-sec*6
mangle=306-min*6

while run==True:
    pygame.time.delay(1000)
    sangle=sangle-6
    cnt=cnt+6

    screen.blit(back, (0, 0))
    screen.blit(sur, (0, 0))
    sur.blit(pygame.transform.rotate(right, sangle), pygame.transform.rotate(right, sangle).get_rect(center=(1280/2, 960/2))) 
    screen.blit(sur1, (0, 0))
    sur1.blit(pygame.transform.rotate(left, mangle), pygame.transform.rotate(left, mangle).get_rect(center=(1280/2, 960/2)))
    
    if cnt==360:
        cnt=0
        mangle=mangle-6
    pygame.display.flip()
    
    for action in pygame.event.get(): 
        if action.type==pygame.QUIT: 
            run=False 
pygame.quit()