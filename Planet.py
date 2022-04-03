import pygame
import math

pygame.init()

WIDTH, HEIGHT = 850, 800
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("comicsans", 14)


class Planet:
    # defining some constants
    AU = 150.6e6 * 1000  # astronomical unit: roughly the distance from Earth to the Sun and equal to about 150 million kilometres
    G = 6.67428e-11
    SCALE = 250 / AU  # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24   # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.isSun = False
        self.distance_to_sun = 0

        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, window):
        # Here we need every thing to begin from the center of the screen
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                point_x, point_y = point
                point_x = point_x * self.SCALE + WIDTH / 2
                point_y = point_y * self.SCALE + HEIGHT / 2
                updated_points.append((point_x, point_y))

            pygame.draw.lines(window, self.color, False, updated_points)

        if not self.isSun:
            distance_text = FONT.render(
                f"{round(self.distance_to_sun/1000,1)}Km", 1, WHITE)
            window.blit(distance_text, (x - distance_text.get_width() /
                        2, y - distance_text.get_height() / 2))
        pygame.draw.circle(window, self.color, (x, y), self.radius)

    def attraction(self, other_planet):
        other_planet_x, other_planet_y = other_planet.x, other_planet.y
        distance_x = other_planet_x - self.x
        distance_y = other_planet_y - self.y
        distance = math.sqrt(pow(distance_x, 2) + pow(distance_y, 2))

        if other_planet.isSun:
            self.distance_to_sun = distance

        force = (self.G * self.mass * other_planet.mass) / pow(distance, 2)
        theta = math.atan2(distance_y, distance_x)
        force_in_x = force * math.cos(theta)
        force_in_y = force * math.sin(theta)
        return force_in_x, force_in_y

    def update_position(self, planets):
        total_force_in_x = total_force_in_y = 0
        for planet in planets:

            if self == planet:
                continue

            fx, fy = self.attraction(planet)

            total_force_in_x += fx
            total_force_in_y += fy

        self.x_velocity += total_force_in_x / self.mass * self.TIMESTEP
        self.y_velocity += total_force_in_y / self.mass * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))
