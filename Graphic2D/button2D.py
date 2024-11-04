import pygame

from Graphic2D.graphic2D import Graphic2DInstruments
from Graphic2D.textures import Textures
from logs import Logout


class Button2D(Graphic2DInstruments):
    """Creates a button without functionality"""
    
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int = 0,
                 y: int = 0,
                 texture_x: int = 0,
                 texture_y: int = 0,
                 width: int = 100,
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

        self._id: str = "no_texture"
        self._textures: Textures = Textures.get_images(self._id)
        self._texture_x: int = texture_x
        self._texture_y: int = texture_y

        self.rect: pygame.Rect = pygame.Rect((x, y), (width, height))
        self.is_hover: bool = self.rect.collidepoint(pygame.mouse.get_pos())

    def render(self) -> None:
        try:
            self.is_hover = self.rect.collidepoint(pygame.mouse.get_pos())
            if self.is_hover:
                self._screen.blit(self._textures[len(self._textures)-1], self.__get_textures())
            else:
                self._screen.blit(self._textures[0], self.__get_textures())
        except Exception as e:
            self._log.fatal(str(e))
            raise e

    def check_pressed(self, event: pygame.event.Event) -> None:
        """
        This method checks the button press
        (The method must be redefined)

        :param event: current event
        """
        pass

    def __get_textures(self):
        return (self._texture_x, self._texture_y)
