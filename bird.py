import pygame
import random

class Bird:

    bird1 = pygame.image.load('/Users/rnda/Desktop/CODING_PROJECTS/NEAT_AI/NEAT_FLAPPY_B/MY_FLAPPY/imgs/bird1.png') #CHANGE
    bird2 = pygame.image.load('/Users/rnda/Desktop/CODING_PROJECTS/NEAT_AI/NEAT_FLAPPY_B/MY_FLAPPY/imgs/bird2.png')
    bird3 = pygame.image.load('/Users/rnda/Desktop/CODING_PROJECTS/NEAT_AI/NEAT_FLAPPY_B/MY_FLAPPY/imgs/bird3.png')

    bird_imgs = [bird1,bird2,bird3]

    jump_vel = -10.5
    jump_count = 0
    flap_count = 0
    max_tilt = og_max_tilt = 25
    score = 0


    def __init__(self,y):
        self.x = 33
        self.y = self.og_y = y
        self.bird_img_count = 0
        self.img = self.bird_imgs[self.bird_img_count]
        self.tilt = 0

    def jump(self, birdJump = True):

        #create hill when pressing space

        #track when we last jump. when jump, restart jump_count and displacement 
        if birdJump == True:
            self.jump_count = 0
            self.jump_count += 1
            self.tilt = self.max_tilt
            displacement = self.jump_count * self.jump_vel +  0.5*(3)* self.jump_count **2
            self.y += displacement
        
        else:
            self.jump_count += 1
            self.tilt -= 2
            displacement = self.jump_count * 0.1
            self.y += displacement
        
        #if key down space happens once how does displacement cause full jump shape?


    def flap(self):

        self.flap_count += 1

        if self.flap_count == 5:
            self.bird_img_count += 1
            self.img = self.bird_imgs[self.bird_img_count]
    
        elif self.flap_count == 10:
            self.bird_img_count += 1
            self.img = self.bird_imgs[self.bird_img_count]

        elif self.flap_count == 15:
            self.bird_img_count -= 2
            self.flap_count -= 15
            self.img = self.bird_imgs[self.bird_img_count]


    def draw(self, window):

        self.img_r = pygame.transform.rotate(self.img,self.tilt)
        window.blit(self.img_r,(self.x,self.y))

    
    def reset(self):
        self.x = 33
        self.y = self.og_y
        self.bird_img_count = 0
        self.img = self.bird_imgs[self.bird_img_count]
        self.tilt = 0