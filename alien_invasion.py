import sys
import pygame
from setting import Settings
from ship import Ship
from pygame.locals import *
from bullet import Bullets
from ufo import Alien
from random import randint
from game_stats import GameStats
import time
from button import Button
from button import LevelButton
from button import InfoLevel
from scoreboard import Scoreboard
# PR mengatur jumlah alien di layar (belum tuntas)
# PR mengatur tampilan kecepatan pada layar saat game berlangsung. Note: Nilai pada layar tidak bisa dirubah
# bukan hanya nilai, kecepatan pesawat memang tidak berubah
# http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw (penjelasan mengenai library pygame.sprites)

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.display_width = self.screen.get_rect().width
        self.setting.display_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # membuat grup bullets yang berisi seluruh instance dari class Bullets
        self.aliens = pygame.sprite.Group()
        # membuat gruo aliens yang isinya seluruh instance dari class Aliens yang kemudian akan digambar pada layar
        # pygame.sprite.Group() merupakan sebuah  kontainer yang menyimpan seluruh objek dari sluru sprites
        self.stats = GameStats(self)

        self._create_fleet()

        self.play_button = Button(self, "P to Start")

        self.level_button = LevelButton(self)

        self.info_level = InfoLevel(self)

        self.sb = Scoreboard(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_level_button(mouse_pos)

    def _check_level_button(self, mouse_pos):
        easy_button = self.level_button.easy_rect.collidepoint(mouse_pos)
        medium_button = self.level_button.medium_rect.collidepoint(mouse_pos)
        hard_button = self.level_button.hard_rect.collidepoint(mouse_pos)

        if easy_button and not self.stats.game_active:
            self.setting.easy_mode()
            print("easy")
            self.info_level.speed = self.setting.ship_speed
            self.info_level.kondisi_easy = True
            self.info_level.kondisi_hard = False
            self.info_level.kondisi_medium = False
            self.info_level.draw_speed_msg()
        elif medium_button and not self.stats.game_active:
            self.setting.medium_mode()
            self.info_level.speed = self.setting.ship_speed
            self.info_level.kondisi_medium = True
            self.info_level.kondisi_easy = False
            self.info_level.kondisi_hard = False
            self.info_level.draw_speed_msg()
        elif hard_button and not self.stats.game_active:
            self.setting.hard_mode()
            self.info_level.speed = self.setting.ship_speed
            self.info_level.kondisi_hard = True
            self.info_level.kondisi_easy = False
            self.info_level.kondisi_medium = False
            self.info_level.draw_speed_msg()

    def _check_play_button(self, mouse_pos):
        button = self.play_button.rect.collidepoint(mouse_pos)
        if button and not self.stats.game_active: #jika mouse mengkilik pada bagian rect dari tombol dan game_active bernilai False
            self.stats.game_active = True # Ketika gam_active menjadi True, maka tulisan button play pada layar akan hilang
            self.stats.reset_stats()
            self.setting.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_ship()

            for alien in self.aliens.sprites():
                self.aliens.remove(alien)
            for bullet in self.bullets.sprites():
                self.bullets.remove(bullet)

            self._create_fleet()
            self.ship.center_ship()
            
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_r:
            self.setting.bg_color = self.setting.dict_color['red']
        elif event.key == pygame.K_g:
            self.setting.bg_color = self.setting.dict_color['green']
        elif event.key == pygame.K_w:
            self.setting.ship_speed += 1
            self.info_level.speed = self.setting.ship_speed
            self.info_level.draw_speed_msg()
        elif event.key == pygame.K_s:
            self.setting.ship_speed -= 1
            self.info_level.speed = self.setting.ship_speed
            self.info_level.draw_speed_msg()
        elif event.key == pygame.K_s:
            self.setting.ship_speed -= 1
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.game_active = True
            self.stats.reset_stats()

            for alien in self.aliens.sprites():
                self.aliens.remove(alien)
            for bullet in self.bullets.sprites():
                self.bullets.remove(bullet)

            self._create_fleet()
            self.ship.center_ship()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False
    
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            # self.bullets.sprites() merupakan list dari objek sprites di dalam class container sprites yang sebelumnya telah didefinisikan pada init
            # objek tersebut merupakan class Bullets
            bullet.draw_bullet()
            # menggambar peluru yang terdapat di grup yang di simpan dengan fungsi bullets.sprite
            # menggambar peluru oada bagian ini menggunakan method dari class Bullets

        self.aliens.draw(self.screen)
        # menggambar seluruh objek yang ada pada grouo alien
        # objek tersebut ditambahkan pada fungsi _create_fleet
        if not self.stats.game_active:
            self.play_button.draw_button() # button hanya digambar pada layar jika game belum aktiv
            self.level_button.draw_button()
            self.info_level.draw_easy_msg()
            self.info_level.draw_medium_msg()
            self.info_level.draw_hard_msg()

        self.sb.show_score()

        if self.stats.game_active:
            self.info_level._prep_msg()
            self.info_level.draw_speed_msg()


        pygame.display.flip()

    def _check_bullets(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        #collision merupakan dictionary yang menyimpan alien yang mengalami collision dengan peluru
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens: # jika alien habis pada layar
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()
            self.info_level.speed = self.setting.ship_speed
            self.info_level._prep_msg()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets()



    def _fire_bullet(self):
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)
        # menambahkan bullets ke kontainer class sprites yang telah dideklarasikan pada init

    def _create_alien(self, alien_number_x, alien_number_y):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number_x
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_number_y + self.ship.rect.height
        self.aliens.add(alien)

    def _update_alien(self):
        self._check_fleet_edges()
        for alien in self.aliens.sprites():
            alien.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens): #jika kapal collide dengan salah satu dari alien
            self._ship_hit()

        self._check_alien_bottom()

    def _ship_hit(self):

        for alien in self.aliens.sprites():
            self.aliens.remove(alien)
        for bullet in self.bullets.sprites():
            self.bullets.remove(bullet)

        self.ship.center_ship()
        time.sleep(0.1)
        self._create_fleet()

        if self.stats.ships_left > 0:
            self.stats.ships_left = self.stats.ships_left - 1
            self.sb.prep_ship()

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.stats.reset_stats()
            self.sb.prep_score()
            self.info_level.kondisi_hard = False
            self.info_level.kondisi_easy = False
            self.info_level.kondisi_medium = False

        print(f"Jumlah kapal tersisa : {self.stats.ships_left}")

    def _check_fleet_edges(self):
        uji = False
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        for  alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _create_fleet(self): # alien pertama kali dibuat ketika metod init dijalankan, dan smuanya di gambarkan pada layar dengan ,method draw pada update screen
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height

        available_space_x = self.setting.display_width - (2 * alien_width)
        numb_alien_x = available_space_x // (2 * alien_width)

        avaliable_space_y = (self.setting.display_height - (3 * alien_height) - (3 * ship_height))
        numb_alien_y = avaliable_space_y // (2 * alien_height)

        # membuat alien

        for y in range (numb_alien_y):
            for x in range(numb_alien_x):
                self._create_alien(x, y)



    def run_game(self):
        running = True
        while running:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()

            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()