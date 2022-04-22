import pygame

from controllers.popup_controller import PopupController
from sprites.windows.popup_window import PopupWindow


class Scene:
    """

    """

    # Scene numbers
    MAINMENU_SCENE = 0
    GAMEPLAY_SCENE = 1

    scene_dict = {}
    current_displaying_scene = MAINMENU_SCENE

    def __init__(self, scene_number: int, *popup_windows: PopupWindow):
        """
        Initializing method
        """

        # Subgroup of sprites needed for update and ordered drawing
        self.sprite_groups = []

        # Popup window controller
        self.popup_controller = PopupController(*popup_windows)

        self.scene_dict[scene_number] = self

    def add_group(self, sprite_group: pygame.sprite.Group) -> None:
        """
        Add a new group of sprite

        :param sprite_group: New sprite group to add
        :return: None
        """

        self.sprite_groups.append(sprite_group)

    def update(self) -> None:
        """
        Update all sprites in this scene

        :return: None
        """

        for group in self.sprite_groups:
            group.update()
        self.popup_controller.listen()

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw all sprites in this scene on the given surface

        :param surface: Surface to draw things on
        :return: None
        """

        for group in self.sprite_groups:
            group.draw(surface)

    @staticmethod
    def update_current() -> None:
        """
        Update current displaying scene

        :return: None
        """

        Scene.scene_dict[Scene.current_displaying_scene].update()

    @staticmethod
    def draw_current(surface: pygame.Surface) -> None:
        """
        Draw current displaying scene

        :param surface: Surface to draw things on
        :return: None
        """

        Scene.scene_dict[Scene.current_displaying_scene].draw(surface)

    @staticmethod
    def switch_to(scene_number) -> None:
        """
        Switch to another scene

        :param scene_number: Number of scene to switch to
        :return: None
        """

        Scene.current_displaying_scene = scene_number
