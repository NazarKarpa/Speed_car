import time

import pygame.locals
from pygame import *
from random import randint, choice


import os
import sys


coin_record = 0

price_car1 = 0
price_car2 = 15

level = 1

init()
font.init()
mixer.init()

WIDTH, HEIGHT = 900,600

bg_image = image.load('background-1.png')

image_shop = image.load('test_128x128_7.png')

buy_png = image.load('pngtree-buy-now-png-image_3165728-removebg-preview.png')
sold_png = image.load('sales-stock-photography-rubber-stamp-postage-stamps-sold-out-removebg-preview.png')

player_image2= image.load('car-truck2 — копия.png.')
player_image2 = transform.scale(player_image2, (50, 80))
player_image1 = image.load('car-truck1.png')
player_image1 = transform.scale(player_image1, (50, 80))

spike_image = image.load('small_metal_spike.png')

shop = image.load('2D shop.png')

coin_image = image.load('coin_01.png')

bost_image = image.load('boostmega-removebg-preview.png')

enemy_image1 = image.load('car-truck2.png')
enemy_image2 = image.load('car-truck4.png')
enemy_image3 = image.load('car-truck5.png')

menu_bg = image.load('background-1.png')

button_play_img = image.load('PlayButton.png')

button_exit_img = image.load('Quit_button-removebg-preview.png')

enemy_images = [enemy_image1, enemy_image2, enemy_image3]

font_meny = font.SysFont('arial', 50)

crash_sound = mixer.Sound('ar crashed.mp3')



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


def coins():
    global coin_record
    with open('Record.txt', 'r') as f:
        coin_record = int(f.readline())

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


bg_shop = transform.scale(image_shop, (WIDTH, HEIGHT))
bg = transform.scale(bg_image, (WIDTH, HEIGHT))

coin_group = sprite.Group()
bostery = sprite.Group()
spike_group = sprite.Group()
enemys = sprite.Group()

lost = 0


button_play = Menu(button_play_img, 300, 200, 300, 50, 1)



button_buy = Menu(buy_png, 120, 120, 20, 350, 1)

button_buy2 = Menu(buy_png, 120, 120, 185, 350, 1)

sould_button1 = Menu(sold_png, 200, 200, 0, 150, 1)
sould_button2 = Menu(sold_png, 200, 200, 160, 150, 1)

button_shop = Menu(shop, 210, 180, 350, 220, 1)

button_QUIT = Menu(button_exit_img, 250, 150, 330, 450, 1)

player_image_shop2 = Menu(player_image2, 90, 120, 200, 200, 1)
player_image_shop1 = Menu(player_image1, 90, 120, 40, 200, 1)

player = Player(player_image1, 50, 80, 200, HEIGHT - 150, 7)
FPS = 60

finish = False


clock = time.Clock()

rand_intervaled = randint(500, 30000)
rand_interval = randint(1000, 3000)
rand_interval_spike = randint(1000, 10000)
rand_interval_coin = randint(1000, 9000)
font1 = font.SysFont("Aril", 35)
font2 = font.SysFont('Aril', 25)
font3 = font.SysFont('Aril', 104)
font4 = font.SysFont('Aril', 104)
txt_lose_game = font3.render("You lose", True, (255, 0, 0))
txt_win_game = font3.render('You win', True, (0, 255, 0))
level = int(1)
menu = True

frames = 0
timer = 0


start_time4 = time.get_ticks()
start_time3 = time.get_ticks()
start_time2 = time.get_ticks()
start_time = time.get_ticks()
start_time1 = time.get_ticks()

b = 0
if_buy1 = False
if_buy2 = False

