import pygame.locals
from pygame import *
from random import randint, choice

import os
import sys



init()
font.init()
mixer.init()

WIDTH, HEIGHT = 900,600

bg_image = image.load('background-1.png')

player_image1 = image.load('car-truck1.png')

enemy_image1 = image.load('car-truck2.png')
enemy_image2 = image.load('car-truck4.png')
enemy_image3 = image.load('car-truck5.png')

menu_bg = image.load('background-1.png')

button_play = image.load('PlayButton.png')

enemy_images = [enemy_image1, enemy_image2, enemy_image3]

font_meny = font.SysFont('arial', 50)

mixer.music.load('run car.mp3')
mixer.music.set_volume(0.4)


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, rect_x, rect_y, speed):
        super().__init__()
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
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 150:
            self.rect.x -= self.speed
        if keys[K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
class Enemy(GameSprite):

    def update(self):

        if self.rect.y < HEIGHT:
            self.rect.y += self.speed


class Menu():
    pass









def random_car():


    rand_race = randint(1, 4)
    rand_y = randint(-200, -20)
    rand_speed = randint(10, 15)
    enemy_image = choice(enemy_images)
    if rand_race == 1:
        enemy = Enemy(enemy_image, 50, 100, 210, rand_y, rand_speed)
        enemys.add(enemy)
    if rand_race == 2:
        enemy = Enemy(enemy_image, 50, 100, 350, rand_y, rand_speed)
        enemys.add(enemy)
    if rand_race == 3:
        enemy = Enemy(enemy_image, 50, 100, 500, rand_y, rand_speed)
        enemys.add(enemy)
    if rand_race == 4:
        enemy = Enemy(enemy_image, 50, 100, 630, rand_y, rand_speed)
        enemys.add(enemy)








window = display.set_mode((WIDTH, HEIGHT))

bg = transform.scale(bg_image, (WIDTH, HEIGHT))



enemys = sprite.Group()

lost = 0



player = Player(player_image1, 50, 80, 200, HEIGHT - 150, 7)
FPS = 60
game = False
finish = False



clock = time.Clock()
random_car()

rand_interval = randint(1000, 3000)
font1 = font.SysFont("Aril", 35)

menu = True

while menu:
    for e in event.get():
        if e.type == QUIT:
            menu = False



    window.blit(bg, (0, 0))


    display.update()
    clock.tick(FPS)

start_time = time.get_ticks()
start_time1 = time.get_ticks()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        if time.get_ticks() - start_time > rand_interval:
            random_car()
            start_time = time.get_ticks()
            rand_interval = randint(1000, 3000)
        time_tick = (time.get_ticks() - start_time1) / 1000



        spritelist = sprite.spritecollide(player,enemys, False)
        for collide in spritelist:
            finish = True
        if time_tick > 10:
            finish = True

        window.blit(bg, (0, 0))

        txt_time = font1.render(f"Час: {time_tick}", True, (200, 200, 100))
        window.blit(txt_time, (30, 30))
        player.draw()
        enemys.draw(window)

        player.update()
        enemys.update()


    display.update()
    clock.tick(FPS)