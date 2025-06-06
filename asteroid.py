import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid_1_velocity = self.velocity.rotate(angle)
        asteroid_2_velocity = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], radius)
        asteroid1.velocity = asteroid_1_velocity * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], radius)
        asteroid2.velocity = asteroid_2_velocity * 1.2