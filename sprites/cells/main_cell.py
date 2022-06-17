from .counting_cell import *
from utilities import tetration_log10


class MainCell(CountingCell):
    """
    Only receives number, doesn't transmit in local group.
    """

    def __init__(self):
        """
        Initializing method
        """

        CountingCell.__init__(self)

        self.width = 400
        self.height = 250
        self.image = pygame.Surface((self.width, self.height))

        self.rect = self.image.get_rect(center=(round(self.screen_pos[0]), round(self.screen_pos[1])))

        self.remove_text(0)
        self.add_text("{}", (self.number, ), "fonts/Quicksand-Bold.ttf", 30, "center", (self.width // 2, self.height // 2 - 20))
        self.add_text("= 10^^{}", (round(tetration_log10(self.number), 4), ), "fonts/Quicksand-Bold.ttf", 30, "center", (self.width // 2, self.height // 2 + 20))

    def update(self):
        """
        Updates this sprite every frame

        :return: None
        """

        mouse_state = Player.mouse

        self.update_text_args(0, (round(self.number, ROUNDING_DIGITS), ))
        self.update_text_args(1, (round(tetration_log10(self.number), 4), ))
        Button.update(self)

        self.screen_pos = trans_field_to_screen(self.field_pos)
        self.rect.center = (round(self.screen_pos[0]), round(self.screen_pos[1]))

        if self.selected and not mouse_state.left.clicked:
            self.selected = False
