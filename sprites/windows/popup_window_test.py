import pygame

from player import Player
from sprites.windows.popup_window import PopupWindow


class PopupWindowForTest(PopupWindow):
    """
    Just for test

    Appears at mouse click event, and its position is always on mouse pointer.
    """

    size = (100, 100)

    def __init__(self):
        """
        Initializing method
        """

        PopupWindow.__init__(self, self.size, self.get_pivot((0, 0)), (0, 0))

    def update(self) -> None:
        """
        Update all contents in this window

        :return: None
        """

        curspos = Player.mouse.cursor.pos

        self.rect = self.set_position(self.get_pivot(curspos), curspos)

        PopupWindow.update(self)

    def listen(self, group: pygame.sprite.Group) -> None:
        """
        PopupWindowForTest's own method of listening events

        :param group: Sprite group which this window belongs to
        :return: None
        """

        mouse_state = Player.mouse
        if mouse_state.left.clicked:
            if self.popped_up:
                self.popdown(group)
            else:
                self.popup(group)
