import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
falling_speed = 5
speed = 2

screen_width = 864
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Spawn Game")

score = 0

bg = pygame.image.load("fruit game/bg.jpeg")
apple = pygame.image.load("fruit game/apple.png")
banana = pygame.image.load("friuit game/banana.png")
orange = pygame.image.load("fruit game/orange.png")
basket = pygame.image.load("fruit game/basket.png")

# def apple_drop():
# def banana_drop():
# def orange_drop():

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        y -= speed

    if keys[K_DOWN]:
        y += speed

    if keys[K_LEFT]:
        x -= speed

    if keys[K_RIGHT]:
        x += speed
