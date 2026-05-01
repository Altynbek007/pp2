import pygame
import random

CELL = 20
WIDTH, HEIGHT = 600, 600

class Game:
    def __init__(self):
        self.snake = [(300,300)]
        self.direction = (CELL, 0)

        self.food = self.spawn()
        self.poison = self.spawn()

        self.score = 0
        self.level = 1
        self.speed = 10

        self.powerup = None
        self.power_timer = 0

        self.obstacles = []

    def spawn(self):
        return (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))

    def spawn_obstacles(self):
        self.obstacles = []
        for _ in range(5):
            self.obstacles.append(self.spawn())

    def move(self):
        head = (self.snake[0][0] + self.direction[0],
                self.snake[0][1] + self.direction[1])

        #ГРАНИЦЫ
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return "GAMEOVER"

        #САМ В СЕБЯ
        if head in self.snake:
            return "GAMEOVER"

        #ОБСТАКЛЫ
        if head in self.obstacles:
            return "GAMEOVER"

        self.snake.insert(0, head)

        #еда
        if head == self.food:
            self.score += 10
            self.food = self.spawn()

        #яд
        elif head == self.poison:
            self.snake = self.snake[:-2]
            if len(self.snake) <= 1:
                return "GAMEOVER"

        else:
            self.snake.pop()

        #уровень
        self.level = self.score // 50 + 1

        if self.level >= 3:
            self.spawn_obstacles()

        return "OK"

    def update(self):
        #power-up таймер
        if self.powerup and pygame.time.get_ticks() > self.power_timer:
            self.powerup = None
            self.speed = 10

        return self.move()

    def draw(self, screen):
        #snake
        for s in self.snake:
            pygame.draw.rect(screen, (0,255,0), (*s, CELL, CELL))

        #food
        pygame.draw.rect(screen, (255,0,0), (*self.food, CELL, CELL))

        #poison
        pygame.draw.rect(screen, (150,0,0), (*self.poison, CELL, CELL))

        #obstacles
        for o in self.obstacles:
            pygame.draw.rect(screen, (100,100,100), (*o, CELL, CELL))