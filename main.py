# inports

import pygame
import random

# Pygame init and screen settings

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space invader')
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/invader.png')
playerX = 370
playerY = 500
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = pygame.image.load('img/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Main loop
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.2

            if event.key == pygame.K_RIGHT:
                playerX_change = .2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

