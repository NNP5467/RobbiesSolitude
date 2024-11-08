import pygame

from Graphic2D.object2D import Object2D

from logs import Logout


class Button2D(Object2D):
    """
    Creates a button without functionality
    Inheritance is required for full functioning
    """
    
    def __init__(self,
                 screen: pygame.Surface,
                 log: Logout,
                 x: int = 0,
                 y: int = 0,
                 texture_x: int = 0,
                 texture_y: int = 0,
                 width: int = 100,
                 height: int = 50):
        super().__init__(screen, log, x, y, texture_x, texture_y, width, height)
        
        self._is_hover: bool = self._hitbox.collidepoint(pygame.mouse.get_pos())

    def render(self) -> None:
        try:
            self._is_hover = self.hitbox.collidepoint(pygame.mouse.get_pos())
            if self._is_hover:
                self._screen.blit(self._textures[len(self._textures)-1], self._get_textures_pos())
            else:
                self._screen.blit(self._textures[0], self._get_textures_pos())
        except Exception as e:
            self._log.fatal(e)
            raise e

    def check_pressed(self, event: pygame.event.Event) -> None:
        """
        This method checks the button press
        (The method must be redefined)

        :param event: current event
        """
        pass
