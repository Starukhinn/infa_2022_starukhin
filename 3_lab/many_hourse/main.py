import pygame
from pygame.draw import *

# построение прямоугольника
def rectangle(n1, n2, n3, n4, size):
    return (int(n1*size), int(n2*size), int(n3*size), int(n4*size))

# рисуем эллипсы для хвоста
def outranging_number_of_ellipses(x0, y0, size):
    color_1_pink = (233, 175, 175)
    color_2_pink = (233, 198, 175)
    color_1_yellow = (255, 238, 170)
    color_1_green = (229, 255, 128)
    color_1_blue = (175, 233, 231)
    color_1_lilac = (221, 175, 233)
    ellipse(screen, color_1_pink, rectangle(x0 - 80, y0 - 200, 50, 20, size))
    ellipse(screen, color_2_pink, rectangle(x0 - 85, y0 - 190, 40, 35, size))
    ellipse(screen, color_1_yellow, rectangle(x0 - 65, y0 - 185, 40, 25, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 62, y0 - 170, 50, 20, size))
    ellipse(screen, color_2_pink, rectangle(x0 - 90, y0 - 167, 40, 15, size))
    ellipse(screen, color_1_lilac, rectangle(x0 - 80, y0 - 155, 50, 20, size))
    ellipse(screen, color_1_green, rectangle(x0 - 90, y0 - 160, 40, 25, size))
    ellipse(screen, color_2_pink, rectangle(x0 - 55, y0 - 158, 50, 30, size))
    ellipse(screen, color_1_yellow, rectangle(x0 - 80, y0 - 150, 50, 30, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 95, y0 - 147, 50, 35, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 60, y0 - 140, 40, 20, size))
    ellipse(screen, color_1_blue, rectangle(x0 - 80, y0 - 130, 60, 30, size))
    ellipse(screen, color_1_blue, rectangle(x0 - 50, y0 - 125, 70, 35, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 95, y0 - 120, 75, 25, size))
    ellipse(screen, color_1_lilac, rectangle(x0 - 80, y0 - 115, 70, 30, size))
    ellipse(screen, color_1_blue, rectangle(x0 - 90, y0 - 110, 70, 25, size))
    ellipse(screen, color_1_blue, rectangle(x0 - 70, y0 - 100, 80, 40, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 80, y0 - 95, 80, 40, size))
    ellipse(screen, color_1_lilac, rectangle(x0 - 100, y0 - 90, 75, 30, size))
    ellipse(screen, color_1_yellow, rectangle(x0 - 70, y0 - 87, 90, 35, size))
    ellipse(screen, color_2_pink, rectangle(x0 - 95, y0 - 82, 95, 25, size))

def outranging_number_of_ellipses_reflected(x0, y0, size):

    color_1_pink = (233, 175, 175)
    color_2_pink = (233, 198, 175)
    color_1_yellow = (255, 238, 170)
    color_1_green = (229, 255, 128)
    color_1_blue = (175, 233, 231)
    color_1_lilac = (221, 175, 233)
    ellipse(screen, color_1_pink, rectangle(x0 + 80, y0 - 200, 50, 20, size))
    ellipse(screen, color_2_pink, rectangle(x0 + 85, y0 - 190, 40, 35, size))
    ellipse(screen, color_1_yellow, rectangle(x0 + 65, y0 - 185, 40, 25, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 62, y0 - 170, 50, 20, size))
    ellipse(screen, color_2_pink, rectangle(x0 + 90, y0 - 167, 40, 15, size))
    ellipse(screen, color_1_lilac, rectangle(x0 + 80, y0 - 155, 50, 20, size))
    ellipse(screen, color_1_green, rectangle(x0 + 90, y0 - 160, 40, 25, size))
    ellipse(screen, color_2_pink, rectangle(x0 + 55, y0 - 158, 50, 30, size))
    ellipse(screen, color_1_yellow, rectangle(x0 + 80, y0 - 150, 50, 30, size))
    ellipse(screen, color_1_pink, rectangle(-x0 + 95, y0 - 147, 50, 35, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 60, y0 - 140, 40, 20, size))
    ellipse(screen, color_1_blue, rectangle(x0 + 80, y0 - 130, 60, 30, size))
    ellipse(screen, color_1_blue, rectangle(x0 + 50, y0 - 125, 70, 35, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 95, y0 - 120, 75, 25, size))
    ellipse(screen, color_1_lilac, rectangle(x0 + 80, y0 - 115, 70, 30, size))
    ellipse(screen, color_1_blue, rectangle(x0 + 90, y0 - 110, 70, 25, size))
    ellipse(screen, color_1_blue, rectangle(x0 + 70, y0 - 100, 80, 40, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 80, y0 - 95, 80, 40, size))
    ellipse(screen, color_1_lilac, rectangle(x0 + 100, y0 - 90, 75, 30, size))
    ellipse(screen, color_1_yellow, rectangle(x0 + 70, y0 - 87, 90, 35, size))
    ellipse(screen, color_2_pink, rectangle(x0 + 95, y0 - 82, 95, 25, size))

