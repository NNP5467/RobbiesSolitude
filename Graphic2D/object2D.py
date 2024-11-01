from typing import Tuple

import pygame

from Graphic2D.graphic2D import Graphic2DInstruments
from logs import Logout


class Object2D(Graphic2DInstruments):
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int = 0,
                 y: int = 0,
                 width: int = 50,
                 height: int = 50,
                 color: Tuple[int, int, int] = (255, 0, 0),
                 border: int = 0,
                 border_radius: int = 0):
        super().__init__(screen, log, x, y)
        self.rect: pygame.Rect = pygame.Rect((x, y), (width, height))
        self.color = color
        self.border = border
        self.border_radius = border_radius

    def render(self):
        try:
            pygame.draw.rect(self._screen, self.color, self.rect, self.border, self.border_radius)
        except Exception as e:
            self._log.fatal(str(e))
            raise e
