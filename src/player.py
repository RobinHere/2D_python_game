import pygame
from pygame.locals import *
from world import *
from const import *
from key import *


class Player:
    def __init__(self,x: int,y: int) -> None:
        self.imagesRight = []
        self.imagesLeft = []
        self.index_of_image = 0
        self.counter_of_frame = 0
        self.direction = 'r'
        #load all animations as list
        for image_number in range(1,12):
            img_right = pygame.image.load(f'graphics/player{image_number}.png')         
            img_right = pygame.transform.scale(img_right, (30, 60))
            img_left = pygame.transform.flip(img_right, True, False)
            self.imagesRight.append(img_right)
            self.imagesLeft.append(img_left)
        self.image = self.imagesRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_Y = 0
        self.hasJumped = False
        self.isInAir = False
    
    def statusUpdate(self) -> int:
        #change in X and Y direction and cooldown for animation
        cooldown = 5
        change_X = 0
        change_Y = 0

        #Get pressed key and do action
        control = pygame.key.get_pressed()
        if control[pygame.K_w] and self.hasJumped == False and self.isInAir == False:
            self.velocity_Y = -17
            self.hasJumped = True
        if control[pygame.K_w] == False:
            self.hasJumped = False
        if control[pygame.K_d]:
            self.counter_of_frame += 1
            change_X += 4
            self.direction = 'r'
        if control[pygame.K_a]:
            change_X -= 4
            self.counter_of_frame += 1
            self.direction = 'l'
        if control[pygame.K_a] == False and control[pygame.K_d] == False:
            self.counter_of_frame = 0
            self.index_of_image = 0
            if self.direction == 'r':
                self.image = self.imagesRight[self.index_of_image]
            if self.direction == 'l':
                self.image = self.imagesLeft[self.index_of_image]

        #animation
        if self.counter_of_frame > cooldown:
            self.counter_of_frame = 0
            self.index_of_image += 1
            if self.index_of_image >= len(self.imagesRight):
                self.index_of_image = 0
            if self.direction == 'r':
                self.image = self.imagesRight[self.index_of_image]
            if self.direction == 'l':
                self.image = self.imagesLeft[self.index_of_image]

        #gravity
        self.velocity_Y += 1
        if self.velocity_Y > 8:
            self.velocity_Y = 8
        change_Y += self.velocity_Y

        self.isInAir = True
        #check collision
        for tile in world.tile_list:
			#check for collision in x direction
            if tile[1].colliderect(self.rect.x + change_X, self.rect.y, 30, 60):
                change_X = 0
                self.isInAir = False #wall jump
			#check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + change_Y, 30, 60):
				#check if below the ground i.e. jumping
                if self.velocity_Y < 0:
                    change_Y = tile[1].bottom - self.rect.top
                    self.velocity_Y = 0
				#check if above the ground i.e. falling
                elif self.velocity_Y >= 0:
                    change_Y = tile[1].top - self.rect.bottom
                    self.velocity_Y = 0
                    self.isInAir = False

        #check collsion with spikes and key
        if pygame.sprite.spritecollide(self, spike_group, False):
            pygame.mixer.Sound.stop(game_music)
            pygame.mixer.Sound.play(death_music,-1)
            return 1

        if pygame.sprite.spritecollide(self, key_group, False):
            return 2

        #adjust rect position on x and y
        self.rect.x += change_X
        self.rect.y += change_Y

        #block possibility for player to get out of bounds
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            change_X = 0
        
        if self.rect.left < 0 :
            self.rect.left = 0
            change_X = 0
        
        #draw player
        SCREEN.blit(self.image, self.rect)
        
        return 0

player = Player(50, 800)