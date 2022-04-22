from .counting_cell import *


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
        self.add_text("{}", (self.number, ), "fonts/Quicksand-Bold.ttf", 30, "center", (self.width // 2, self.height // 2))
