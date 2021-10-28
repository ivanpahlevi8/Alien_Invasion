import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__() # its called construcotor for this class that inherit from main class called Sprite
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.image = pygame.image.load('ufo.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # memposisiikan alien di pojok kiri atas

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x