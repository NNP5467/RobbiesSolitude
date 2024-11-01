import pygame

import config

from logs import Logout
from Graphic2D import *

pygame.init()


class Window:
    def __init__(self, log: Logout):
        config.BG_COLOR = (0, 0, 0)
        config.WIDTH = pygame.display.Info().current_w
        config.HEIGHT = pygame.display.Info().current_h

        self.__screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

        self.log = log
        self.exit = None
        self.button = None

        self.log.info("The window has been created")

    def init(self):
        self.exit = False

        self.button = Button2D(self.screen, self.log, 50, 50)

        self.log.info("The window has been initialized")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True

    def main_loop(self):
        self.events()

        self.button.draw()

        pygame.display.flip()
        self.__screen.fill(config.BG_COLOR)

    @property
    def screen(self):
        return self.__screen
