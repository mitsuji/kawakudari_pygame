# kawakudari-pygame

This project implements part of the [std15.h](https://github.com/IchigoJam/c4ij/blob/master/src/std15.h) API (from [c4ij](https://github.com/IchigoJam/c4ij)) with [pygame](https://www.pygame.org), and [Kawakudari Game](https://ichigojam.github.io/print/en/KAWAKUDARI.html) on top of it.

It will allow programming for [IchigoJam](https://ichigojam.net/index-en.html)-like targets that display [IchigoJam FONT](https://mitsuji.github.io/ichigojam-font.json/) on screen using a Python programming language.
```

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

```

## Prerequisite

* [Download](https://www.python.org/downloads/) and install Python suitable for your environment.
* [Download](https://www.pygame.org/wiki/GettingStarted) and install pygame library.

```
$ pip3 install pygame --user
```


## How to use

To run it
```
$ python3 kawakudari.py
```


## License
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
[CC BY](https://creativecommons.org/licenses/by/4.0/) [mitsuji.org](https://mitsuji.org)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
