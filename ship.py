import pygame
from setting import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # ai_game merupakan instance dari class AlienInvasion, sehingga pada class sheep dapat mengakses tiap2 method dan
        # atribut yang ada pada class AlienInvasion seeprti screen dll
        self.screen = ai_game.screen
        # mengakses atribut screen pada class AlienInvasion
        # yang mana screen pada AlienInvasion merupakan lib pygame.display.set_mode, sehingga atribut screen pada class Ship
        # memiliki akses ke jendela windows utama pada class AlienInvasion
        self.screen_rect = ai_game.screen.get_rect()
        # menciptakan persegi dari jendela utama pada class AlienInvasion yang mana persegi tersebut seluas layar window
        # get_rect() merupakan atribut yang berfungsi mendapatkan sluruh area screen dalam bentuk persegi
        # dalam hal ini, screen_rect merupakan sluruh arean persegi dari window utama pada class InvasionAlien

        self.image = pygame.image.load('ship2.bmp')
        #mengimport gambar menggunakan library pygame
        self.rect = self.image.get_rect()
        # mendapatkan seluruh area gambar dalam bentuk persegi, dalam hal ini adalah gambar ship
        self.rect.midbottom = self.screen_rect.midbottom
        # atribut self.rect.midbottom posisinya diletakkan pada screen atau window utama dari class AlienInvasion
        # sehungga self.rect yang isinya merupakan pesawat ship dengan bentuk persegi diletakkan pada bagian midbottom
        # dari self.screen_rect yang self.screen_rect itu sendiri merupakan layar utama dari window pada class AlienInvasion
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.setting = Settings()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # menggambar slef.image pada laya dengan posisi sesuai dengan self.rect

    def update(self):
        if self.move_up and self.rect.y > 0:
            self.y -= self.setting.get_ship_speed()
        elif self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.get_ship_speed()
        elif self.move_left and self.rect.left > 0:
            self.x -= self.setting.get_ship_speed()
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.get_ship_speed()

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) #masalah pada ini
        # karena ketika pesawat collision dengan alien, pesawat dibuat berada di tengah, karena sebelumnya belum ada baris ini
        # maka ketika pesawat dibuat kembali di tengah, pesawat langsung mengalamin collision lagi dengan alien
        # sehingga ketika collision pertama terjadi, pesawat langsung freeze