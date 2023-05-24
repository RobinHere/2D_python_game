import pygame
from pygame.locals import *
from const import *
from player import *
from world import *
from spikes import *
from key import *

#pygame engine init and mixer init
pygame.init()
pygame.mixer.init()


#define name of process and initialize clock
clock = pygame.time.Clock()
pygame.display.set_caption("2D Platformer")

#Game loop
while isRunning:

    clock.tick(FPS)

    #Menu
    if menu:
        SCREEN.blit(img_MENU, (0, 0))
        SCREEN.blit(img_MENU_TEXT, (300,250))
        SCREEN.blit(img_MENU_TEXT2, (290,290))
        control = pygame.key.get_pressed()
        if isPlayingMusic:
            pass
        if not isPlayingMusic:
            pygame.mixer.Sound.stop(game_music)
            pygame.mixer.Sound.play(menu_music,-1)
            isPlayingMusic = True
        if control[K_RETURN]:
            pygame.mixer.Sound.stop(menu_music)
            isPlayingMusic = False
            menu = False
    #Game
    if menu == False and hasEnded == 0:
        SCREEN.blit(img_BACKGROUND, (0, 0))
        world.draw()
        hasEnded = player.statusUpdate()
        spike_group.draw(SCREEN)
        key_group.draw(SCREEN)
        if isPlayingMusic:
            pass
        if not isPlayingMusic:
            pygame.mixer.Sound.play(game_music,-1)
            isPlayingMusic = True
    
    #Game Over
    if hasEnded == 1:
        SCREEN.blit(img_DEATH, (0,0))
        SCREEN.blit(img_GAME_OVER, (300,250))
        SCREEN.blit(img_QUIT_TEXT, (300,310))
        SCREEN.blit(img_ENTER_TEXT, (300,360))
        player.rect.x = 50
        player.rect.y = 800
        control = pygame.key.get_pressed()
        if control[K_RETURN]:
            pygame.mixer.Sound.stop(death_music)
            isPlayingMusic = False
            hasEnded = 0
            menu = True
        elif control[K_q]:
            isRunning = False
        else:
            pass
    #Won
    if hasEnded == 2:
        SCREEN.blit(img_DEATH, (0, 0))
        SCREEN.blit(img_WON, (300,250))
        SCREEN.blit(img_QUIT_TEXT, (300,310))
        control = pygame.key.get_pressed()
        if control[K_q]:
            isRunning = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()
        
pygame.quit()




