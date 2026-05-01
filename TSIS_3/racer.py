import pygame
import random

LANES = [150, 250, 350]

def safe_spawn_x(player):
    safe = [x for x in LANES if abs(x - player.rect.x) > 80]
    return random.choice(safe)

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill((255,0,0) if color=="red" else (0,0,255))
        self.rect = self.image.get_rect(center=(250, 500))

        self.base_speed = 5
        self.speed = self.base_speed

        self.nitro = False
        self.shield = False
        self.timer = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        self.rect.x = max(150, min(350, self.rect.x))

        if self.timer > 0 and pygame.time.get_ticks() > self.timer:
            self.nitro = False
            self.shield = False
            self.speed = self.base_speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((50,80))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = safe_spawn_x(player)
        self.rect.y = -100
        self.speed = random.randint(5,8)

    def update(self):
        self.rect.y += self.speed


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.type = random.choice(["oil","barrier","pothole"])

        self.image = pygame.Surface((50,50))

        if self.type == "oil":
            self.image.fill((50,50,50))
        elif self.type == "barrier":
            self.image.fill((255,0,0))
        else:
            self.image.fill((255,255,0))

        self.rect = self.image.get_rect()
        self.rect.x = safe_spawn_x(player)
        self.rect.y = -100

    def update(self):
        self.rect.y += 5


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.type = random.choice(["Nitro","Shield","Repair"])

        self.image = pygame.Surface((40,40))

        if self.type == "Nitro":
            self.image.fill((0,255,255))
        elif self.type == "Shield":
            self.image.fill((255,215,0))
        else:
            self.image.fill((0,255,0))

        self.rect = self.image.get_rect()
        self.rect.x = safe_spawn_x(player)
        self.rect.y = -100

    def update(self):
        self.rect.y += 4