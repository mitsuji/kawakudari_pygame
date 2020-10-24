import pygame
import random
from ichigojam import Std15
from ichigojam import DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT

def main():
    pygame.init()
    screen = pygame.display.set_mode((512,384))
    clock = pygame.time.Clock()

    std15 = Std15(512, 384, 32, 24)
    frame = 0
    x = 15
    running = True

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                elif event.key == pygame.K_RIGHT:
                    x += 1

        if not running:
            continue
        if frame % 5 == 0:
            std15.locate(x, 5)
            std15.putc(ord('0'))
            std15.locate(random.randrange(32), 23)
            std15.putc(ord('*'))
            std15.scroll(DIR_UP)
            if std15.scr(x,5) != 0:
                std15.locate(0,23)
                std15.putstr("Game Over...")
                std15.putnum(frame)
                running = False
        frame += 1
  
        std15.draw_screen(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()

