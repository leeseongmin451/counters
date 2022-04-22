from sprites.cells.counting_cell import CountingCell
from sprites.cells.counting_cell_install_guide import CountingCellInstallGuide
from sprites.cell_connector_install_guide import CellConnectorInstallGuide
from sprites.cell_connector import CellConnector

from sprites.buttons.add_new_cell_button import AddNewCellButton
from sprites.buttons.add_new_connector_button import AddNewConnectorButton
from sprites.buttons.back_to_main_button import BackToMainButton

from sprites.cells.main_cell import MainCell
from sprites.texts.player_cash_text import PlayerCashText
from utilities import camera

from .scene import *


main_cell = MainCell()

button_group = pygame.sprite.Group(
    AddNewCellButton(),
    AddNewConnectorButton(),
    BackToMainButton()
)

text_group = pygame.sprite.Group(
    PlayerCashText()
)


class GamePlayScene(Scene):
    """
    A scene displayed during gameplay
    """

    def __init__(self):
        """
        Initializing method
        """

        Scene.__init__(self, Scene.GAMEPLAY_SCENE)

        self.add_group(CellConnector.group)
        self.add_group(CellConnectorInstallGuide.group)
        self.add_group(CountingCell.group)
        self.add_group(CountingCellInstallGuide.group)
        self.add_group(button_group)
        self.add_group(text_group)

        self.camera = camera

    def update(self) -> None:
        """
        Overriding method

        :return: None
        """

        Scene.update(self)
        self.camera.update()
