from constants.basic_settings import SCREEN_HEIGHT
from constants.colors import WHITE1
from player import Player
from sprites.texts.text import TextSurface


class PlayerCashText(TextSurface):
    """
    Text object for displaying player's current cash
    """

    def __init__(self):
        """
        Initializing method
        """

        TextSurface.__init__(self, "You have {} Cash.", (round(Player.cash), ), "fonts/Quicksand-SemiBold.ttf", 30, WHITE1, "bottomleft", (20, SCREEN_HEIGHT - 20))

    def update(self, mouse_state=None, key_state=None) -> None:
        """
        Update this text

        :param mouse_state: Mouse inputs
        :param key_state: Keyboard inputs
        :return: None
        """

        self.update_args((round(Player.cash), ))

        TextSurface.update(self)
