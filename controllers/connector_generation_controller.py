from typing import Union

import pygame

from player import Player
from sprites.cell_connector import CellConnector
from sprites.cell_connector_install_guide import CellConnectorInstallGuide
from sprites.cells.counting_cell import CountingCell
from sprites.cells.main_cell import MainCell


class ConnectorGenerationController:
    """
    Guides connecting two cells.

    Activated by AddNewConnectorButton.
    """

    def __init__(self):
        """
        Initializing method
        """

        # init, sender_selected, receiver_selected
        self.state = "init"

        self.available_cells = pygame.sprite.Group()

        self.selected_sender: Union[None, CountingCell] = None
        self.selected_receiver: Union[None, CountingCell] = None

        self.connector_guide: Union[None, CellConnectorInstallGuide] = None

        # Turn off all cells except connectable ones
        """
        for cell in CountingCell.group:
            if isinstance(cell, MainCell) or cell.distance_from_main == 1:
                cell.deactivate()
            elif cell.distance_from_main == 0:
                self.available_cells.add(cell)
            else:
                all_connected = True
                for c in CountingCell.group:
                    if c.distance_from_main == cell.distance_from_main - 1 and c not in cell.connect_to_list:
                        self.available_cells.add(cell)
                        all_connected = False
                        break
                if all_connected:
                    cell.deactivate()
        """

        # All CountingCells' operation will be "connect"
        CountingCell.current_operation = CountingCell.operate_connect

    def update(self):
        """
        Updates ConnectorGenerationController every frame

        :return: None
        """

        mouse_state = Player.mouse
        key_state = Player.keys
        ##################################################################################################
        """
        if self.state == "init" and mouse_state.left.clicked:
            for cell in self.available_cells:
                if cell.selected:
                    self.selected_sender = cell
                    self.state = "sender_selected"
                    self.connector_guide = CellConnectorInstallGuide(cell.field_pos)
                    cell.selected = False

                    # Turn off all cells in self.available_cells
                    for c in self.available_cells:
                        c.deactivate()
                    self.available_cells.empty()

                    # Turn on all cells connectable with selected sender
                    if cell.distance_from_main == 0:
                        for c in CountingCell.group:
                            if c.distance_from_main != cell.distance_from_main or isinstance(c, MainCell):
                                self.available_cells.add(c)
                                c.activate()
                    else:
                        for c in CountingCell.group:
                            if c.distance_from_main + 1 == cell.distance_from_main and c not in cell.connect_to_list:
                                self.available_cells.add(c)
                                c.activate()

                    # A cell cannot connect to itself.
                    cell.deactivate()
                    break

        elif self.state == "sender_selected":
            self.connector_guide.update()

            if mouse_state.left.clicked:
                for cell in self.available_cells:
                    if cell.selected and cell != self.selected_sender:
                        self.selected_receiver = cell
                        cell.selected = False

                        self.install_connector()
                        self.terminate()
                        break
        """
        ##################################################################################################
        if self.state == "init" and mouse_state.left.clicked:
            for cell in CountingCell.group:
                if cell.selected:
                    self.selected_sender = cell
                    self.state = "sender_selected"
                    self.connector_guide = CellConnectorInstallGuide(cell.field_pos)
                    cell.selected = False

        elif self.state == "sender_selected":
            self.connector_guide.update()

            if mouse_state.left.clicked:
                for cell in CountingCell.group:
                    if cell.selected and cell != self.selected_sender:
                        self.selected_receiver = cell
                        cell.selected = False

                        self.install_connector()
                        self.terminate()
                        break
        ##################################################################################################
        if key_state[pygame.K_ESCAPE]:
            self.terminate()

    def install_connector(self):
        """
        Actually generate connector

        :return: None
        """

        CellConnector(self.selected_sender, self.selected_receiver)
        self.selected_sender.connect_to_list.append(self.selected_receiver)
        self.selected_receiver.connect_from_list.append(self.selected_sender)
        self.selected_sender.distance_from_main = self.selected_receiver.distance_from_main + 1

        Player.spend(CellConnector.cost)
        CellConnector.raise_cost()

    def terminate(self):
        """
        Terminates this controller

        :return: None
        """

        self.state = "receiver_selected"

        for c in CountingCell.group:
            c.activate()

        if self.connector_guide:
            self.connector_guide.kill()
        CellConnectorInstallGuide.group.empty()

        CountingCell.current_operation = CountingCell.operate_upgrade
