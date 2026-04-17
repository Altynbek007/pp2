import pygame
from datetime import datetime

def get_angles():
    now = datetime.now()  # локальное время (Алматы)

    minutes = now.minute
    seconds = now.second

    # маленькая стрелка (минуты)
    minute_angle = -(minutes * 6)

    # большая стрелка (секунды)
    second_angle = -(seconds * 6)

    return minute_angle, second_angle


def rotate(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    return rotated, rect