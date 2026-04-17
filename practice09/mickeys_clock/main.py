import pygame
import os
from clock import get_angles, rotate

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey Clock")

BASE_DIR = os.path.dirname(__file__)

bg = pygame.image.load(os.path.join(BASE_DIR, "images/clock.PNG")).convert_alpha()
right_hand = pygame.image.load(os.path.join(BASE_DIR, "images/right_hand.PNG")).convert_alpha()
left_hand = pygame.image.load(os.path.join(BASE_DIR, "images/left_hand.PNG")).convert_alpha()

bg = pygame.transform.scale(bg, (800, 800))
right_hand = pygame.transform.scale(right_hand, (800, 800))
left_hand = pygame.transform.scale(left_hand, (800, 800))

center = (400, 400)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    minute_angle, second_angle = get_angles()

    # большая стрелка = секунды
    right_rotated, right_rect = rotate(right_hand, second_angle, center)

    # маленькая стрелка = минуты
    left_rotated, left_rect = rotate(left_hand, minute_angle, center)

    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    screen.blit(right_rotated, right_rect)
    screen.blit(left_rotated, left_rect)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()