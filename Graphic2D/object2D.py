import pygame

import pygame

from Graphic2D.graphic2D import Graphic2DInstruments
from Graphic2D.textures import Textures

from logs import Logout
from utils import types_checking


class Object2D(Graphic2DInstruments):
    """
    Creates an object with a texture
    Inheritance is required for full functioning
    """

    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int = 0,
                 y: int = 0,
                 texture_x: int = 0,
                 texture_y: int = 0,
                 width: int = 50,
                 height: int = 50):
        """
        :param screen: application window
        :param log: logging object
        :param x: button x
        :param y: button y
        :param texture_x: texture x
        :param texture_y: texture y
        :param width: button width
        :param height: button height
        """
        super().__init__(screen, log, x, y)
        types_checking((screen, log, x, y, texture_x, texture_y, width, height),
                       (pygame.Surface, Logout, int, int, int, int, int, int))

        self._id: str = "no_texture"
        self._textures: list = Textures.get_images(self._id)
        self._textures_x = texture_x
        self._textures_y = texture_y

        self._hitbox: pygame.Rect = pygame.Rect((x, y), (width, height))

    def render(self):
        try:
            self._screen.blit(self._textures[0], self._get_texture_pos())
        except Exception as e:
            self._log.fatal(str(e))
            raise e

    def _get_texture_pos(self) -> tuple:
        return tuple(self._texture_x, self._texture_y)
