import pygame
import sys
from Player import Player
from Apple import Apple
pygame.init()
pygame.font.init()

LENGTH = 500
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

SIZE_OF_AREA = 10
BLOCK_SIZE = LENGTH / SIZE_OF_AREA

screen = pygame.display.set_mode((LENGTH, LENGTH))
clock = pygame.time.Clock()

def game():

    player = Player(1, 1)
    apple = Apple(5, 5)

    while 1:
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dir = 'right'
                if event.key == pygame.K_LEFT:
                    player.dir = 'left'
                if event.key == pygame.K_UP:
                    player.dir = 'up'
                if event.key == pygame.K_DOWN:
                    player.dir = 'down'

        player.update_parts()
        player.update_movement()
        player.update_score(apple)

        is_dead = player.update_collision(SIZE_OF_AREA)
        if is_dead:
            return player.size

        apple.update_collision(player, SIZE_OF_AREA)

        screen.fill(GREEN)

        apple_rect = pygame.Rect(apple.x * BLOCK_SIZE, apple.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, apple_rect)

        player_rect = pygame.Rect(player.x * BLOCK_SIZE, player.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, BLUE, player_rect)

        for part in player.parts:
            part_rect = pygame.Rect(part[0] * BLOCK_SIZE, part[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, BLUE, part_rect)

        pygame.display.flip()

font = pygame.font.Font(pygame.font.get_default_font(), 36)

screen.fill(GREEN)
score = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            score = game()

    welcome_text = font.render('Press SPACE to start', False, BLACK)
    screen.blit(welcome_text, dest=(LENGTH / 2 - welcome_text.get_rect().width / 2, LENGTH * (2 / 3)))

    score_text = font.render(f'Score: {score}', False, BLACK)
    screen.blit(score_text, dest=(LENGTH / 2 - score_text.get_rect().width / 2, LENGTH * (1 / 3)))
    pygame.display.flip()