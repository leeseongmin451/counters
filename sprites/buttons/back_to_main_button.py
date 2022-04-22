from init import main_color, SCREEN_WIDTH, SCREEN_HEIGHT

from .button import Button

from scenes.scene import Scene


class BackToMainButton(Button):
    """
    Button for going back to main menu scene
    """

    def __init__(self):
        """
        Initializing method
        """

        Button.__init__(self, [SCREEN_WIDTH - 220, SCREEN_HEIGHT - 90, 200, 70], main_color)
        self.add_text("Back to Menu", (), "fonts/Quicksand-Medium.ttf", 20, "center", (100, 35))

    def operate(self) -> None:
        """
        BackToMainButton's own operation at clicking event
        :return: None
        """

        Scene.switch_to(Scene.MAINMENU_SCENE)
