import pygame, sys
from pygame.locals import *

from map import *
from entity import *

from random import randint

class Game():

    WINDOW_X_SIZE = 800
    WINDOW_Y_SIZE = 600
    MAP_TILE_SIZE = 10
    NUM_AI_WORMS = 20

    def __init__(self):

        # set up pygame
        pygame.init()

        # set up the window
        self.windowSurface = pygame.display.set_mode((Game.WINDOW_X_SIZE, Game.WINDOW_Y_SIZE), 0, 32)
        pygame.display.set_caption('Worms!')

        self._setup_new_game()

    def _setup_new_game(self):
        self.current_map = Map(80,60)

        self.entities = []
        for i in range(Game.NUM_AI_WORMS):
            new_worm = Entity("Player "+str(i+1),(randint(0,255),randint(0,255),randint(0,255)))
            self.entities.append(new_worm)
            new_worm.place_on_map(self.current_map)

    def _step(self):
        for entity in self.entities:
            entity.step(self.current_map)

        make_new_game = True
        for entity in self.entities:
            if entity.alive == True:
                make_new_game = False
                break
        if make_new_game == True:
            self._setup_new_game()

    def _draw(self):
        self.windowSurface.fill((0,0,0))
        self._draw_map(self.current_map)
        self._draw_entities(self.entities)
        pygame.display.update()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self._step()
            self._draw()

    def _draw_map(self,map):
        for x in range(map.size_x):
            for y in range(map.size_y):

                if map.tiles[x][y].walkable == True:
                    color = (40,40,40)
                else:
                    color = (0,0,0)

                pygame.draw.rect(
                    self.windowSurface,
                    map.tiles[x][y].color,
                    (
                        x*Game.MAP_TILE_SIZE,
                        y*Game.MAP_TILE_SIZE,
                        Game.MAP_TILE_SIZE,
                        Game.MAP_TILE_SIZE
                    ))

    def _draw_entities(self,entities):
        for entity in entities:
            pygame.draw.rect(
                self.windowSurface,
                entity.color,
                (
                    entity.x*Game.MAP_TILE_SIZE,
                    entity.y*Game.MAP_TILE_SIZE,
                    Game.MAP_TILE_SIZE,
                    Game.MAP_TILE_SIZE
                ))
