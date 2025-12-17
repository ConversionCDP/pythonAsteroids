from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            pass
        log_event("asteroid_split")
        randRot = random.uniform(20, 50)
        astVelocity = self.velocity
        astRotate = astVelocity.rotate(randRot)
        negRotate = astVelocity.rotate(-randRot)
        newRad = self.radius - ASTEROID_MIN_RADIUS
        firstAst = Asteroid(self.position.x, self.position.y, newRad)
        firstAst.velocity = astRotate*1.2
        secondAst = Asteroid(self.position.x, self.position.y, newRad)
        secondAst.velocity = negRotate*1.2


    def update(self, dt):
        self.position = (self.velocity*dt) + self.position