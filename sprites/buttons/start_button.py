from init import main_color

from .button import Button

from scenes.scene import Scene


class StartButton(Button):
    """
    Button for starting game, displayed in main menu
    """

    def __init__(self):
        """
        Initializing method
        """

        Button.__init__(self, [560, 700, 800, 200], main_color)
        self.add_text("START GAME", (), "fonts/Quicksand-SemiBold.ttf", 100, "center", (400, 100))

    def operate(self) -> None:
        """
        StartButton's own operation at clicking event
        :return: None
        """

        Scene.switch_to(Scene.GAMEPLAY_SCENE)