bg_y1 = 0
bg_y2 = -600
bg_speed = 3
while level < 7:





    if menu == True:
        window.blit(bg, (0, 0))

        if b == 1:

            window.blit(bg_shop, (0, 0))


            coins()


            for e in event.get():
                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        b = 0


                elif e.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(mouse_y, '-y', mouse_x, '-x')

                    if mouse_x <= 300 and mouse_y < 428 and mouse_x > 180 and mouse_y > 390:
                        '2 knopka'
                        if coin_record > 15:
                            if if_buy2 == False:
                                with open('Record.txt', 'w') as f:
                                    coin_record -= 15
                                    f.write(str(coin_record))
                                    player_image1 = image.load('car-truck2 — копия.png')
                                    player_image1 = transform.scale(player_image1, (50, 80))

                                    if_buy2 = True
                            elif if_buy2 == True:
                                player_image1 = image.load('car-truck2 — копия.png')
                                player_image1 = transform.scale(player_image1, (50, 80))




                    if mouse_x <= 140 and mouse_y < 428 and mouse_x > 20 and mouse_y > 390:
                        'Провірка покупка прошла ли'

                        player_image1 = image.load('car-truck1.png')
                        player_image1 = transform.scale(player_image1, (50, 80))


                        if_buy1 = True

                        print('popad')


            txt_coin = font2.render(f"Ціна: {price_car1}", True, (201, 200, 100))
            window.blit(txt_coin, (50, 350))

            txt_coin = font2.render(f"Ціна: {price_car2}", True, (201, 200, 100))
            window.blit(txt_coin, (210, 350))

            txt_coin = font4.render(f"Очки: {coin_record}", True, (201, 200, 100))
            window.blit(txt_coin, (50, 10))

            player_image_shop2.draw()
            player_image_shop1.draw()

            button_buy2.draw()
            button_buy.draw()

            button_buy.update()
            button_buy2.update()

            player_image_shop2.update()
            player_image_shop1.update()


            sould_button1.draw()
            sould_button1.update()

        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x <= 553 and mouse_y <= 182 and mouse_x > 358 and mouse_y > 50:
                    'старт'
                    menu = False
                    finish = False

                elif mouse_x <= 557 and mouse_y <= 339 and mouse_x > 351 and mouse_y > 222:
                    'Кнопка магазу'
                    b +=1
                    print('button')




                elif mouse_x <= 559 and mouse_y <= 581 and mouse_x > 353 and mouse_y > 464:
                    'Кнопка виходу'
                    menu = False
                    level = 8

            if e.type == QUIT:
                menu = False
                level = 8

        if b < 1:
            window.blit(bg, (0, 0))
            button_QUIT.draw()
            button_shop.draw()
            button_play.draw()
            button_QUIT.update()
            button_shop.update()
            button_play.update()


        if if_buy2 == True and b == 1:
            sould_button2.draw()
            sould_button2.update()




    else:
        for e in event.get():
            if e.type == QUIT:
                level = 8
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE and level <= 6:

                    menu = True
                    finish = True

        if not finish:
            coins()
            frames += 1
            if frames >=60:
                timer+=1
                frames=0

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
                coin_record += 1
                with open('Record.txt', 'w') as f:
                        f.write(str(coin_record))

                coin_group.empty()


                print(coin_record)
            for collide in sprite_list_spike:
                window.blit(txt_lose_game, (280,260))
                finish = True
            for collide in spritelist:
                crash_sound.play()
                window.blit(txt_lose_game, (280,260))
                finish = True
            for collide in spritelist_boost:

                player.speed += 0.1
                bostery.empty()
            if timer > 10 and level == 1:


                bg_speed += 2
                level += 1

                print(level)
            if timer > 20 and level == 2:
                bg_speed += 2
                level += 1
                print(level)

            if timer > 30 and level == 3:
                bg_speed += 2
                level += 1
                print(level)
            if timer > 40 and level == 4:
                bg_speed += 2
                level += 1
                print(level)
            if timer > 45 and level == 5:
                bg_speed = 9
                level += 1
            if level == 6:
                window.blit(txt_win_game, (280,260))
                finish = True
            coins()
            txt_coin = font2.render(f"Очки: {coin_record}", True, (201, 200, 100))
            window.blit(txt_coin, (30, 90))


            txt_level = font2.render(f"Рівень: {level}", True, (201, 200, 100))
            window.blit(txt_level, (40, 60))

            txt_time = font1.render(f"Час: {timer}", True, (200, 200, 100))
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





