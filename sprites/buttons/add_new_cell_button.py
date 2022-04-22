from controllers.cell_generation_controller import CellGenerationController
from init import main_color
from player import Player

from .button import Button
from ..cells.counting_cell import CountingCell


class AddNewCellButton(Button):
    """
    Button for adding new CountingCell
    """

    def __init__(self):
        """
        Initializing method
        """

        Button.__init__(self, [20, 20, 200, 70], main_color)
        self.add_text("Add New Cell", (), "fonts/Quicksand-Medium.ttf", 20, "center", (100, 30))
        self.add_text("Cost: {}", (round(CountingCell.INITIAL_BUYING_COST),), "fonts/Quicksand-Medium.ttf", 15, "center", (100, 50))

        self.controller = None

    def update(self) -> None:
        """
        Overriding method

        :return: None
        """

        if not self.controller:
            if self.active and CountingCell.buying_cost > Player.cash:
                self.deactivate()
            if not self.active and CountingCell.buying_cost <= Player.cash:
                self.activate()

        Button.update(self)

        if self.controller:
            self.controller.update()

            if self.controller.state == "finished":
                self.controller = None
                self.update_text_args(1, (round(CountingCell.buying_cost),))
                self.activate()

    def operate(self) -> None:
        """
        AddNewCellButton's own operation at clicking event
        :return: None
        """

        self.controller = CellGenerationController()
        self.deactivate()
