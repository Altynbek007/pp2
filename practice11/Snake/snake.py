import pygame
import random

pygame.init()

# ===== SETTINGS =====
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ===== COLORS =====
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# ===== SNAKE =====
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# ===== FOOD TYPES (color, score, lifetime) =====
food_types = [
    {"color": RED, "score": 1, "time": 300},     # обычная еда
    {"color": BLUE, "score": 2, "time": 200},    # средняя
    {"color": YELLOW, "score": 3, "time": 120},  # редкая (быстро исчезает)
]

# ===== GENERATE FOOD =====
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        
        if (x, y) not in snake:
            food_type = random.choice(food_types)
            return {
                "pos": (x, y),
                "type": food_type,
                "timer": food_type["time"]
            }

food = generate_food()

# ===== GAME STATS =====
score = 0
level = 1
food_eaten = 0
speed = 10

running = True
while running:
    screen.fill(BLACK)

    # ===== EVENTS =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # управление змейкой
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # ===== MOVE SNAKE =====
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # ===== COLLISIONS =====
    # выход за границы
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False

    # столкновение с собой
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # ===== FOOD LOGIC =====
    if new_head == food["pos"]:
        score += food["type"]["score"]  # добавляем очки в зависимости от еды
        food_eaten += 1
        food = generate_food()
    else:
        snake.pop()

    # ===== FOOD TIMER =====
    food["timer"] -= 1
    if food["timer"] <= 0:
        food = generate_food()  # еда исчезает и появляется новая

    # ===== LEVEL SYSTEM =====
    if food_eaten >= 3:
        level += 1
        food_eaten = 0
        speed += 2

    # ===== DRAW SNAKE =====
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # ===== DRAW FOOD =====
    pygame.draw.rect(
        screen,
        food["type"]["color"],
        (food["pos"][0], food["pos"][1], CELL_SIZE, CELL_SIZE)
    )

    # ===== UI =====
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()