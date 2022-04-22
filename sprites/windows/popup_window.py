from typing import Tuple, List
from abc import ABC, abstractmethod

import pygame.sprite

from constants.basic_settings import SCREEN_WIDTH, SCREEN_HEIGHT
from init import background_color, main_color
from sprites.buttons.button import Button
from sprites.texts.text import TextSurface


class PopupWindow(ABC, pygame.sprite.Sprite):
    """
    A rectangular window sprite which pops up in a scene

    It can contain any number of texts and buttons.
    """

    def __init__(self, size: Tuple[int, int], pivot: str, position: Tuple[int, int]):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.pivot = pivot
        self.position = position
        self.image = pygame.Surface(self.size)
        self.rect = self.set_position(self.pivot, self.position)

        self.text_list: List[TextSurface] = []
        self.text_group = pygame.sprite.Group()
        self.button_list: List[Button] = []
        self.button_group = pygame.sprite.Group()

        self.popped_up = False

    def get_pivot(self, position: Tuple[int, int]) -> str:
        """
        Returns a pivot string based on given position

        :return: pivot
        """

        x_pivot = "right" if position[0] > SCREEN_WIDTH - self.size[0] else "left"
        y_pivot = "bottom" if position[1] > SCREEN_HEIGHT - self.size[1] else "top"

        return y_pivot + x_pivot

    def set_position(self, pivot: str, position: Tuple[int, int]) -> pygame.Rect:
        """
        Set position of this window

        :param pivot: A fixpoint of text rect to set
        :param position: position
        :return: Rect object of this text sprite
        """

        self.pivot = pivot
        self.position = position

        if self.pivot == "topleft":
            return self.image.get_rect(topleft=self.position)
        elif self.pivot == "midtop":
            return self.image.get_rect(midtop=self.position)
        elif self.pivot == "topright":
            return self.image.get_rect(topright=self.position)
        elif self.pivot == "midleft":
            return self.image.get_rect(midleft=self.position)
        elif self.pivot == "center":
            return self.image.get_rect(center=self.position)
        elif self.pivot == "midright":
            return self.image.get_rect(midright=self.position)
        elif self.pivot == "bottomleft":
            return self.image.get_rect(bottomleft=self.position)
        elif self.pivot == "midbottom":
            return self.image.get_rect(midbottom=self.position)
        elif self.pivot == "bottomright":
            return self.image.get_rect(bottomright=self.position)

    def add_text(self, new_text: TextSurface):
        """
        Add a new text surface in this window as a content

        :return: None
        """

        self.text_list.append(new_text)
        self.text_group.add(new_text)

    def add_button(self, new_button: Button):
        """
        Add a new button in this window as a content

        :return: None
        """

        self.button_list.append(new_button)
        self.button_group.add(new_button)

    def update(self) -> None:
        """
        Update all contents in this window

        :return: None
        """

        self.text_group.update()
        self.button_group.update()

        self.update_image()

    @abstractmethod
    def listen(self, group: pygame.sprite.Group) -> None:
        """
        Listen to a specific event and pops up at that event

        This method will be overrided by its child classes.

        :param group: Sprite group which this window belongs to
        :return: None
        """

        pass

    def popup(self, group: pygame.sprite.Group):
        """
        Pop up this window and add it to its sprite group

        :param group: Sprite group which this window belongs to
        :return: None
        """

        self.popped_up = True
        group.add(self)

    def popdown(self, group: pygame.sprite.Group):
        """
        Pop down this window and remove it from its sprite group

        :param group: Sprite group which this window belongs to
        :return: None
        """

        self.popped_up = False
        group.remove(self)

    def update_image(self):
        """
        Update appearance of this window and its contents

        :return: None
        """

        self.image.fill(background_color)
        pygame.draw.rect(self.image, main_color, [0, 0, self.size[0], self.size[1]], 3)

        self.text_group.draw(self.image)
        self.button_group.draw(self.image)
