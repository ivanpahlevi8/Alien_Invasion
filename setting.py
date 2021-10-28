
class Settings:
    def __init__(self):
        self.display_width = 1200
        self.display_height = 800
        self.bg_color = (72, 61, 139)
        self.dict_color = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
        }

        self.ship_limit = 2


        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # alien setting
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.bullet_speed = 1
        self.ship_speed = 1.5
        self.alien_points = 50


    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.bullet_speed = 1
        self.ship_speed = 1.5

    def get_ship_speed(self):
        return self.ship_speed

    def increase_speed(self):
        self.ship_speed = int(self.ship_speed * self.speedup_scale)
        self.alien_speed = int(self.alien_speed * self.speedup_scale)
        self.bullet_speed = int(self.bullet_speed * self.speedup_scale)

        self.alien_points = int(self.alien_points * self.score_scale)

    def easy_mode(self):
        self.ship_speed = 1.0
        self.alien_speed = 1.0
        self.bullet_speed = 1.0

    def medium_mode(self):
        self.ship_speed = 3.0
        self.alien_speed = 3.0
        self.bullet_speed = 3.0

    def hard_mode(self):
        self.ship_speed = 5.0
        self.bullet_speed = 5.0
        self.alien_speed = 5.0



