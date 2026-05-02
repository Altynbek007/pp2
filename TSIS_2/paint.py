import pygame
import datetime
from tools import*

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

color = (255, 0, 0)
brush_size = 5
mode = "draw"

drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont(None, 32)
text_mode = False
text_input = ""
text_pos = (0, 0)

screen.fill(WHITE)
base_layer = screen.copy()

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # r - red, g - green, b - blue, q - qara(black)
            if event.key == pygame.K_r:
                color = (255, 0, 0)
                print("COLOR CHANGED TO RED")
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
                print("COLOR CHANGED TO GREEN")
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
                print("COLOR CHANGED TO BLUE")
            elif event.key == pygame.K_q:
                color = (0, 0, 0)
                print("COLOR CHANGED TO QARA")

            elif event.key == pygame.K_1:
                brush_size = 2
                print("BRUSH SIZE CHANGED TO 2")
            elif event.key == pygame.K_2:
                brush_size = 5
                print("BRUSH SIZE CHANGED TO 5")
            elif event.key == pygame.K_3:
                brush_size = 10
                print("BRUSH SIZE CHANGED TO 10")
            #d - draw, l - line, p - rect, c - circle, s - save / square, t - text, f - fill, e - erase

            elif event.key == pygame.K_d:
                mode = "draw"
                print("MODE CHANGED TO DRAW")
            elif event.key == pygame.K_l:
                mode = "line"
                print("MODE CHANGED TO LINE")
            elif event.key == pygame.K_p:
                mode = "rect"
                print("MODE CHANGED TO RECT")
            elif event.key == pygame.K_c:
                mode = "circle"
                print("MODE CHANGED TO CIRCLE")
            elif event.key == pygame.K_s:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    filename = datetime.datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                    pygame.image.save(screen, filename)
                    print("Saved:", filename)
                else:
                    mode = "square"
                    print("MODE CHANGED TO SQUARE")
            elif event.key == pygame.K_t:
                mode = "text"
                print("MODE CHANGED TO TEXT")
            elif event.key == pygame.K_f:
                mode = "fill"
                print("MODE CHANGED TO FILL")
            elif event.key == pygame.K_e:
                mode = "erase"
                print("MODE CHANGED TO ERASE")

            if text_mode:
                if event.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    screen.blit(img, text_pos)
                    text_mode = False

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            base_layer = screen.copy()

            if mode == "fill":
                flood_fill(screen, event.pos[0], event.pos[1], color)

            if mode == "text":
                text_mode = True
                text_pos = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
            end_pos = event.pos

            if mode == "line":
                draw_line(screen, color, start_pos, end_pos, brush_size)

            elif mode == "rect":
                draw_rect(screen, color, start_pos, end_pos, brush_size)

            elif mode == "circle":
                draw_circle(screen, color, start_pos, end_pos, brush_size)

            elif mode == "square":
                draw_square(screen, color, start_pos, end_pos, brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:

            if mode == "draw":
                draw_pencil(screen, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

            elif mode == "erase":
                draw_pencil(screen, WHITE, last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

            elif mode in ["line", "rect", "circle", "square"]:
                screen.blit(base_layer, (0, 0))

                if mode == "line":
                    draw_line(screen, color, start_pos, event.pos, brush_size)

                elif mode == "rect":
                    draw_rect(screen, color, start_pos, event.pos, brush_size)

                elif mode == "circle":
                    draw_circle(screen, color, start_pos, event.pos, brush_size)

                elif mode == "square":
                    draw_square(screen, color, start_pos, event.pos, brush_size)

    if text_mode:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ================= CONTROLS =================

# COLORS:
# R - red
# G - green
# B - blue
# Q - black

# BRUSH SIZE:
# 1 - small (2 px)
# 2 - medium (5 px)
# 3 - large (10 px)

# MODES:
# D - draw (freehand)
# L - line
# P - rectangle
# C - circle
# S - square
# E - eraser
# F - fill (bucket)
# T - text mode

# SAVE:
# CTRL + S - save image

# TEXT MODE:
# ENTER - place text
# BACKSPACE - delete symbol
# ESC - cancel text input