from typing import *

import pygame


class TextSurface(pygame.sprite.Sprite):
    """
    Text class as a sprite object
    """

    group = pygame.sprite.Group()

    def __init__(self, text: str, text_args: Tuple, font: str, font_size: int, color: Tuple[int, int, int], pivot: str, position: Tuple[int, int]):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self)

        self.text = text
        self.text_args = text_args
        self.font = pygame.font.Font(font, font_size)
        self.color = color
        self.pivot = pivot
        self.position = position

        self.image = self.font.render(self.text.format(*self.text_args), True, self.color)
        self.rect = self.set_position(self.pivot, self.position)

    def set_position(self, pivot: str, position: Tuple[int, int]) -> pygame.Rect:
        """
        Set position of this text

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

    def update_text(self, new_text: str, new_text_args: Tuple) -> None:
        """
        Update to new text surface

        :return: None
        """

        self.text = new_text
        self.text_args = new_text_args

    def update_args(self, new_text_args: Tuple) -> None:
        """
        Update arguments of text

        :return: None
        """

        self.text_args = new_text_args

    def update_color(self, new_color: Tuple[int, int, int]) -> None:
        """
        Update color of text

        :return: None
        """

        self.color = new_color

    def update(self, mouse_state=None, key_state=None) -> None:
        """
        Update this text

        :param mouse_state: Mouse inputs
        :param key_state: Keyboard inputs
        :return: None
        """

        self.image = self.font.render(self.text.format(*self.text_args), True, self.color)
        self.rect = self.set_position(self.pivot, self.position)
