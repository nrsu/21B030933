import pygame
from pygame import mixer
from pygame.locals import *
pygame.init()

run=True
img=pygame.image.load("musicplayersurface.png")
surface=pygame.display.set_mode((500, 500))
mixer.music.load("yiruma.mp3")
mixer.music.play()
mixer.music.pause()

while run==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pressed_keys = pygame.key.get_pressed()
    
            
    if pressed_keys[K_UP]:
        mixer.music.unpause()
    if pressed_keys[K_DOWN]:
        mixer.music.pause()
    if pressed_keys[K_1]:
            mixer.music.unload()
            mixer.music.load("marsh.mp3")
            mixer.music.play()
        
    if pressed_keys[K_2]:

            mixer.music.unload()
            mixer.music.load("yiruma.mp3")
            mixer.music.play()
    if pressed_keys[K_3]:    
        mixer.music.unload()
        mixer.music.load("fur_elise.mp3")
        mixer.music.play()
    surface.blit(img, (0, 0))
    pygame.display.flip()
