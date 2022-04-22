from controllers.connector_generation_controller import ConnectorGenerationController
from init import main_color

from player import Player
from .button import Button
from ..cell_connector import CellConnector


class AddNewConnectorButton(Button):
    """
    Button for adding new CountingCell
    """

    def __init__(self):
        """
        Initializing method
        """

        Button.__init__(self, [240, 20, 200, 70], main_color)
        self.add_text("Add New Connector", (), "fonts/Quicksand-Medium.ttf", 20, "center", (100, 30))
        self.add_text("Cost: {}", (round(CellConnector.cost), ), "fonts/Quicksand-Medium.ttf", 15, "center", (100, 50))

        self.controller = None

    def update(self) -> None:
        """
        Overriding method

        :return: None
        """

        if not self.controller:
            if self.active and CellConnector.cost > Player.cash:
                self.deactivate()
            if not self.active and CellConnector.cost <= Player.cash:
                self.activate()

        Button.update(self)

        if self.controller:
            self.controller.update()

            if self.controller.state == "receiver_selected":
                self.controller = None
                self.update_text_args(1, (round(CellConnector.cost), ))
                self.activate()

    def operate(self) -> None:
        """
        AddNewConnectorButton's own operation at clicking event
        :return: None
        """

        self.controller = ConnectorGenerationController()
        self.deactivate()
