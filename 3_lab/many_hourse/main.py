import pygame
import pygame.draw as dr

FPS = 30

# constant colours
PINK_1 = (233, 175, 175)
PINK_2 = (233, 198, 175)
YELLOW = (255, 238, 170)
GREEN = (229, 255, 128)
BLUE = (175, 233, 231)
LILAC = (221, 175, 233)
WHITE = (255, 255, 255)


def work_surface(n1, n2, n3, n4, size):
    """
    Draw work surface
    :param n1: coordinates of left top corner
    :param n2: coordinates of left top corner
    :param n3: size of rectangle
    :param n4: size of rectangle
    :param size: variable for existence of proportion
    :return: 4 int size variables
    """
    return int(n1 * size), int(n2 * size), int(n3 * size), int(n4 * size)

def unicorns_tail_from_ellipses(x0: int, y0: int, size: int, flip = True):
    """
    Draw ellipses for unicorn's tail
    :param flip: if true: normal orientation (left), if false: reflected
    :param x0: coordinate of left top corner
    :param y0: coordinate of left top corner
    :param size:variable for existence of proportion
    :return: nothing
    """
    if flip:
        side = -1
    else:
        side = 1
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*80, y0 - 200, 50, 20, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 + side*85, y0 - 190, 40, 35, size))
    dr.ellipse(screen, YELLOW, work_surface(x0 + side*65, y0 - 185, 40, 25, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*62, y0 - 170, 50, 20, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 + side*90, y0 - 167, 40, 15, size))
    dr.ellipse(screen, LILAC, work_surface(x0 + side*80, y0 - 155, 50, 20, size))
    dr.ellipse(screen, GREEN, work_surface(x0 + side*90, y0 - 160, 40, 25, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 + side*55, y0 - 158, 50, 30, size))
    dr.ellipse(screen, YELLOW, work_surface(x0 + side*80, y0 - 150, 50, 30, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*95, y0 - 147, 50, 35, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*60, y0 - 140, 40, 20, size))
    dr.ellipse(screen, BLUE, work_surface(x0 + side*80, y0 - 130, 60, 30, size))
    dr.ellipse(screen, BLUE, work_surface(x0 + side*50, y0 - 125, 70, 35, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*95, y0 - 120, 75, 25, size))
    dr.ellipse(screen, LILAC, work_surface(x0 + side*80, y0 - 115, 70, 30, size))
    dr.ellipse(screen, BLUE, work_surface(x0 + side*90, y0 - 110, 70, 25, size))
    dr.ellipse(screen, BLUE, work_surface(x0 + side*70, y0 - 100, 80, 40, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + side*80, y0 - 95, 80, 40, size))
    dr.ellipse(screen, LILAC, work_surface(x0 + side*100, y0 - 90, 75, 30, size))
    dr.ellipse(screen, YELLOW, work_surface(x0 + side*70, y0 - 87, 90, 35, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 + side*95, y0 - 82, 95, 25, size))

def sun(x):
    """
    Draw sun in top right corner
    :param x: intensity of sun glowing, can be only 0 <= x <= 128
    """
    for i in range(x):
        color = (int(255 * (i / 127)), 251 + int(4 * ((127 - i) / 127)), 85 + int(170 * ((127 - i) / 127)))
        dr.circle(screen, color, (int(758 * picture_size), int(112 * picture_size)),
                int(100 - i * picture_size * 100 / 127))

