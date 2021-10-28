import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (72, 61, 139)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 - 3 * self.height) #memposisikan frame dari tulisan ditengah dari layar utama

        self._prep_msg(msg) # fungsi ini dipaggil pertama kali ketika memanggil kelas Button pada alien_invasion :)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True , self.text_color, self.button_color) #membuat tulisan
        self.msg_image_rect = self.msg_image.get_rect() #memwrap tulisan dengan persegi
        self.msg_image_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 - 3 * self.height) #memposiiskan tulisan di tengah layar

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class LevelButton():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 50
        self.width_button_wrapper = 200
        self.height_button_wrapper = 200
        self.easy_button_color = (0, 200, 0)
        self.medium_button_color = (251, 140, 1)
        self.hard_button_color = (255, 0, 0)
        self.wrapper_button_color = (245, 255, 250)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.easy_rect = pygame.Rect(0, 0, self.width, self.height)
        self.medium_rect = pygame.Rect(0, 0, self.width, self.height)
        self.hard_rect = pygame.Rect(0, 0, self.width, self.height)
        self.wrapper_rect = pygame.Rect(0, 0, self.width_button_wrapper, self.height_button_wrapper)

        self.easy_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 - self.height - 10)
        self.medium_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2)
        self.hard_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 + self.height + 10)
        self.wrapper_rect.center = self.screen_rect.center

        self._prep_msg()

    def _prep_msg(self):
        self.easy_msg_image = self.font.render("Easy", True, self.text_color, self.easy_button_color)
        self.medium_msg_image = self.font.render("Medium", True, self.text_color, self.medium_button_color)
        self.hard_msg_image = self.font.render("Hard", True, self.text_color, self.hard_button_color)

        self.easy_msg_image_rect = self.easy_msg_image.get_rect()
        self.medium_msg_image_rect = self.medium_msg_image.get_rect()
        self.hard_msg_image_rect = self.hard_msg_image.get_rect()

        self.easy_msg_image_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 - self.height - 10)
        self.medium_msg_image_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2)
        self.hard_msg_image_rect.center = (self.setting.display_width / 2, self.setting.display_height / 2 + self.height + 10)

    def draw_button(self):
        self.screen.fill(self.wrapper_button_color, self.wrapper_rect)
        self.screen.fill(self.easy_button_color, self.easy_rect)
        self.screen.fill(self.medium_button_color, self.medium_rect)
        self.screen.fill(self.hard_button_color, self.hard_rect)
        self.screen.blit(self.easy_msg_image, self.easy_msg_image_rect)
        self.screen.blit(self.medium_msg_image, self.medium_msg_image_rect)
        self.screen.blit(self.hard_msg_image, self.hard_msg_image_rect)


class InfoLevel():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = self.screen.get_rect()

        self.width = 380
        self.height = 50
        self.speed_info_width = 100
        self.speed_info_height = 25
        self.easy_info_color = (0, 200, 0)
        self.medium_info_color = (251, 140, 1)
        self.hard_info_color = (255, 0, 0)
        self.speed_ship_info_color = (152, 251, 153)
        self.text_color = (255, 255, 255)
        self.text_speed_color = (254, 228, 225)
        self.font = pygame.font.SysFont(None, 48)
        self.font_speed_info = pygame.font.SysFont(None, 40)

        self.easy_info_rect = pygame.Rect(0, 0, self.width, self.height)
        self.medium_info_rect = pygame.Rect(0, 0, self.width, self.height)
        self.hard_info_rect = pygame.Rect(0, 0, self.width, self.height)

        self.easy_info_rect.center = (self.setting.display_width / 2, 120)
        self.medium_info_rect.center = (self.setting.display_width / 2, 120)
        self.hard_info_rect.center = (self.setting.display_width / 2, 120)

        self.kondisi_easy = False
        self.kondisi_medium = False
        self.kondisi_hard = False
        self.speed = self.setting.ship_speed
        self._prep_msg()

    def _prep_msg(self):
        self.easy_msg_image = self.font.render("Easy Level Choosen", True, self.text_color, self.easy_info_color)
        self.medium_msg_image = self.font.render("Medium Level Choosen", True, self.text_color, self.medium_info_color)
        self.hard_msg_image = self.font.render("Hard Level Choosen", True, self.text_color, self.hard_info_color)
        self.speed_msg_image = self.font_speed_info.render(f"Ship Speed : {self.speed}", True, self.text_speed_color, self.setting.bg_color)

        self.easy_msg_image_rect = self.easy_msg_image.get_rect()
        self.medium_msg_image_rect = self.medium_msg_image.get_rect()
        self.hard_msg_image_rect = self.hard_msg_image.get_rect()
        self.speed_msg_image_rect = self.speed_msg_image.get_rect()

        self.easy_msg_image_rect.center = (self.setting.display_width / 2, 120)
        self.medium_msg_image_rect.center = (self.setting.display_width / 2, 120)
        self.hard_msg_image_rect.center = (self.setting.display_width / 2, 120)
        self.speed_msg_image_rect.top = self.screen_rect.top + 23
        self.speed_msg_image_rect.right = (self.screen_rect.right - 170) - self.screen_rect.top

    def draw_easy_msg(self):
        if (self.kondisi_easy):
            self.screen.fill(self.easy_info_color, self.easy_info_rect)
            self.screen.blit(self.easy_msg_image, self.easy_msg_image_rect)
            self.text_speed_color = (63, 255, 0)
            self._prep_msg() #untuk memperbarui nilai kecepatan oada pesawat yang akan ditampilkan pada layar

    def draw_medium_msg(self):
        if (self.kondisi_medium):
            self.screen.fill(self.medium_info_color, self.medium_info_rect)
            self.screen.blit(self.medium_msg_image, self.medium_msg_image_rect)
            self.text_speed_color = (244, 164, 95)
            self._prep_msg()

    def draw_hard_msg(self):
        if (self.kondisi_hard):
            self.screen.fill(self.hard_info_color, self.hard_info_rect)
            self.screen.blit(self.hard_msg_image, self.hard_msg_image_rect)
            self.text_speed_color = (250, 69, 1)
            self._prep_msg()

    def draw_speed_msg(self):
        self.screen.blit(self.speed_msg_image, self.speed_msg_image_rect)
























