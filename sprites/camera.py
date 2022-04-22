from init import *
from player import Player


class Camera(pygame.sprite.Sprite):
    """
    An invisible camera class.
    """

    def __init__(self):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self)

        self.center_x = self.center_y = 0   # Position in field where camera looking at

    def update(self):
        """
        Updates this sprite every frame

        :return: None
        """

        # Move camera position when dragging cursor.
        mouse_state = Player.mouse
        if mouse_state.left.holding:
            self.center_x -= mouse_state.cursor.delta[0]
            self.center_y -= mouse_state.cursor.delta[1]
