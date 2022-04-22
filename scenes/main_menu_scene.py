from sprites.buttons.start_button import StartButton
from sprites.buttons.quit_button import QuitButton
from sprites.texts.main_menu_title_text import MainMenuTitleText

from .scene import *


button_group = pygame.sprite.Group(
    StartButton(),
    QuitButton()
)

text_group = pygame.sprite.Group(
    MainMenuTitleText()
)


class MainMenuScene(Scene):
    """
    A scene displayed when starting game
    """

    def __init__(self):
        """
        Initializing method
        """

        Scene.__init__(self, Scene.MAINMENU_SCENE)

        self.add_group(button_group)
        self.add_group(text_group)
        self.add_group(self.popup_controller.current_showing_group)
