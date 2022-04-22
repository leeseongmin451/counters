import init
from init import *

from utilities import trans_field_to_screen
from sprites.cells.counting_cell import CountingCell


class CellConnector(pygame.sprite.Sprite):
    """
    A line-shaped sprite which sends number from one cell to another.
    """

    group = pygame.sprite.Group()

    cost = 5
    cost_multiplier = 1.1

    def __init__(self, recv_from: CountingCell, send_to: CountingCell):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self, self.group)

        # CellConnector sends number from 'recv_from' cell to 'send_to' cell
        self.recv_from = recv_from
        self.send_to = send_to

        self.recv_pos = self.recv_from.field_pos
        self.send_pos = self.send_to.field_pos

        rect_w = abs(self.recv_pos[0] - self.send_pos[0])
        rect_h = abs(self.recv_pos[1] - self.send_pos[1])
        self.image = pygame.Surface((rect_w, rect_h))
        self.image.set_colorkey(background_color)

        x_offset = min(self.recv_pos[0], self.send_pos[0])
        y_offset = min(self.recv_pos[1], self.send_pos[1])
        line_start_pos = (self.recv_pos[0] - x_offset, self.recv_pos[1] - y_offset)
        line_end_pos = (self.send_pos[0] - x_offset, self.send_pos[1] - y_offset)
        pygame.draw.line(self.image, main_color, line_start_pos, line_end_pos, 4)

        self.field_pos = ((self.recv_pos[0] + self.send_pos[0]) // 2,
                          (self.recv_pos[1] + self.send_pos[1]) // 2)
        self.screen_pos = trans_field_to_screen(self.field_pos)
        self.rect = self.image.get_rect(center=self.screen_pos)

        self.send_interval = 1      # Sending interval in seconds

    def update(self) -> None:
        """
        Updating method needed for all sprite class

        Sends number from 'recv_from' cell to 'send_to' cell

        :return: None
        """

        self.screen_pos = trans_field_to_screen(self.field_pos)
        self.rect.center = self.screen_pos

        self.send_to.number += self.recv_from.number * self.send_interval * init.DELTA_TIME

    @staticmethod
    def raise_cost():
        CellConnector.cost *= CellConnector.cost_multiplier

    @staticmethod
    def lower_cost():
        CellConnector.cost /= CellConnector.cost_multiplier