def tree(size, x0, y0, width, height):
    """
    Draw tree with greenness
    :param size: coefficient of proportion
    :param x0: coordinate of left top corner
    :param y0: coordinate of left top corner
    :param width:
    :param height:
    """
    dr.rect(screen, (255, 255, 255), work_surface(x0 * width, (y0 - 200) * height, 40 * width, 200 * height, size))
    dr.ellipse(screen, (0, 128, 0),
               work_surface((x0 - 80) * width, (y0 - 280) * height, 200 * width, 150 * height, size))
    dr.ellipse(screen, (0, 255, 0),
               work_surface((x0 - 80) * width, (y0 - 280) * height, 200 * width, 150 * height, size), 1)
    dr.ellipse(screen, (0, 128, 0),
               work_surface((x0 - 50) * width, (y0 - 500) * height, 200 * width, 150 * height, size))
    dr.ellipse(screen, (0, 255, 0),
               work_surface((x0 - 50) * width, (y0 - 500) * height, 200 * width, 150 * height, size), 1)
    dr.ellipse(screen, (0, 128, 0),
               work_surface((x0 - 120) * width, (y0 - 400) * height, 300 * width, 175 * height, size))
    dr.ellipse(screen, (0, 255, 0),
               work_surface((x0 - 120) * width, (y0 - 400) * height, 300 * width, 175 * height, size), 1)
    dr.circle(screen, (255, 204, 170), (int((x0 + 70) * size * width), int((y0 - 170) * size * height)), int(30 * size))
    dr.circle(screen, (0, 255, 0), (int((x0 + 70) * size * width), int((y0 - 170) * size * height)), int(30 * size), 1)
    dr.circle(screen, (255, 204, 170), (int((x0 + -75) * size * width), int((y0 - 300) * size * height)),
              int(30 * size))
    dr.circle(screen, (0, 255, 0), (int((x0 + -75) * size * width), int((y0 - 300) * size * height)), int(30 * size), 1)
    dr.circle(screen, (255, 204, 170), (int((x0 + 120) * size * width), int((y0 - 300) * size * height)),
              int(30 * size))
    dr.circle(screen, (0, 255, 0), (int((x0 + 120) * size * width), int((y0 - 300) * size * height)), int(30 * size), 1)
    dr.circle(screen, (255, 204, 170), (int((x0 + 60) * size * width), int((y0 - 450) * size * height)), int(30 * size))
    dr.circle(screen, (0, 255, 0), (int((x0 + 60) * size * width), int((y0 - 450) * size * height)), int(30 * size), 1)

def body(x0, y0, size):
    """
    Draw unicorn's body
    :param x0: coordinate of top left corner
    :param y0: coordinate of top left corner
    :param size: coefficient of proportion
    """

    dr.rect(screen, WHITE, work_surface(x0, y0 - 200, 20, 200, size))
    dr.ellipse(screen, WHITE, work_surface(x0 - 50, y0 - 250, 300, 100, size))
    dr.rect(screen, WHITE, work_surface(x0 + 60, y0 - 220, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 + 200, y0 - 220, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 + 140, y0 - 200, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 + 160, y0 - 350, 80, 150, size))
    dr.ellipse(screen, WHITE, work_surface(x0 + 130, y0 - 400, 120, 75, size))
    dr.ellipse(screen, WHITE, work_surface(x0 + 180, y0 - 380, 100, 50, size))

def horn(x0, y0, size):
    """
    Draw horn for horse to become an unicorn
    :param x0: coordinate of top left corner
    :param y0: coordinate of top left corner
    :param size: coefficient of proportion
    """

    corn_point1 = (int((x0 + 145) * size), int((y0 - 387) * size))
    corn_point2 = (int((x0 + 160) * size), int((y0 - 497) * size))
    corn_point3 = (int((x0 + 180) * size), int((y0 - 397) * size))
    dr.polygon(screen, PINK_1, [corn_point1, corn_point2, corn_point3])

def eye(x0, y0, size):
    """
    Draw unicorn's eye
    :param x0: coordinate of top left corner
    :param y0: coordinate of top left corner
    :param size: coefficient of proportion
    """
    dr.circle(screen, (229, 128, 255), (int((x0 + 200) * size), int((y0 - 365) * size)), int(15 * size))
    dr.circle(screen, (0, 0, 0), (int((x0 + 202) * size), int((y0 - 365) * size)), int(7 * size))
    dr.ellipse(screen, WHITE, work_surface(x0 + 187, y0 - 375, 15, 10, size))

def horse(x0, y0, size):
    """
    Draw horse and lower part of horse tail
    :param x0: coordinate of left top rectangle where unicorn is
    :param y0: coordinate of left top rectangle where unicorn is
    :param size: coefficient of proportion
    """
    unicorns_tail_from_ellipses(x0, y0, size)

    #lower part of tail
    dr.ellipse(screen, GREEN, work_surface(x0 - 75, y0 - 80, 105, 50, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 - 60, y0 - 70, 90, 40, size))
    dr.ellipse(screen, YELLOW, work_surface(x0 - 100, y0 - 60, 86, 35, size))
    dr.ellipse(screen, BLUE, work_surface(x0 - 80, y0 - 55, 70, 30, size))
    dr.ellipse(screen, LILAC, work_surface(x0 - 90, y0 - 50, 65, 30, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 - 65, y0 - 47, 70, 25, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 - 60, y0 - 42, 60, 25, size))
    dr.ellipse(screen, GREEN, work_surface(x0 - 50, y0 - 40, 50, 30, size))

    body(x0, y0, size)
    horn(x0, y0, size)
    eye(x0, y0, size)
    unicorns_tail_from_ellipses(x0 + 195, y0 - 190, size)


