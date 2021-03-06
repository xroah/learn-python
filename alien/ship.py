import pygame
from settings import Settings
import os
from screen import screen


class Ship:
    def __init__(self):
        image_dir = os.path.dirname(__file__)

        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load(os.path.join(image_dir, "./images/ship.bmp"))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += Settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= Settings.ship_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= Settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += Settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
