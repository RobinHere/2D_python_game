import pygame

pygame.mixer.init()

#screen
SCREEN_WIDTH= 1000
SCREEN_HEIGHT = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#game variables
tile_size = 50
isRunning = True
FPS = 60
menu = True
hasEnded = 0
isPlayingMusic = False
menu_music = pygame.mixer.Sound('sound/menu.mp3')
menu_music.set_volume(0.3)
game_music = pygame.mixer.Sound('sound/game.mp3')
game_music.set_volume(0.3)
death_music = pygame.mixer.Sound('sound/death.mp3')
death_music.set_volume(0.3)

#images
img_BACKGROUND = pygame.image.load('graphics/background.png')
img_GRASS_BLOCK = pygame.image.load('graphics/grass_block.png')
img_DIRT_BLOCK = pygame.image.load('graphics/dirt_block.png')
img_MENU_TEXT = pygame.image.load('graphics/menu_text.png')
img_MENU_TEXT = pygame.transform.scale(img_MENU_TEXT, (400,50))
img_MENU_TEXT2 = pygame.image.load('graphics/menu_text2.png')
img_MENU_TEXT = pygame.transform.scale(img_MENU_TEXT, (400,25))
img_MENU = pygame.image.load('graphics/menu.png')
img_DEATH = pygame.image.load('graphics/black.png')
img_DEATH = pygame.transform.scale(img_DEATH, (1024,1024))
img_GAME_OVER = pygame.image.load('graphics/over.png')
img_GAME_OVER = pygame.transform.scale(img_GAME_OVER,(400,50))
img_WON = pygame.image.load('graphics/won.png')
img_WON = pygame.transform.scale(img_WON,(400,50))
img_ENTER_TEXT = pygame.image.load('graphics/enter_text.png')
img_ENTER_TEXT = pygame.transform.scale(img_ENTER_TEXT,(400,25))
img_QUIT_TEXT = pygame.image.load('graphics/q_text.png')
img_QUIT_TEXT = pygame.transform.scale(img_QUIT_TEXT,(400,25))



