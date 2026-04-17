import pygame
import sys
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

image = pygame.image.load("mickey_hand.png")

def draw_hand(angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=(300, 300))
    screen.blit(rotated, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    min_angle = -minutes * 6
    sec_angle = -seconds * 6

    screen.fill((255, 255, 255))

    draw_hand(min_angle)
    draw_hand(sec_angle)

    pygame.display.flip()
    clock.tick(1)