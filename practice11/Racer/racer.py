import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# ===== WINDOW SETTINGS =====
WIDTH, HEIGHT = 1400, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game(ШАШКИ)")
clock = pygame.time.Clock()

# ===== PATHS =====
BASE_DIR = os.path.dirname(__file__)

def load_path(*path):
    return os.path.join(BASE_DIR, *path)

# ===== IMAGES =====
road = pygame.image.load(load_path("image", "road.png"))
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

car_img = pygame.image.load(load_path("image", "car.png"))
car_img = pygame.transform.scale(car_img, (80, 140))

enemy_img1 = pygame.image.load(load_path("image", "enemy.png"))
enemy_img1 = pygame.transform.scale(enemy_img1, (80, 140))

enemy_img2 = pygame.image.load(load_path("image", "enemy2.png"))
enemy_img2 = pygame.transform.scale(enemy_img2, (80, 140))

enemy_images = [enemy_img1, enemy_img2]

# ===== MUSIC =====
music_folder = load_path("music")

playlist = [
    os.path.join(music_folder, f)
    for f in os.listdir(music_folder)
    if f.endswith(".mp3") or f.endswith(".wav")
]

playlist.sort()

current_track = 0
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play(-1)

# ===== GAME VARIABLES =====
road_y = 0
base_speed = 10  

car = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 160, 80, 140)

coins = []
coin_timer = 0
score = 0

enemies = []
enemy_timer = 0

game_over = False
font = pygame.font.SysFont("Arial", 30)

# ===== COIN TYPES (color, value) =====
coin_types = [
    {"color": (255, 215, 0), "value": 1},   # золотая
    {"color": (0, 255, 255), "value": 2},   # голубая
    {"color": (255, 0, 255), "value": 3},   # редкая
]

running = True
while running:
    clock.tick(60)

    # скорость дороги зависит от очков
    speed = base_speed + score * 0.1

    # ===== EVENTS =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # управление музыкой
            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_m:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            # рестарт игры
            if game_over and event.key == pygame.K_r:
                game_over = False
                score = 0
                coins.clear()
                enemies.clear()
                car.x = WIDTH // 2 - 40

    if not game_over:

        # ===== MOVEMENT =====
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            car.x -= 10
        if keys[pygame.K_RIGHT]:
            car.x += 10

        # ограничения
        if car.x < 0:
            car.x = 0
        if car.x > WIDTH - car.width:
            car.x = WIDTH - car.width

        # ===== ROAD =====
        road_y += speed
        if road_y >= HEIGHT:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - HEIGHT))

        # ===== COINS SPAWN =====
        coin_timer += 1
        if coin_timer > 40:
            x = random.randint(50, WIDTH - 50)

            coin_type = random.choice(coin_types)

            coins.append({
                "rect": pygame.Rect(x, -20, 25, 25),
                "type": coin_type
            })

            coin_timer = 0

        # ===== COINS UPDATE =====
        for coin in coins[:]:
            coin["rect"].y += speed

            # сбор монеты
            if car.colliderect(coin["rect"]):
                score += coin["type"]["value"]
                coins.remove(coin)

            elif coin["rect"].y > HEIGHT:
                coins.remove(coin)

        # ===== ENEMY SPEED SCALING =====
        enemy_speed_bonus = score // 5  # каждые 5 очков ускорение

        # ===== ENEMIES SPAWN =====
        enemy_timer += 1
        if enemy_timer > 50:
            x = random.randint(50, WIDTH - 130)
            rect = pygame.Rect(x, -150, 80, 140)
            img = random.choice(enemy_images)
            enemies.append([rect, img])
            enemy_timer = 0

        # ===== ENEMIES UPDATE =====
        for enemy in enemies[:]:
            enemy[0].y += speed + 3 + enemy_speed_bonus

            if car.colliderect(enemy[0]):
                game_over = True

            if enemy[0].y > HEIGHT:
                enemies.remove(enemy)

        # ===== DRAW CAR =====
        screen.blit(car_img, (car.x, car.y))

        # ===== DRAW COINS =====
        for coin in coins:
            pygame.draw.circle(
                screen,
                coin["type"]["color"],
                coin["rect"].center,
                12
            )

        # ===== DRAW ENEMIES =====
        for enemy in enemies:
            screen.blit(enemy[1], (enemy[0].x, enemy[0].y))

        # ===== UI =====
        screen.blit(font.render(f"Coins: {score}", True, (255, 255, 255)), (WIDTH - 170, 10))
        screen.blit(font.render(f"Speed: {int(speed)}", True, (200, 200, 200)), (10, 10))
        screen.blit(font.render(f"Track: {current_track + 1}", True, (200, 200, 200)), (10, 40))

    else:
        # ===== GAME OVER SCREEN =====
        screen.fill((0, 0, 0))

        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (WIDTH//2 - 120, HEIGHT//2 - 50))
        screen.blit(font.render("Press R to restart", True, (255, 255, 255)), (WIDTH//2 - 150, HEIGHT//2 + 10))
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 0)), (WIDTH//2 - 80, HEIGHT//2 + 60))

    pygame.display.flip()

pygame.quit()

# ===== УПРАВЛЕНИЕ =====

# ← (LEFT)  - движение машины влево
# → (RIGHT) - движение машины вправо

# N - следующий трек
# P - предыдущий трек
# M - пауза / продолжить музыку

# R - рестарт игры (после GAME OVER)

# Закрытие окна (крестик) - выход из игры