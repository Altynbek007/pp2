import pygame
from datetime import datetime


def get_angles():
    now = datetime.now()

    minute = now.minute
    second = now.second

    minute_angle = -(minute * 6)
    second_angle = -(second * 6)

    return minute_angle, second_angle


def rotate(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    return rotated, rect