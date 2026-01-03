from circleshape import *
import pygame
import random
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) :
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(0 - angle)
        size = self.radius - ASTEROID_MIN_RADIUS
        A1 = Asteroid(self.position.x, self.position.y, size)
        A2 = Asteroid(self.position.x, self.position.y, size)
        A1.velocity = vect1 * 1.2
        A2.velocity = vect2 * 1.2

