from init import *
from typing import *
from abc import ABC, abstractmethod

from player import Player
from sprites.texts.text import TextSurface


class Button(ABC, pygame.sprite.Sprite):
    """
    A rectangular button class
    """

    group = pygame.sprite.Group()       # Button's own sprite group

    def __init__(self, rect: List[int], btn_color: Union[List[int], Tuple[int, int, int]], default_back_color=background_color):
        """
        Initialize and apply basic settings to button

        :param rect: position and rectangular size of button
        :param btn_color: color of button boundary and text
        :param default_back_color: color of background of button, default value is black(0, 0, 0)
        """

        pygame.sprite.Sprite.__init__(self, self.group)

        # Surface object for this button
        self.image = pygame.Surface(rect[2:])

        # Rect attribute
        self.rect = pygame.Rect(rect)

        # Text attribute
        self.text_list = []
        self.text_group = pygame.sprite.Group()

        # Color attrubutes
        self.active_color = btn_color

        # Background color attributes
        # Default color is the darkest color
        self.default_back_color = default_back_color
        # Hovered color displayed when cursor is in rect has half brightness of active color
        self.hovered_back_color = ((self.active_color[0] + self.default_back_color[0]) // 2,
                                   (self.active_color[1] + self.default_back_color[1]) // 2,
                                   (self.active_color[2] + self.default_back_color[2]) // 2)
        # Clicked color displayed when the button is pressed has half brightness of hovered color
        self.clicked_back_color = ((self.hovered_back_color[0] + self.default_back_color[0]) // 2,
                                   (self.hovered_back_color[1] + self.default_back_color[1]) // 2,
                                   (self.hovered_back_color[2] + self.default_back_color[2]) // 2)
        # Set initial color of button
        self.current_color = self.active_color
        self.current_back_color = self.default_back_color
        self.inactive_color = self.hovered_back_color

        # Boolean values for button control
        self.active = True
        self.cursor_in_rect = False
        self.drag_enter = False
        self.clickable = False

    def add_text(self, text: str, text_args: Tuple, font: str, font_size: int, pivot: str, position: Tuple[int, int]):
        """
        Add a new text surface to this button

        :return: None
        """

        new_text = TextSurface(text, text_args, font, font_size, self.active_color, pivot, position)
        self.text_list.append(new_text)
        self.text_group.add(new_text)

    def remove_text(self, index: int) -> None:
        """
        Select a text surface by index and remove it from this button

        :return: None
        """

        text_to_remove = self.text_list[index]
        text_to_remove.kill()
        del self.text_list[index]

    def update_image(self, button_color, button_background_color):
        """
        Update the appearance of this button at certain event

        :param button_color: Color of borderline and text of this button to update
        :param button_background_color: Background color of this button to update
        :return: None
        """

        pygame.draw.rect(self.image, button_background_color, [0, 0, self.rect.w, self.rect.h])
        pygame.draw.rect(self.image, button_color, [0, 0, self.rect.w, self.rect.h], 3)
        self.update_text_color(button_color)
        self.text_group.update()
        self.text_group.draw(self.image)

    def update_text_color(self, new_color):
        """
        Update color of all texts and draw them in this button

        :return: None
        """

        for text in self.text_list:
            text.update_color(new_color)

    def update_text_args(self, index, new_text_args):
        """
        Update value of arguments of selected text using index number

        :return: None
        """

        self.text_list[index].update_args(new_text_args)

    def activate(self) -> None:
        """
        Make button active(clickable)
        :return: None
        """

        self.current_color = self.active_color
        # Rerender text surface with newly set color
        self.active = True      # Update method will be executed

        self.update_image(self.current_color, self.current_back_color)  # Update image of this button

    def deactivate(self) -> None:
        """
        Make button inactive(not clickable)
        :return:
        """

        self.current_color = self.inactive_color
        # Rerender text surface with newly set color
        self.active = False     # Update method will be passed
        self.current_back_color = self.default_back_color

        self.update_image(self.current_color, self.current_back_color)  # Update image of this button

    def update(self) -> None:
        """
        Updating method needed for all sprite class

        Check whether cursor is in button or clicked the button when button is active(clickable).
        Only if click-and-release the button, operate() method will be executed.

        :return: None
        """

        mouse_state = Player.mouse

        if self.active:
            self.current_color = self.active_color
            self.current_back_color = self.default_back_color
            self.clickable = False

            if not self.cursor_in_rect and self.rect.collidepoint(*mouse_state.cursor.pos):
                self.drag_enter = mouse_state.left.holding
                self.cursor_in_rect = True

            if self.cursor_in_rect and not self.rect.collidepoint(*mouse_state.cursor.pos):
                self.drag_enter = False
                self.cursor_in_rect = False
                self.clickable = False

            if self.cursor_in_rect:
                if self.drag_enter:
                    if mouse_state.left.release:
                        self.drag_enter = False
                else:
                    self.clickable = True
                    self.current_back_color = self.hovered_back_color

            if self.clickable:
                if mouse_state.left.holding:
                    self.current_back_color = self.clicked_back_color
                elif mouse_state.left.clicked:
                    self.operate()

        else:
            self.current_color = self.inactive_color
            self.current_back_color = self.default_back_color

        self.update_image(self.current_color, self.current_back_color)

    @abstractmethod
    def operate(self) -> None:
        """
        Button's specific function will be defined here.
        Child button classes will have specific functions by overriding this method
        :return: None
        """

        pass
