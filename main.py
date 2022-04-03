from Planet import *
import pygame
# import math

pygame.init()

WIDTH, HEIGHT = 850, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 130, 230)
RED = (230, 40, 100)
DARK_GREY = (80, 90, 100)


def main():
    run = True
    clock = pygame.time.Clock()

    # define the sun
    sun = Planet(0, 0, 30, YELLOW, 1.98847 * 10**30)
    sun.isSun = True

    # define planets
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9722 * 10**24)
    earth.y_velocity = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_velocity = 24.077 * 1000

    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_velocity = 47.4 * 1000

    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_velocity = 35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:

            planet.update_position(planets=planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


main()