def horse_reflected(x0, y0, size):
    """
    Draw reflected unicorn
    :param x0: coordinate of top left corner
    :param y0: coordinate of top left corner
    :param size: coefficient of proportion
    """
    # upper part of the unicorn's tail
    unicorns_tail_from_ellipses(x0, y0, size, False)

    # lower part of the unicorn's tail
    dr.ellipse(screen, GREEN, work_surface(x0 + 75, y0 - 80, 105, 50, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + 60, y0 - 70, 90, 40, size))
    dr.ellipse(screen, YELLOW, work_surface(x0 + 100, y0 - 60, 86, 35, size))
    dr.ellipse(screen, BLUE, work_surface(x0 + 80, y0 - 55, 70, 30, size))
    dr.ellipse(screen, LILAC, work_surface(x0 + 90, y0 - 50, 65, 30, size))
    dr.ellipse(screen, PINK_2, work_surface(x0 + 65, y0 - 47, 70, 25, size))
    dr.ellipse(screen, PINK_1, work_surface(x0 + 60, y0 - 42, 60, 25, size))
    dr.ellipse(screen, GREEN, work_surface(x0 + 50, y0 - 40, 50, 30, size))

    #draw body, legs
    dr.rect(screen, WHITE, work_surface(x0 + 60, y0 - 200, 20, 200, size))
    dr.ellipse(screen, WHITE, work_surface(x0 - 200, y0 - 250, 300, 100, size))
    dr.rect(screen, WHITE, work_surface(x0, y0 - 220, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 - 170, y0 - 220, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 - 110, y0 - 200, 20, 200, size))
    dr.rect(screen, WHITE, work_surface(x0 - 180, y0 - 350, 80, 150, size))
    dr.ellipse(screen, WHITE, work_surface(x0 - 200, y0 - 400, 120, 75, size))
    dr.ellipse(screen, WHITE, work_surface(x0 - 220, y0 - 380, 100, 50, size))

    # hair
    unicorns_tail_from_ellipses(x0 - 195, y0 - 190, size, False)


    # horn
    corn_point1 = (int((x0 - 95) * size), int((y0 - 387) * size))
    corn_point2 = (int((x0 - 110) * size), int((y0 - 497) * size))
    corn_point3 = (int((x0 - 130) * size), int((y0 - 397) * size))
    dr.polygon(screen, PINK_1, [corn_point1, corn_point2, corn_point3])

    # eye
    dr.circle(screen, (229, 128, 255), (int((x0 - 150) * size), int((y0 - 365) * size)), int(15 * size))
    dr.circle(screen, (0, 0, 0), (int((x0 - 152) * size), int((y0 - 365) * size)), int(7 * size))
    dr.ellipse(screen, WHITE, work_surface(x0 - 157, y0 - 375, 15, 10, size))

pygame.init()

# choose proposal coefficient for normal view
picture_size = 0.8

screen = pygame.display.set_mode((int(794 * picture_size), int(1123 * picture_size)))
dr.rect(screen, (0, 255, 0), (0, 0, int(794 * picture_size), int(1123 * picture_size)))
dr.rect(screen, (0, 255, 255), (0, 0, int(794 * picture_size), int(512 * picture_size)))

# unicorns and trees
tree(picture_size, 211, 594, 1.25, 1)
tree(picture_size, 75, 610, 1, 1.5)
tree(picture_size * 0.7, 275, 1010, 1.5, 1)
tree(picture_size, 175, 980, 1, 1)
tree(picture_size, 75, 1180, 1, 1)
horse(325, 1380, picture_size * 0.8)
horse_reflected(1195, 1580, picture_size * 0.6)
horse(1125, 1880, picture_size * 0.4)
horse_reflected(3395, 3080, picture_size * 0.2)
sun(125)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
