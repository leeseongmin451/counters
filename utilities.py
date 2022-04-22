from typing import Tuple
from init import *
from sprites.camera import Camera


camera = Camera()
screen_offset_x = SCREEN_WIDTH // 2
screen_offset_y = SCREEN_HEIGHT // 2


def trans_screen_to_field(screen_pos: Tuple[int, int]) -> Tuple[int, int]:
    field_pos_x = screen_pos[0] + camera.center_x - screen_offset_x
    field_pos_y = screen_pos[1] + camera.center_y - screen_offset_y
    return field_pos_x, field_pos_y


def trans_field_to_screen(field_pos: Tuple[int, int]) -> Tuple[int, int]:
    screen_pos_x = field_pos[0] - camera.center_x + screen_offset_x
    screen_pos_y = field_pos[1] - camera.center_y + screen_offset_y
    return screen_pos_x, screen_pos_y


def get_difference(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Tuple[int, int]:
    diff_x = abs(pos1[0] - pos2[0])
    diff_y = abs(pos1[1] - pos2[1])
    return diff_x, diff_y


def get_midpoint(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Tuple[int, int]:
    midpoint_x = (pos1[0] + pos2[0]) // 2
    midpoint_y = (pos1[1] + pos2[1]) // 2
    return midpoint_x, midpoint_y


def get_pos_in_rect(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    offset_x = min(pos1[0], pos2[0])
    offset_y = min(pos1[1], pos2[1])
    relative_pos1 = (pos1[0] - offset_x, pos1[1] - offset_y)
    relative_pos2 = (pos2[0] - offset_x, pos2[1] - offset_y)
    return relative_pos1, relative_pos2
