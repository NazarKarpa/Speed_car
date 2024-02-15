from pygame import *
from random import randint
import os

WIDTH, HEIGHT = 900,600

bg_image = image.load('background-1.png')

player_image1 = image.load('car-truck1.png')

enemy_image1 = image.load('car-truck2.png')
enemy_image2 = image.load('car-truck4.png')
enemy_image3 = image.load('car-truck5.png')

mixer.music.load('run car.mp3')
mixer.music.set_volume(0.4)


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, rect_x, rect_y, speed):
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
        self.mask = mask.from_surface(self.image)

    def draw(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()




window = display.set_mode((WIDTH, HEIGHT))



game = True
finish = False
clock = time.Clock()
while game:
    pass