import pygame
from player import play_track, stop_track, next_track, previous_track, get_track_name

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

clock = pygame.time.Clock()
done = False

while not done:
    screen.fill((30, 30, 30))

    # текст
    title = font.render("Music Player", True, (255, 255, 255))
    track_text = small_font.render(get_track_name(), True, (255, 255, 255))
    controls_text = small_font.render("P-play  S-stop  N-next  B-back  Q-quit", True, (200, 200, 200))

    screen.blit(title, (250, 50))
    screen.blit(track_text, (50, 120))
    screen.blit(controls_text, (50, 180))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_track()

            elif event.key == pygame.K_s:
                stop_track()

            elif event.key == pygame.K_n:
                next_track()

            elif event.key == pygame.K_b:
                previous_track()

            elif event.key == pygame.K_q:
                done = True

    clock.tick(60)

pygame.quit()