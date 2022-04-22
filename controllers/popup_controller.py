import pygame.sprite

from sprites.windows.popup_window import PopupWindow


class PopupController:
    """
    Controls popup windows
    """

    def __init__(self, *popup_windows: PopupWindow):
        """
        Initializing method
        """

        self.popup_window_list = list(popup_windows)
        self.current_showing_group = pygame.sprite.Group()

    def listen(self) -> None:
        """
        Listen to a specific event

        :return: None
        """

        # All popup windows must listen to events
        for window in self.popup_window_list:
            window.listen(self.current_showing_group)
