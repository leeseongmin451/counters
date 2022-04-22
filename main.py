import init
from constants.basic_settings import FPS
from init import *
from player import Player

from scenes.scene import Scene
from scenes.gameplay_scene import GamePlayScene
from scenes.main_menu_scene import MainMenuScene


# All scenes
GamePlayScene()
MainMenuScene()


# Main game loop
while init.running:

    Player.get_inputs()                             # Get all inputs from player
    Scene.update_current()                          # Update currently displaying scene

    screen.fill(background_color)                   # Fill screen with background color
    Scene.draw_current(screen)                      # Draw currently displaying scene

    pygame.display.flip()                           # Update all display changes and show them
    init.DELTA_TIME = fps_clock.tick(FPS) / 1000    # Get time difference between present and previous game loop in seconds


pygame.quit()
exit()
