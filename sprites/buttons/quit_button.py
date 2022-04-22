import init
from init import main_color

from .button import Button


class QuitButton(Button):
    """
    Button for terminating game, displayed in main menu
    """

    def __init__(self):
        """
        Initializing method
        """

        Button.__init__(self, [760, 950, 400, 100], main_color)
        self.add_text("QUIT GAME", (), "fonts/Quicksand-SemiBold.ttf", 50, "center", (200, 50))

    def operate(self) -> None:
        """
        QuitButton's own operation at clicking event
        :return: None
        """

        init.running = False
