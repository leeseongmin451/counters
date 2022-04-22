import pygame
import time
import copy


# Index constants for mouse button specification
LEFT = 0
MIDDLE = 1
RIGHT = 2


class MouseEventListener:
    """
    Catches all events generated from mouse
    """

    def __init__(self):
        """
        Initializing method
        """

        self.left = MouseButton(LEFT)
        self.middle = MouseButton(MIDDLE)
        self.right = MouseButton(RIGHT)
        self.cursor = MousePosition()

        self.dragged = False

    def update(self) -> None:
        """
        Update mouse status

        :return: None
        """

        self.check_dragging()

        self.left.update()
        self.middle.update()
        self.right.update()
        self.cursor.update()

    def check_dragging(self) -> None:
        """
        Check mouse dragging event

        :return: None
        """

        if self.left.holding and self.cursor.moved and not self.dragged:
            self.dragged = True

        if self.dragged and self.left.release:
            self.dragged = False


class MouseButton:
    """
    Catches all events generated from particular mouse button
    """

    DOUBLECLICK_TERM = 0.2

    def __init__(self, btn_type: int):
        """
        Initializing method
        """

        self.btn_type = btn_type

        self.pressed = False
        self.holding = False
        self.release = False
        self.clicked = False
        self.dbclick = False

        self.first_release = False
        self.released_time = 0

        self.held_last = self.holding

    def update(self) -> None:
        """
        Update status of this button

        :return: None
        """

        self.pressed = False
        self.release = False
        self.clicked = False
        self.dbclick = False

        self.holding = pygame.mouse.get_pressed()[self.btn_type]

        if not self.held_last and self.holding:
            self.pressed = True

        if self.held_last and not self.holding:
            self.release = True

            if not self.first_release:
                self.first_release = True
                self.clicked = True
                self.released_time = time.time()

            else:
                self.first_release = False
                self.dbclick = True

        if self.first_release and time.time() - self.released_time > MouseButton.DOUBLECLICK_TERM:
            self.first_release = False

        self.held_last = self.holding


class MousePosition:
    """
    Catches all events generated by moving cursor
    """

    def __init__(self):
        """
        Initializing method
        """

        self.pos = (0, 0)
        self.moved = False
        self.delta = (0, 0)

        self.last_pos = copy.copy(self.pos)

    def update(self) -> None:
        """
        Update status of cursor position

        :return: None
        """

        self.pos = pygame.mouse.get_pos()

        self.moved = self.pos != self.last_pos
        self.delta = (self.pos[0] - self.last_pos[0],
                      self.pos[1] - self.last_pos[1])

        self.last_pos = copy.copy(self.pos)
