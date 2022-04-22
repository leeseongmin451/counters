import pygame

from constants.colors import *
from player import Player
from sprites.cells.counting_cell import CountingCell
from sprites.cells.counting_cell_install_guide import CountingCellInstallGuide
from utilities import trans_screen_to_field


class CellGenerationController:
    """
    Guides adding a new cell.

    Activated by AddNewCellButton.
    """

    def __init__(self):
        """
        Initializing method
        """

        # init, pos selecting, finished
        self.state = "init"

        self.overlap = False  # Indicates whether is overlaps any of CountingCells

        self.cell_guide = CountingCellInstallGuide()

        for cell in CountingCell.group:
            cell.deactivate()

    def update(self):
        """
        Updates ConnectorGenerationController every frame

        :return: None
        """

        mouse_state = Player.mouse
        key_state = Player.keys

        self.cell_guide.update()

        if pygame.sprite.spritecollide(self.cell_guide, CountingCell.group, False):
            self.cell_guide.image.fill(RED2)
            self.overlap = True
        else:
            self.cell_guide.image.fill(WHITE3)
            self.overlap = False

        if self.state == "pos selecting" and not self.overlap and \
                mouse_state.left.clicked and not mouse_state.dragged:

            self.install_cell(mouse_state.cursor.pos)
            self.terminate()

        if key_state[pygame.K_ESCAPE]:
            self.terminate()

        if self.state == "init":
            self.state = "pos selecting"

    @staticmethod
    def install_cell(curpos):
        """
        Actually generate CountingCell

        :return: None
        """

        new_cell_field_pos = trans_screen_to_field(curpos)
        CountingCell(new_cell_field_pos)
        Player.spend(CountingCell.INITIAL_BUYING_COST)
        CountingCell.raise_cost()

    def terminate(self):
        """
        Terminates this controller

        :return: None
        """

        self.state = "finished"

        for cell in CountingCell.group:
            cell.activate()

        self.cell_guide.kill()
        CountingCellInstallGuide.group.empty()
