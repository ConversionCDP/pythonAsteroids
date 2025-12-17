import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    number = 1
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        pygame.display.flip()
        for object in asteroids:
            collision = player.collides_with(object)
            if collision == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for object in asteroids:
            for bullet in shots:
                collision = object.collides_with(bullet)
                if collision == True:
                    log_event("asteroid_shot")
                    bullet.kill()
                    object.split()
        deltaTime = clock.tick(60)
        dt = deltaTime/1000
        


if __name__ == "__main__":
    main()
