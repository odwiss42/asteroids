import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        #check if game window has been closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update all
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        #fill window with black
        screen.fill("black")
        #refresh window
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        #wait 1/60s. Save delta time in seconds to dt
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
