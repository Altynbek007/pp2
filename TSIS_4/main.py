import pygame
import sys

from game import Game
from db import init_db, save_score, get_best

pygame.init()

screen = pygame.display.set_mode((600, 600))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

init_db()

state = "MENU"
username = ""
game = None
best = 0


def handle_menu_input(event):
    global username, state, game, best

    if event.key == pygame.K_RETURN:
        if username.strip() == "":
            username = "Player"

        game = Game()
        best = get_best(username)
        state = "PLAY"

    elif event.key == pygame.K_BACKSPACE:
        username = username[:-1]

    else:
        if event.unicode.isprintable() and len(username) < 12:
            username += event.unicode


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== MENU =====
        if state == "MENU":
            if event.type == pygame.KEYDOWN:
                handle_menu_input(event)

        # ===== PLAY =====
        elif state == "PLAY":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.direction = (0, -20)
                elif event.key == pygame.K_DOWN:
                    game.direction = (0, 20)
                elif event.key == pygame.K_LEFT:
                    game.direction = (-20, 0)
                elif event.key == pygame.K_RIGHT:
                    game.direction = (20, 0)

        # ===== GAMEOVER =====
        elif state == "GAMEOVER":
            if event.type == pygame.KEYDOWN:
                state = "MENU"
                username = ""

    # ===== LOGIC =====
    if state == "MENU":
        screen.blit(font.render("Enter name:", True, (255, 255, 255)), (200, 200))
        screen.blit(font.render(username, True, (255, 255, 255)), (200, 250))

    elif state == "PLAY":
        result = game.update()

        if result == "GAMEOVER":
            save_score(username, game.score, game.level)
            state = "GAMEOVER"

        game.draw(screen)

        screen.blit(font.render(f"Score: {game.score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Best: {best}", True, (255, 255, 0)), (10, 40))

    elif state == "GAMEOVER":
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (200, 250))
        screen.blit(font.render("Press any key", True, (255, 255, 255)), (200, 300))

    pygame.display.flip()
    clock.tick(game.speed if game else 10)