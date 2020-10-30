import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREY = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
pygame.init()


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(GREY)

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_grid():
    blockSize = 100  # tamanho do bloco
    count = 1
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 2)


main()
