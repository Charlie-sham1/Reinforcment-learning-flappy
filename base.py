import pygame
pygame.init()

class Base:
    VEL = 5
    Basee = pygame.image.load('/Users/rnda/Desktop/CODING_PROJECTS/NEAT_AI/NEAT_FLAPPY_B/MY_FLAPPY/imgs/base.png')

    def __init__(self,y):
        self.y = y
        self.img = self.Basee
        self.x1 = 0
        self.width = self.img.get_width()
        self.x2 = self.img.get_width()


    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, window):
        window.blit(self.img,(self.x1,self.y))
        window.blit(self.img,(self.x2,self.y))

