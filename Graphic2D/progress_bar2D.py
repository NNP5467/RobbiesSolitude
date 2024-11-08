import pygame

from Graphic2D.object2D import Object2D
from Graphic2D.textures import Textures

from logs import Logout


class ProgressBar2D(Object2D):
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 size: int = 100,
                 x: int = 0,
                 y: int = 0,
                 texture_x: int = 0,
                 texture_y: int = 0,
                 width: int = 50,
                 height: int = 50):
        super().__init__(screen, log, x, y, texture_x, texture_y, width, height)

        self._size = size
        self.__score = 1
        self.__current_image = 0

    def render(self):
        if len(self._textures) == 0:
            self._log.warn("Progress bar render: index out of range")
            self._textures = Textures.get_images("no_texture")
        try:
            self._screen.blit(self._textures[self.__current_image], self._get_texture_pos())
        except Exception as e:
            self._log.fatal(e)
            raise e

    @property
    def _current_image(self) -> int:
        return self.__current_image
        
    @property
    def _score(self) -> int:
        return self.__score
    
    @_score.setter
    def _score(self, value: int) -> None:
        self.__score = value

        if self.__score > self._size:
            self.__score = self._size
        elif self.__score < 1:
            self.__score = 1

        self.__current_image = int(len(self._textures) * (self.__score / self._size) - 1 / self._size)
        self._log.debug(self.__score, "|", self.__current_image, "|", value)
