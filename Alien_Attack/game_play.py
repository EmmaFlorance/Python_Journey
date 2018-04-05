import sys
import pygame
from pygame.locals import *


def scan_act(ship):
    for action in pygame.event.get():
        if action.type == QUIT:
            sys.exit()
            pygame.quit()

        elif action.type == KEYDOWN:
            if action.type == K_RIGHT:
                ship.rect.centerx += 100

def update_screen(aa_settings, screen, ship):
    screen.fill(aa_settings.bg_col)
    ship.appear()
    pygame.display.flip()