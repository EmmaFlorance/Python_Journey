import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        #Load the new ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Spawn each ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def appear(self):
        self.screen.blit(self.image, self.rect)