import pygame
import numpy
import time
import pygame.draw as draw
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

# цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
BROWN = (75, 39, 13)
GREY_BLOW = (119, 164, 197)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BROWN]


def new_ball():

    """
    создадим новый мяч на экране
    :return: заготовка под движущийся на экране мяч
    """
    x = randint(100, 1200)
    y = randint(100, 800)
    r = randint(30, 50)
    speed_x = randint(-20, 20)
    speed_y = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    return [x, y, r, color, False, speed_x, speed_y]


def catch_ball_checker(event, ball_information):
    """
    проверим, куда вы попали и попали ли вообще
    :param event: событие, на котором основана проверка
    :param ball_information: информация о мяче
    :return: 1 попали по мячу 0 не попали
    """
    for item_of_ball_coordinates in ball_information:
        x, y, r = item_of_ball_coordinates[0], item_of_ball_coordinates[1], item_of_ball_coordinates[2]
        ball_is_touched = item_of_ball_coordinates[4]
        distance_to_the_ball_center_squared = (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2
        if distance_to_the_ball_center_squared <= r ** 2 and not ball_is_touched:
            item_of_ball_coordinates[4] = True
            return True
    return False


def strike_wall(current_ball):
    """
    изменим скорость мяча, если он ударяется о стену
    :param current_ball: мяч который находится в моменте удара
    :return: мяч который поменял свою скорость после взаимодействмя со стеной
    """

    if current_ball[0] < 0 or current_ball[0] > 1200:
        current_ball[5] *= -1
    if current_ball[1] < 0 or current_ball[1] > 900:
        current_ball[6] *= -1


def new_bolt():
    """
    сделаем новый болт
    :return: заготовка под болт, движущийся по экрану
    """
    x = randint(100, 1200)
    y = randint(100, 800)
    size = randint(20, 40)
    speed_x = randint(-20, 20)
    speed_y = randint(-25, 25)
    color = GREY_BLOW
    return [x, y, size, color, False, speed_x, speed_y]


def catch_bolt_checker(event, bolt_information):
    """
    function
    :param event: рассматриваемое событие
    :param bolt_information: информация о болтике
    :return: 1 - попали по болту, 1 - не попали
    """
    for bolt in bolt_information:
        x, y, r = bolt[0], bolt[1], bolt[2]
        is_touched = bolt[4]
        if (x - event.pos[0]) ** 2 <= r ** 2 and 4 * (y - event.pos[1]) ** 2 <= r ** 2 and not is_touched:
            bolt[4] = True
            bolt[3] = BROWN
            return True
    return False


def draw_bolt(surf, bolt):
    """
   рисуем болт и ставим его на экран
    :param surf: экран, где рисуем болт
    :param bolt: болт, кладущийся на экарн
    :return: болт на экране
    """

    x, y, r, speed_x, speed_y = bolt[0], bolt[1], bolt[2], bolt[5], bolt[6]
    surface = pygame.Surface((r, r))
    surface.fill((0, 0, 0))

    # рисуем болт
    draw.polygon(surface, bolt[3], ((0, 0), (r // 4, 0), (r // 4, r // 8), (r // 4 + r, r // 8), (r // 4 + r, r // 4),
                                    (r // 4, r // 4), (r // 4, r // 4 + r // 8), (0, r // 4 + r // 8), (0, 0)), 2)
    slot = 20
    while slot > 0:
        draw.line(surface, bolt[3], (r // 4 + slot * r // 10, r // 8), (r // 4 + slot * r // 10, r // 4), 2)
        slot -= 1

    hat = 100
    while hat > 0:
        draw.line(surface, bolt[3], (r // 4 - hat * r // 100, 0), (r // 4 - hat * r // 100, r // 4 + r // 8), 3)
        hat -= 1
    surface.set_colorkey(BLACK)

    # запускаем наш болт
    angle = 57 * numpy.arctan(speed_y / (speed_x + 0.01))
    if speed_x * speed_y > 0:
        angle += 90
    surface2 = pygame.transform.rotate(surface, angle)
    surf.blit(surface2, (x, y))


# начальная информация о шарах и болтах
balls = [new_ball()]
bolts = [new_bolt()]

# введем количество игроков
print("Write number of players")
number_players = int(input())
number_items_in_dict = number_players
list_of_players = dict()

while number_players > 0:

    # введем имя игрока
    print("Write name of player")
    name_player = str(input())

    # информация об игре
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    score = 0
    phase = 0
    time.sleep(1)

    # обработка событий
    while not finished:

        clock.tick(FPS)

        # заполняем экран мишенями
        for bolt in bolts:
            if bolt[4]:
                draw.circle(screen, bolt[3], (bolt[0], bolt[1]), bolt[2] // 2)
        for ball in balls:
            if ball[2] == 0:
                ball[4] = True
            if not ball[4]:
                ball[0] += ball[5]
                ball[1] += ball[6]
                strike_wall(ball)
                draw.circle(screen, ball[3], (ball[0], ball[1]), ball[2])
        for bolt in bolts:
            if not bolt[4]:
                bolt[0] += bolt[5]
                bolt[1] += bolt[6]
                bolt[5] += randint(-2, 2)
                bolt[6] += randint(-2, 2)
                strike_wall(bolt)
                draw_bolt(screen, bolt)

        # контроль событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if catch_ball_checker(event, balls):
                    score += 1
                if catch_bolt_checker(event, bolts):
                    score += 2

        # создание новых предметов
        phase += 1
        if phase % 10 == 0:
            balls.append(new_ball())
        if phase % 100 == 0:
            bolts.append(new_bolt())
        # обновляем экран
        pygame.display.update()
        screen.fill(BLACK)

    # конец игры
    balls.clear()
    bolts.clear()

    list_of_players[name_player] = score
    number_players -= 1

# запишим в файл данные о игроках
file = open('results.txt', 'w')

for key, value in list_of_players.items():
    file.write(f'{key}: {value}\n')

file.close()

print("Game is over, check file")

pygame.quit()