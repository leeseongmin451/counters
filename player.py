import pygame
from controllers.mouse_controller import MouseEventListener


class Player:
    """
    An invisible player class

    It does not create instances.
    """

    cash = 1000000000000000

    control_camera = True
    cell_clickable = True
    button_clickable = True

    # Mouse and keyboard controls
    mouse = MouseEventListener()
    keys = pygame.key.get_pressed()

    @staticmethod
    def get_inputs():
        """
        Get all kind of events

        :return: None
        """

        pygame.event.get()

        # Get all kind of events generated from mouse
        Player.mouse.update()

        # Get all kind of events generated from keyboard
        Player.keys = pygame.key.get_pressed()

    @staticmethod
    def spend(cost):
        """
        Spend `cost` amount of cash

        :param cost: amount of cash to spend
        :return: None
        """

        Player.cash -= cost
