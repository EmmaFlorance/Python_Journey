import sys
import pygame
from settings import Settings
from ship import Ship
import game_play as pf

def start_game():
    pygame.init()
    aa_settings = Settings()
    screen = pygame.display.set_mode((aa_settings.srn_width, 
    aa_settings.srn_height))
    pygame.display.set_caption("Alien Attack!")

    ship = Ship(screen)

    while True:
        pf.scan_act(ship)
        pf.update_screen(aa_settings, screen, ship)

start_game()