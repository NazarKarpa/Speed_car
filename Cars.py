import time

import pygame.locals
from pygame import *
from random import randint, choice

import os
import sys

coin_record = 0

level = 1

init()
font.init()
mixer.init()

WIDTH, HEIGHT = 900,600

bg_image = image.load('background-1.png')

player_image1 = image.load('car-truck1.png')
player_image1 = transform.scale(player_image1, (50, 80))

spike_image = image.load('small_metal_spike.png')

coin_image = image.load('coin_01.png')

bost_image = image.load('boostmega-removebg-preview.png')

enemy_image1 = image.load('car-truck2.png')
enemy_image2 = image.load('car-truck4.png')
enemy_image3 = image.load('car-truck5.png')

menu_bg = image.load('background-1.png')

button_play_img = image.load('PlayButton.png')

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
            self.image = transform.rotate(player_image1, -10)

        elif keys[K_a] and self.rect.x > 150:
            self.rect.x -= self.speed
            self.image = transform.rotate(player_image1, 10)
        else:
            self.image = player_image1
        if keys[K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

class Enemy(GameSprite):

    def update(self):

        if self.rect.y < HEIGHT:
            self.rect.y += self.speed


class Menu(GameSprite):
    pass









def random_car():
    global rand_speed
    global level
    global rand_interval

    if level == 2:
        rand_speed = randint(10, 15)
        rand_interval = randint(1000, 2000)

    elif level == 1:
        rand_speed = randint(5, 10)
        rand_interval = randint(1000, 3000)
    if level == 3:
        rand_speed = randint(15, 20)
        rand_interval = randint(500, 2000)

    elif level == 4:
        rand_speed = randint(25, 30)
        rand_interval = randint(500, 1500)
    elif level == 5:
        rand_speed = randint(30, 35)
        rand_interval = randint(500, 1000)


    rand_race = randint(1, 4)
    rand_y = randint(-200, -20)

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



def random_booster():

    rand_speeded = randint(3, 5)
    rand_race = randint(1, 4)
    rand_y = randint(-200, -20)

    if rand_race == 1:
        boost = Enemy(bost_image, 50, 60, 210, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 2:
        boost = Enemy(bost_image, 50, 60, 350, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 3:
        boost = Enemy(bost_image, 50, 60, 500, rand_y, rand_speeded)
        bostery.add(boost)
    if rand_race == 4:
        boost = Enemy(bost_image, 50, 60, 630, rand_y, rand_speeded)
        bostery.add(bostery)

def random_coin():

    rand_speed_coin = randint(3, 5)
    rand_race = randint(1, 4)
    rand_y = randint(-200, -20)

    if rand_race == 1:
        coin = Enemy(coin_image, 40, 50, 210, rand_y, rand_speed_coin)
        coin_group.add(coin)
    if rand_race == 2:
        coin = Enemy(coin_image, 40, 50, 350, rand_y, rand_speed_coin)
        coin_group.add(coin)
    if rand_race == 3:
        coin = Enemy(coin_image, 40, 50, 500, rand_y, rand_speed_coin)
        coin_group.add(coin)
    if rand_race == 4:
        coin = Enemy(coin_image, 40, 50, 630, rand_y, rand_speed_coin)
        coin_group.add(coin)



def random_spike():
    global bg_speed
    rand_race = randint(1, 4)
    rand_y = randint(-200, -20)




    if rand_race == 1:
        spike = Enemy(spike_image, 30, 25, 200, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 230, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 260, rand_y, bg_speed)
        spike_group.add(spike)
    if rand_race == 2:

        spike = Enemy(spike_image, 30, 25, 330, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 360, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 390, rand_y, bg_speed)
        spike_group.add(spike)

    if rand_race == 3:
        spike = Enemy(spike_image, 30, 25, 470, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 500, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 530, rand_y, bg_speed)
        spike_group.add(spike)
    if rand_race == 4:
        spike = Enemy(spike_image, 30, 25, 610, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 640, rand_y, bg_speed)
        spike_group.add(spike)
        spike = Enemy(spike_image, 30, 25, 670, rand_y, bg_speed)
        spike_group.add(spike)

window = display.set_mode((WIDTH, HEIGHT))

bg = transform.scale(bg_image, (WIDTH, HEIGHT))

coin_group = sprite.Group()
bostery = sprite.Group()
spike_group = sprite.Group()
enemys = sprite.Group()

lost = 0


button_play = Menu(button_play_img, 100, 200, 200, 400, 1)

player = Player(player_image1, 50, 80, 200, HEIGHT - 150, 7)
FPS = 60

finish = False


clock = time.Clock()
random_car()
rand_intervaled = randint(500, 20000)
rand_interval = randint(1000, 3000)
rand_interval_spike = randint(1000, 10000)
rand_interval_coin = randint(1000, 5000)
font1 = font.SysFont("Aril", 35)
font2 = font.SysFont('Aril', 25)
font3 = font.SysFont('Aril', 104)
font4 = font.SysFont('Aril', 104)
txt_lose_game = font3.render("You lose", True, (255, 0, 0))
txt_win_game = font3.render('You win', True, (0, 255, 0))
level = int(1)
menu = True


start_time4 = time.get_ticks()
start_time3 = time.get_ticks()
start_time2 = time.get_ticks()
start_time = time.get_ticks()
start_time1 = time.get_ticks()
bg_y1 = 0
bg_y2 = -600
bg_speed = 3
while level < 7:





    if menu == True:
        window.blit(bg, (0, 0))
        for e in event.get():
            if e.type == QUIT:
                menu = False
        button_play.draw()
        button_play.update()
    else:
        for e in event.get():
            if e.type == QUIT:
                level = 8
        if not finish:
            if bg_y1 > 600:
                bg_y1 = -600

            if bg_y2 > 600:
                bg_y2 = -600
            window.blit(bg, (0, bg_y1))

            bg_y1 += bg_speed
            window.blit(bg, (0, bg_y2))
            bg_y2 += bg_speed



            if time.get_ticks() - start_time > rand_interval:
                random_car()
                start_time = time.get_ticks()


            if time.get_ticks() - start_time3 > rand_interval_spike:
                random_spike()
                start_time3 = time.get_ticks()

            if time.get_ticks() - start_time4 > rand_interval_coin:
                random_coin()
                start_time4 = time.get_ticks()

            time_tick = (time.get_ticks() - start_time1) / 1000

            if time.get_ticks() - start_time2 > rand_intervaled:
                random_booster()
                start_time2 = time.get_ticks()

            spritelist = sprite.spritecollide(player, enemys, False)
            spritelist_boost = sprite.spritecollide(player, bostery, False)
            sprite_list_spike = sprite.spritecollide(player, spike_group, False)
            spritelist_coin = sprite.spritecollide(player, coin_group, False)
            for collide in spritelist_coin:
                coin_group.empty()
                coin_record += 1

                print(coin_record)
            for collide in sprite_list_spike:
                window.blit(txt_lose_game, (280,260))
                finish = True
            for collide in spritelist:
                window.blit(txt_lose_game, (280,260))
                finish = True
            for collide in spritelist_boost:
                player.speed += 0.1
            if time_tick > 10 and level == 1:


                bg_speed += 2
                level += 1

                print(level)
            if time_tick > 20 and level == 2:
                bg_speed += 2
                level += 1
                print(level)

            if time_tick > 30 and level == 3:
                bg_speed += 2
                level += 1
                print(level)
            if time_tick > 40 and level == 4:
                bg_speed += 2
                level += 1
                print(level)
            if time_tick > 45 and level == 5:
                bg_speed = 9
                level += 1
            if level == 6:
                window.blit(txt_win_game, (280,260))
                finish = True

            txt_coin = font2.render(f"Очки: {coin_record}", True, (201, 200, 100))
            window.blit(txt_coin, (30, 90))


            txt_level = font2.render(f"Рівень: {level}", True, (201, 200, 100))
            window.blit(txt_level, (40, 60))

            txt_time = font1.render(f"Час: {time_tick}", True, (200, 200, 100))
            window.blit(txt_time, (30, 30))

            player.draw()
            enemys.draw(window)
            bostery.draw(window)
            spike_group.draw(window)
            coin_group.draw(window)

            player.update()
            enemys.update()
            bostery.update()
            spike_group.update()
            coin_group.update()

    display.update()
    clock.tick(FPS)





