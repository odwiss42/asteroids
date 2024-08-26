import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, 'aliceblue', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_vel_1 = self.velocity.rotate(angle)
        new_vel_2 = self.velocity.rotate((-angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        newroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        newroid_1.velocity = new_vel_1 * ASTEROID_SPLIT_SPEED
        newroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        newroid_2.velocity = new_vel_2 * ASTEROID_SPLIT_SPEED