from typing import Tuple

import pygame

from Graphic2D.graphic2D import Graphic2DInstruments
from logs import Logout


class Button2D(Graphic2DInstruments):
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int = 0,
                 y: int = 0,
                 width: int = 100,
                 height: int = 50,
                 colors: Tuple[Tuple[int, int, int], Tuple[int, int, int]] = ((100, 100, 100), (150, 150, 150))):
        super().__init__(screen, log, x, y)
        self.rect: pygame.Rect = pygame.Rect((x, y), (width, height))
        self.colors = colors
        self.is_hover: bool = self.rect.collidepoint(pygame.mouse.get_pos())

    def render(self):
        try:
            self.is_hover = self.rect.collidepoint(pygame.mouse.get_pos())

            pygame.draw.rect(self._screen, self.colors[1 if self.is_hover else 0], self.rect)
        except Exception as e:
            self._log.fatal(str(e))
            raise e