# делаем деревья
def tree(size, x0, y0, width, height):
    rect(screen, (255, 255, 255), rectangle(x0 * width, (y0 - 200) * height, 40 * width, 200 * height, size))
    ellipse(screen, (0, 128, 0), rectangle((x0 - 80) * width, (y0 - 280) * height, 200 * width, 150 * height, size))
    ellipse(screen, (0, 255, 0), rectangle((x0 - 80) * width, (y0 - 280) * height, 200 * width, 150 * height, size), 1)
    ellipse(screen, (0, 128, 0), rectangle((x0 - 50) * width, (y0 - 500) * height, 200 * width, 150 * height, size))
    ellipse(screen, (0, 255, 0), rectangle((x0 - 50) * width, (y0 - 500) * height, 200 * width, 150 * height, size), 1)
    ellipse(screen, (0, 128, 0), rectangle((x0 - 120) * width, (y0 - 400) * height, 300 * width, 175 * height, size))
    ellipse(screen, (0, 255, 0), rectangle((x0 - 120) * width, (y0 - 400) * height, 300 * width, 175 * height, size), 1)
    circle(screen, (255, 204, 170), (int((x0 + 70) * size * width), int((y0-170) * size * height)), int(30 * size))
    circle(screen, (0, 255, 0), (int((x0 + 70) * size * width), int((y0 - 170) * size * height)), int(30 * size), 1)
    circle(screen, (255, 204, 170), (int((x0 + -75) * size * width), int((y0 - 300) * size * height)), int(30 * size))
    circle(screen, (0, 255, 0), (int((x0 + -75) * size * width), int((y0 - 300) * size * height)), int(30 * size), 1)
    circle(screen, (255, 204, 170), (int((x0 + 120) * size * width), int((y0 - 300) * size * height)), int(30 * size))
    circle(screen, (0, 255, 0), (int((x0 + 120) * size * width), int((y0 - 300) * size * height)), int(30 * size), 1)
    circle(screen, (255, 204, 170), (int((x0 + 60) * size * width), int((y0 - 450) * size * height)), int(30 * size))
    circle(screen, (0, 255, 0), (int((x0 + 60) * size * width), int((y0 - 450) * size * height)), int(30 * size), 1)

# рисуем лошадь
def horse(x0, y0, size):

    white = (255, 255, 255)
    color_1_pink = (233, 175, 175)
    color_2_pink = (233, 198, 175)
    color_1_yellow = (255, 238, 170)
    color_1_green = (229, 255, 128)
    color_1_blue = (175, 233, 231)
    color_1_lilac = (221, 175, 233)

    # делаем верхнюю часть хвостса
    outranging_number_of_ellipses(x0, y0, size)

    # делаем нижнюю часть хвостса
    ellipse(screen, color_1_green, rectangle(x0 - 75, y0 - 80, 105, 50, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 60, y0 - 70, 90, 40, size))
    ellipse(screen, color_1_yellow, rectangle(x0 - 100, y0 - 60, 86, 35, size))
    ellipse(screen, color_1_blue, rectangle(x0 - 80, y0 - 55, 70, 30, size))
    ellipse(screen, color_1_lilac, rectangle(x0 - 90, y0 - 50, 65, 30, size))
    ellipse(screen, color_2_pink, rectangle(x0 - 65, y0 - 47, 70, 25, size))
    ellipse(screen, color_1_pink, rectangle(x0 - 60, y0 - 42, 60, 25, size))
    ellipse(screen, color_1_green, rectangle(x0 - 50, y0 - 40, 50, 30, size))

    # делаем туловище, ноги и голову
    rect(screen, white, rectangle(x0, y0 - 200, 20, 200, size))
    ellipse(screen, white, rectangle(x0 - 50, y0 - 250, 300, 100, size))
    rect(screen, white, rectangle(x0 + 60, y0 - 220, 20, 200, size))
    rect(screen, white, rectangle(x0 + 200, y0 - 220, 20, 200, size))
    rect(screen, white, rectangle(x0 + 140, y0 - 200, 20, 200, size))
    rect(screen, white, rectangle(x0 + 160, y0 - 350, 80, 150, size))
    ellipse(screen, white, rectangle(x0 + 130, y0 - 400, 120, 75, size))
    ellipse(screen, white, rectangle(x0 + 180, y0 - 380, 100, 50, size))

    # грива
    outranging_number_of_ellipses(x0+195, y0 - 190, size)

    # рог
    corn_point1 = (int((x0 + 145) * size), int((y0 - 387) * size))
    corn_point2 = (int((x0 + 160) * size), int((y0 - 497) * size))
    corn_point3 = (int((x0 + 180) * size), int((y0 - 397) * size))
    polygon(screen, color_1_pink, [corn_point1, corn_point2, corn_point3])

    # глаз
    circle(screen, (229, 128, 255), (int((x0 + 200) * size), int((y0 - 365) * size)), int(15 * size))
    circle(screen, (0, 0, 0), (int((x0 + 202) * size), int((y0 - 365) * size)), int(7 * size))
    ellipse(screen, white, rectangle(x0 + 187, y0 - 375, 15, 10, size))


