import pygame
from pygame.locals import *

from constants.basic_settings import SCREEN_WIDTH, SCREEN_HEIGHT
from constants.colors import *
from controllers.mouse_controller import MouseEventListener

"""
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
"""

pygame.init()

# Set game title
pygame.display.set_caption("Count Forever")

# Create the screen
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)

# Frame control
fps_clock = pygame.time.Clock()
DELTA_TIME = 0

# Indicates whether continue game
running = True


# Theme colors
background_color = BLACK
main_color = WHITE1
