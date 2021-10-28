import pygame.font
from pygame.sprite import Sprite
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.text_color = (252, 165, 3)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)

        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = 100
        self.score_image_rect.top = 20

    def prep_high_score(self):
        high_score_round = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score_round)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.setting.bg_color)

        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = 20

    def prep_level(self):
        level_str = f"Lv : {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.screen_rect.right - 5
        self.level_image_rect.top = self.screen_rect.top + 20

    def prep_ship(self):
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game) #membuat objek ship dari class Ship
            ship.rect.x = 110 + ship_number * ship.rect.width #memposisikan korrdinat x dari rect berada pada 110 ditambah ship * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)

    def show_score(self):
         self.screen.blit(self.score_image, self.score_image_rect)
         self.screen.blit(self.high_score_image, self.high_score_image_rect)
         self.screen.blit(self.level_image, self.level_image_rect)
         self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()