def horse_reflected(x0, y0, size):

    white = (255, 255, 255)
    color_1_pink = (233, 175, 175)
    color_2_pink = (233, 198, 175)
    color_1_yellow = (255, 238, 170)
    color_1_green = (229, 255, 128)
    color_1_blue = (175, 233, 231)
    color_1_lilac = (221, 175, 233)

    # делаем верхнюю часть хвостса
    outranging_number_of_ellipses_reflected(x0, y0, size)

    # делаем нижнюю часть хвостса
    ellipse(screen, color_1_green, rectangle(x0 + 75, y0 - 80, 105, 50, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 60, y0 - 70, 90, 40, size))
    ellipse(screen, color_1_yellow, rectangle(x0 + 100, y0 - 60, 86, 35, size))
    ellipse(screen, color_1_blue, rectangle(x0 + 80, y0 - 55, 70, 30, size))
    ellipse(screen, color_1_lilac, rectangle(x0 + 90, y0 - 50, 65, 30, size))
    ellipse(screen, color_2_pink, rectangle(x0 + 65, y0 - 47, 70, 25, size))
    ellipse(screen, color_1_pink, rectangle(x0 + 60, y0 - 42, 60, 25, size))
    ellipse(screen, color_1_green, rectangle(x0 + 50, y0 - 40, 50, 30, size))

    # делаем туловище, ноги и голову
    rect(screen, white, rectangle(x0 + 60, y0 - 200, 20, 200, size))
    ellipse(screen, white, rectangle(x0 - 200, y0 - 250, 300, 100, size))
    rect(screen, white, rectangle(x0, y0 - 220, 20, 200, size))
    rect(screen, white, rectangle(x0 - 170, y0 - 220, 20, 200, size))
    rect(screen, white, rectangle(x0 - 110, y0 - 200, 20, 200, size))
    rect(screen, white, rectangle(x0 - 180, y0 - 350, 80, 150, size))
    ellipse(screen, white, rectangle(x0 - 200, y0 - 400, 120, 75, size))
    ellipse(screen, white, rectangle(x0 - 220, y0 - 380, 100, 50, size))

    # грива
    outranging_number_of_ellipses_reflected(x0 - 195, y0 - 190, size)

    # рог
    corn_point1 = (int((x0 - 95) * size), int((y0 - 387) * size))
    corn_point2 = (int((x0 - 110) * size), int((y0 - 497) * size))
    corn_point3 = (int((x0 - 130) * size), int((y0 - 397) * size))
    polygon(screen, color_1_pink, [corn_point1, corn_point2, corn_point3])

    # глаз
    circle(screen, (229, 128, 255), (int((x0 - 150) * size), int((y0 - 365) * size)), int(15 * size))
    circle(screen, (0, 0, 0), (int((x0 - 152) * size), int((y0 - 365) * size)), int(7 * size))
    ellipse(screen, white, rectangle(x0 - 157, y0 - 375, 15, 10, size))


# творим чудо
pygame.init()

FPS = 30


# подбираем коэфициент, чтобы все норм выглядело на экране
picture_size = 0.4

# фон
screen = pygame.display.set_mode((int(794*picture_size), int(1123*picture_size)))
rect(screen, (0, 255, 0), (0, 0, int(794*picture_size), int(1123*picture_size)))
rect(screen, (0, 255, 255), (0, 0, int(794*picture_size), int(512*picture_size)))

# солнце
for i in range(127):
    color = (int(255 * ((i) / 127)), 251 + int(4 * ((127 - i) / 127)), 85 + int(170 * ((127 - i) / 127)))
    circle(screen, color, (int(758*picture_size), int(112*picture_size)), int(100 - i*picture_size*100/127))

# деревья и лошади
tree(picture_size, 211, 594, 1.25, 1)
tree(picture_size, 75, 610, 1, 1.5)
tree(picture_size * 0.7, 275, 1010, 1.5, 1)
tree(picture_size, 175, 980, 1, 1)
tree(picture_size, 75, 1180, 1, 1)
horse(325, 1380, picture_size * 0.8)
horse_reflected(1195, 1580, picture_size * 0.6)
horse(1125, 1880, picture_size * 0.4)
horse_reflected(3395, 3080, picture_size * 0.2)

# радуемся


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()