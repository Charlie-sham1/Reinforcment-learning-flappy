import pygame
import random
import neat
import random
from Game import Game
import pickle
pygame.init()

class Neat_game:
    def __init__(self,window,win_w, win_h):
        self.game = Game(window, win_w, win_h)

        self.bird = self.game.bird
        self.pipe = self.game.pipe
        self.background = self.game.back
        self.base = self.game.base

    def train_ai(self, genome1, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1,config)
        
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output_1 = net1.activate((self.bird.x + self.bird.bird1.get_width(),self.bird.y, self.pipe.bottom_x1,self.pipe.top_x1, self.pipe.bottom_x2, self.pipe.top_x2, self.pipe.bottom_y1, self.pipe.bottom_y2, self.pipe.bottom_y1 - self.pipe.GAP -20))
            decision1 = output_1.index(max(output_1))

            if decision1 == 0:
                self.bird.jump(birdJump=False)

            elif decision1 == 1:
                self.bird.jump(birdJump=True)

            game_info = self.game.game_loop()

            if game_info.collisions == 1:
                self.calculate_fitness(game_info,genome1)
                break


    def test_ai(self, winner_net):
        
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output_1 = winner_net.activate((self.bird.x + self.bird.bird1.get_width(),self.bird.y, self.pipe.bottom_x1,self.pipe.top_x1, self.pipe.bottom_x2, self.pipe.top_x2, self.pipe.bottom_y1, self.pipe.bottom_y2, self.pipe.bottom_y1 - self.pipe.GAP -20))
            decision1 = output_1.index(max(output_1))

            if decision1 == 0:
                self.bird.jump(birdJump=False)

            elif decision1 == 1:
                self.bird.jump(birdJump=True)

            self.game.game_loop()


    def calculate_fitness(self,game_info,genome1):
        genome1.fitness = game_info.pipe_passes - game_info.collisions


def eval_genomes(genomes,config):

    win_w, win_h = 288, 512
    window = pygame.display.set_mode((win_w, win_h))

    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0 if genome1.fitness == None else genome1.fitness
        neat_bird = Neat_game(window, win_w, win_h)
        neat_bird.train_ai(genome1, config)


def run_ai(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("best_flappy_nn", "wb") as f:
        pickle.dump(winner, f)


def test_best_network(config):
    win_w, win_h = 288, 512
    win = pygame.display.set_mode((win_w, win_h))
    pygame.display.set_caption("best flappy net")

    with open("best_flappy_nn", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    game = Neat_game(win,win_w, win_h)
    game.test_ai(winner_net)



if __name__ == '__main__':

    config_path = 'config-feedforward.txt'

    config = config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    #run_ai(config)
    test_best_network(config)
    