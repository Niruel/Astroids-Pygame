import pygame
import random
from circleshape import*
from constants import*

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "white",self.position,self.radius,width)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20.0, 50.0)
        positive_vector = self.velocity.rotate(angle)
        negitive_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        astroid_one.velocity = positive_vector * 1.2
        astroid_two.velocity = negitive_vector