import pygame
import sys
import random

from racer import *
from ui import *
from persistence import *

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

settings = load_settings()

state = "MENU"
player_name = ""

player = None
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
powerups = pygame.sprite.Group()

score = 0
distance = 0

# кнопки
btn_play = Button(200,150,200,50,"Play")
btn_board = Button(200,220,200,50,"Leaderboard")
btn_settings = Button(200,290,200,50,"Settings")
btn_back = Button(200,500,200,50,"Back")
btn_sound = Button(200,350,200,50,"Sound")
btn_color = Button(200,420,200,50,"Color")

name_input = TextInput(200,250,200,40)

# таймеры
SPAWN_ENEMY = pygame.USEREVENT + 1
SPAWN_OBSTACLE = pygame.USEREVENT + 2
SPAWN_POWERUP = pygame.USEREVENT + 3

pygame.time.set_timer(SPAWN_ENEMY, 1200)
pygame.time.set_timer(SPAWN_OBSTACLE, 2000)
pygame.time.set_timer(SPAWN_POWERUP, 5000)


def reset_game():
    global player, score, distance
    all_sprites.empty()
    enemies.empty()
    obstacles.empty()
    powerups.empty()

    player = Player(settings["car_color"])
    all_sprites.add(player)

    score = 0
    distance = 0


running = True
while running:
    screen.fill((30,30,30))
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if state == "MENU":
            if btn_play.is_clicked(event): state = "NAME"
            if btn_board.is_clicked(event): state = "BOARD"
            if btn_settings.is_clicked(event): state = "SETTINGS"

        elif state == "NAME":
            name_input.handle_event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player_name = name_input.text or "Player"
                reset_game()
                state = "PLAY"

        elif state == "SETTINGS":
            if btn_back.is_clicked(event): state = "MENU"

            if btn_sound.is_clicked(event):
                settings["sound"] = not settings["sound"]
                save_settings(settings)

            if btn_color.is_clicked(event):
                settings["car_color"] = "blue" if settings["car_color"]=="red" else "red"
                save_settings(settings)

        elif state == "PLAY":

            if event.type == SPAWN_ENEMY:
                e = Enemy(player)
                enemies.add(e)
                all_sprites.add(e)

            if event.type == SPAWN_OBSTACLE:
                o = Obstacle(player)
                obstacles.add(o)
                all_sprites.add(o)

            if event.type == SPAWN_POWERUP:
                p = PowerUp(player)
                powerups.add(p)
                all_sprites.add(p)

    if state == "MENU":
        btn_play.draw(screen)
        btn_board.draw(screen)
        btn_settings.draw(screen)

    elif state == "NAME":
        screen.blit(font.render("Enter Name:",True,(255,255,255)),(200,200))
        name_input.draw(screen)

    elif state == "SETTINGS":
        btn_sound.draw(screen)
        btn_color.draw(screen)
        btn_back.draw(screen)

    elif state == "PLAY":
        all_sprites.update()

        distance += 1
        score += 1

        # collisions
        if pygame.sprite.spritecollideany(player, enemies):
            save_score(player_name, score, distance, settings["difficulty"])
            state = "MENU"

        hits = pygame.sprite.spritecollide(player, obstacles, True)
        for h in hits:
            if h.type == "oil":
                player.rect.x += random.choice([-50,50])
            elif h.type == "barrier":
                state = "MENU"
            elif h.type == "pothole":
                player.speed = max(2, player.speed - 2)

        hits = pygame.sprite.spritecollide(player, powerups, True)
        for p in hits:
            player.nitro = False
            player.shield = False

            if p.type == "Nitro":
                player.nitro = True
                player.speed = 10
                player.timer = pygame.time.get_ticks() + 4000

            elif p.type == "Shield":
                player.shield = True
                player.timer = pygame.time.get_ticks() + 4000

            elif p.type == "Repair":
                obstacles.empty()

        all_sprites.draw(screen)

        screen.blit(font.render(f"Score: {score}",True,(255,255,255)),(10,10))
        screen.blit(font.render(f"Dist: {distance}",True,(255,255,255)),(10,40))

    elif state == "BOARD":
        board = load_leaderboard()
        for i, e in enumerate(board):
            txt = f"{i+1}. {e['name']} | {e['score']} | {e['distance']}m | {e['difficulty']}"
            screen.blit(font.render(txt,True,(255,255,255)),(50,50+i*30))
        btn_back.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()