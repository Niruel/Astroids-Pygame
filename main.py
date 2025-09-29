import pygame
import sys
from constants import*
from player import*
from asteroid import*
from asteroidfield import*
from shot import*
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

   
    Asteroid.containers = (asteroid_group, updateable, drawable)
    Shot.containers = (shot_group, updateable, drawable)

    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        #player.update(dt)
        updateable.update(dt)
        for asteroid in asteroid_group:
           if  asteroid.check_collision(player):
                print("Game over")
                sys.exit()
        
        for asteroid in asteroid_group:
            for bullet in shot_group:
                    if(bullet.check_collision(asteroid)):
                        asteroid.split()
                        bullet.kill()


        screen.fill("black")
        #player.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        
        


if __name__ == "__main__":
    main()
