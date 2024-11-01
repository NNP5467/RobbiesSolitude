import pygame

from logs import Logout


class Graphic2DInstruments:  # This class is more like an interface
    """Created EXCLUSIVELY for classes of the Graphic2D category"""
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int,
                 y: int):
        self._x = x
        self._y = y
        self._screen = screen
        self._log = log

    def render(self):
        """Object rendering logic"""
        pass  # You need to overwrite this method when inheriting


class Graphic2D:
    def __init__(self):
        self.obj: Graphic2DInstruments | None = None  # There shouldn't be None, this must be redefined during inheritance

    def draw(self):
        """Draw the object"""
        self.obj.render()
