import pygame
from clock import get_angles, rotate

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey Clock")

bg = pygame.image.load("images/clock.jpeg").convert_alpha()
right_hand = pygame.image.load("images/right_hand.png").convert_alpha()
left_hand = pygame.image.load("images/left_hand.png").convert_alpha()

right_hand = pygame.transform.scale(right_hand, (1000, 1000))
left_hand = pygame.transform.scale(left_hand, (1000, 1000))


bg = pygame.transform.scale(bg, (800, 800))

center = (400, 400)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    minute_angle, second_angle = get_angles()

    right_rotated, right_rect = rotate(right_hand, minute_angle, center)
    left_rotated, left_rect = rotate(left_hand, second_angle, center)

    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    screen.blit(right_rotated, right_rect)
    screen.blit(left_rotated, left_rect)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()