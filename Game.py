import pygame
import random
import neat
import pickle
from bird import Bird
from base import Base
from background import Background
from pipe import Pipe
pygame.init()
 
You_lost_font = pygame.font.SysFont("comicsans",20)


class Game_information:
    def __init__(self,pipe_passes, collisions):
        self.pipe_passes = pipe_passes
        self.collisions = collisions


class Game:
    
    win_w, win_h = 288, 512

    def __init__(self,window,win_width,win_height):
        self.window = window
        self.win_width = win_width
        self.win_height = win_height

        self.back = Background(0)
        self.base = Base(self.win_h - Base.Basee.get_height())
        self.pipe = Pipe()
        self.bird = Bird(((self.win_h-Base.Basee.get_height())//2 - Bird.bird1.get_height()//2))
        self.You_lost_label = You_lost_font.render(f"You lost, restarting in 3 sec", 1, (255,255,255))

        self.pipe_passes = self.pipe.score
        self.collisions = 0


    def move_and_draw_images(self):
        self.back.draw(self.window)
        self.back.move()
        self.base.move()
        self.pipe.draw(self.window)
        self.pipe.move()
        self.base.draw(self.window)
        self.bird.draw(self.window)
        self.bird.flap()


    def check_collision(self):
        if self.pipe.bottom_x1 + Pipe.pipe_img.get_width() >33 and self.pipe.bottom_x1 < 33 + self.bird.img.get_width():
                if self.bird.y + self.bird.img.get_height() > self.pipe.bottom_y1:
                    self.bird.reset()
                    self.pipe.reset()
                    self.collisions += 1

        if self.pipe.bottom_x2 + Pipe.pipe_img.get_width() >33 and self.pipe.bottom_x2 < 33 + self.bird.img.get_width():
                if self.bird.y + self.bird.img.get_height()> self.pipe.bottom_y2:
                    self.bird.reset()
                    self.pipe.reset()
                    self.collisions += 1
                    
        if self.pipe.top_x1 + Pipe.pipe_img.get_width() >33 and self.pipe.top_x1 < 33 + self.bird.img.get_width():
                if self.bird.y < self.pipe.bottom_y1 - self.pipe.GAP-15:
                    self.bird.reset()
                    self.pipe.reset()
                    self.collisions += 1

        if self.pipe.top_x2 + Pipe.pipe_img.get_width() >33 and self.pipe.top_x2 < 33 + self.bird.img.get_width():
            if self.bird.y < self.pipe.bottom_y2 - self.pipe.GAP-15:
                    self.bird.reset()
                    self.pipe.reset()
                    self.collisions += 1
                
        if self.bird.y >= self.base.y-10:
                self.bird.reset()
                self.pipe.reset()
                self.collisions += 1

                
        pygame.display.update()



    def game_loop(self):

        self.move_and_draw_images()
        self.check_collision()
        game_info = Game_information(self.pipe.score, self.collisions)
        return game_info


    def reset(self):
        self.bird.reset()
        self.pipe.reset()


