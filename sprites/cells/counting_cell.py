from constants.basic_settings import ROUNDING_DIGITS
from init import *
from player import Player
from sprites.buttons.button import Button
from utilities import trans_field_to_screen


COUNTER_CELL_W = 200
COUNTER_CELL_H = 100


class CountingCell(Button):
    """
    A cell sprite which counts number one by one.
    """

    group = pygame.sprite.Group()

    INITIAL_BUYING_COST = 20
    buying_cost = INITIAL_BUYING_COST
    BUYING_COST_MULTIPLIER = 1.1

    INITIAL_UPGRADE_COST = 30
    upgrade_cost = INITIAL_UPGRADE_COST
    UPGRADE_COST_MULTIPLIER = 1.1

    CELL_NUMBER_MULTIPLIER = 2

    def __init__(self, field_pos=(0, 0)):
        """
        Initializing method
        """

        self.field_pos = field_pos
        self.screen_pos = trans_field_to_screen(self.field_pos)

        self.width = COUNTER_CELL_W
        self.height = COUNTER_CELL_H


        topleft_x = self.screen_pos[0] - self.width // 2
        topleft_y = self.screen_pos[1] - self.height // 2
        rect = [topleft_x, topleft_y, self.width, self.height]
        Button.__init__(self, rect, main_color)
        self.add(self.group)

        self.number = 1
        self.add_text("{}", (round(self.number, ROUNDING_DIGITS), ), "fonts/Quicksand-Bold.ttf", 15, "center", (self.width // 2, self.height // 2))


        self.worth = 0

        self.connect_to_list = []       # List of cells which this cell sends its number to
        self.connect_from_list = []     # List of cells which this cell receives number from


        self.distance_from_main = 0     # Number of CellConnectors from MainCell to itself

        self.current_operation = self.operate_upgrade
        self.selected = False

    def update(self):
        """
        Updates this sprite every frame

        :return: None
        """

        mouse_state = Player.mouse

        self.update_text_args(0, (round(self.number, ROUNDING_DIGITS), ))
        Button.update(self)

        self.screen_pos = trans_field_to_screen(self.field_pos)
        self.rect.center = (round(self.screen_pos[0]), round(self.screen_pos[1]))

        if self.selected and not mouse_state.left.clicked:
            self.selected = False

    def operate_upgrade(self):
        pass

    def operate_connect(self):
        pass

    current_operation = operate_upgrade

    def operate(self) -> None:
        """
        CountingCell's own operation at clicking event
        :return: None
        """

        self.selected = True
        CountingCell.current_operation(self)

    def remove_from_network(self) -> None:
        """
        Remove cell from network

        It also removes all of its direct connectors.

        :return: None
        """



    @staticmethod
    def raise_cost():
        CountingCell.buying_cost *= CountingCell.BUYING_COST_MULTIPLIER

    @staticmethod
    def lower_cost():
        CountingCell.buying_cost /= CountingCell.BUYING_COST_MULTIPLIER
