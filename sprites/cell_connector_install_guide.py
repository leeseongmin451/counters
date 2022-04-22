from typing import Tuple

import pygame

from constants.colors import *
from init import background_color
from player import Player
from utilities import trans_field_to_screen, get_difference, get_midpoint, get_pos_in_rect


class CellConnectorInstallGuide(pygame.sprite.Sprite):
    """
    A guiding line which follows mouse cursor to guide the installation position of CellConnector.
    """

    group = pygame.sprite.Group()

    def __init__(self, recv_from_pos: Tuple[int, int]):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self, self.group)

        self.recv_from_pos = recv_from_pos
        self.recv_from_pos_screen = trans_field_to_screen(self.recv_from_pos)
        self.send_to_pos_screen = (0, 0)
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates this sprite every frame

        :return: None
        """

        mouse_state = Player.mouse

        self.recv_from_pos_screen = trans_field_to_screen(self.recv_from_pos)
        self.send_to_pos_screen = mouse_state.cursor.pos

        x_diff, y_diff = get_difference(self.recv_from_pos_screen, self.send_to_pos_screen)

        self.image = pygame.Surface((x_diff, y_diff))
        self.image.set_colorkey(background_color)
        self.rect = self.image.get_rect(center=get_midpoint(self.recv_from_pos_screen, self.send_to_pos_screen))

        start_pos, end_pos = get_pos_in_rect(self.recv_from_pos_screen, self.send_to_pos_screen)
        pygame.draw.line(self.image, WHITE3, start_pos, end_pos, 4)
