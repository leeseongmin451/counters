import pygame

from constants.colors import WHITE3
from player import Player
from sprites.cells.counting_cell import COUNTER_CELL_W, COUNTER_CELL_H


class CountingCellInstallGuide(pygame.sprite.Sprite):
    """
    A guiding rectangle which follows mouse cursor to guide the installation position of CountingCell.
    """

    group = pygame.sprite.Group()

    def __init__(self):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self, self.group)

        # Image, size, shape, and rect attribute
        self.image = pygame.Surface((COUNTER_CELL_W, COUNTER_CELL_H))
        self.image.fill(WHITE3)
        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates this sprite every frame

        :return: None
        """

        mouse_state = Player.mouse
        self.rect.center = mouse_state.cursor.pos
