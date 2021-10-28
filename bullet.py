import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        # membuat peluru berbentuk persegi dengan width = self.setting.bullet_width - 0
        # dan height = self.setting.bullet_height - 0
        self.rect.midtop = ai_game.ship.rect.midtop
        # menempatkan peluru diatas tengah ship dalam bentuk persegi
        self.y = float(self.rect.y)
        # mengubah koordinat persegi dari peluru menjadi float

    def update(self):
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # pygame.draw.rect(layar target untuk digambar, warna, persegi yang akan digambar)
        # dalam hal ini layar target merupakan laayr utama dalam class AlienInvasion



