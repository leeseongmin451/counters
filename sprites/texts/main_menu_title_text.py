from constants.basic_settings import SCREEN_WIDTH
from constants.colors import WHITE1
from sprites.texts.text import TextSurface


class MainMenuTitleText(TextSurface):
    """
    Text object for displaying game title
    """

    def __init__(self):
        """
        Initializing method
        """

        TextSurface.__init__(self, "COUNTERS", (), "fonts/Quicksand-SemiBold.ttf", 200, WHITE1, "center", (SCREEN_WIDTH // 2, 200))
