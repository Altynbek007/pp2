import pygame
import sys
import math
import os
from datetime import datetime
from PIL import Image

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
center = (300, 300)

BASE_DIR = os.path.dirname(__file__)

def load_image(path):
    img = Image.open(path).convert("RGBA")
    mode = img.mode
    size = img.size
    data = img.tobytes()
    return pygame.image.fromstring(data, size, mode)

# загружаем картинки
mickey = load_image(os.path.join(BASE_DIR, "images/clock.png"))
left_hand = load_image(os.path.join(BASE_DIR, "images/lefthand.png"))
right_hand = load_image(os.path.join(BASE_DIR, "images/righthand.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ⏰ ВРЕМЯ АЛМАТЫ (UTC+5)
    now = datetime.utcnow()
    minutes = now.minute
    seconds = now.second

    min_angle = math.radians(minutes * 6 - 90)
    sec_angle = math.radians(seconds * 6 - 90)

    screen.fill((255, 255, 255))

    # фон
    screen.blit(mickey, mickey.get_rect(center=center))

    # вращение рук
    def draw_hand(img, angle):
        rotated = pygame.transform.rotate(img, angle)
        rect = rotated.get_rect(center=center)
        screen.blit(rotated, rect)

    draw_hand(right_hand, min_angle)
    draw_hand(left_hand, sec_angle)

    pygame.display.flip()
    clock.tick(1)