import pygame
pygame.init()

# ===== WINDOW SETTINGS =====
Width = 1000
Height = 800
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

# ===== COLORS =====
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

color = Black  # текущий цвет

# ===== COLOR KEYS =====
keys = {
    pygame.K_0: White,
    pygame.K_1: Black,
    pygame.K_2: Red,
    pygame.K_3: Green,
    pygame.K_4: Blue,
}

# ===== MODES =====
mode = "draw"
start_pos = None
drawing = False
last_pos = None

# ===== CANVAS =====
canvas = pygame.Surface((Width, Height))
canvas.fill(White)

# слой для предпросмотра фигур
preview = pygame.Surface((Width, Height), pygame.SRCALPHA)

running = True

while running:

    preview.fill((0, 0, 0, 0))  # очистка preview

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ===== KEYBOARD =====
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                color = keys[event.key]

            if event.key == pygame.K_d:
                mode = "draw"

            if event.key == pygame.K_e:
                mode = "eraser"

            if event.key == pygame.K_r:
                mode = "rect"

            if event.key == pygame.K_o:
                mode = "circle"

            if event.key == pygame.K_s:
                mode = "square"

            if event.key == pygame.K_t:
                mode = "triangle_right"

            if event.key == pygame.K_y:
                mode = "triangle_eq"

            if event.key == pygame.K_h:
                mode = "rhombus"

            if event.key == pygame.K_c:
                canvas.fill(White)

        # ===== MOUSE DOWN =====
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            last_pos = start_pos

        # ===== MOUSE UP =====
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()

            # RECTANGLE
            if mode == "rect" and start_pos:
                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )
                pygame.draw.rect(canvas, color, rect, 2)

            # CIRCLE
            if mode == "circle" and start_pos:
                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0] - start_pos[0]),
                    abs(end_pos[1] - start_pos[1])
                )
                pygame.draw.ellipse(canvas, color, rect, 2)

            # SQUARE
            if mode == "square" and start_pos:
                size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
                pygame.draw.rect(canvas, color, rect, 2)

            # RIGHT TRIANGLE
            if mode == "triangle_right" and start_pos:
                points = [
                    start_pos,
                    (end_pos[0], start_pos[1]),
                    end_pos
                ]
                pygame.draw.polygon(canvas, color, points, 2)

            # EQUILATERAL TRIANGLE
            if mode == "triangle_eq" and start_pos:
                width = abs(end_pos[0] - start_pos[0])
                height = int(width * 0.866)
                points = [
                    (start_pos[0], start_pos[1] + height),
                    (start_pos[0] + width, start_pos[1] + height),
                    (start_pos[0] + width // 2, start_pos[1])
                ]
                pygame.draw.polygon(canvas, color, points, 2)

            # RHOMBUS
            if mode == "rhombus" and start_pos:
                cx = (start_pos[0] + end_pos[0]) // 2
                cy = (start_pos[1] + end_pos[1]) // 2
                points = [
                    (cx, start_pos[1]),
                    (end_pos[0], cy),
                    (cx, end_pos[1]),
                    (start_pos[0], cy)
                ]
                pygame.draw.polygon(canvas, color, points, 2)

            start_pos = None
            last_pos = None

    x, y = pygame.mouse.get_pos()

    # ===== DRAW / ERASER =====
    if drawing and mode in ["draw", "eraser"]:
        draw_color = White if mode == "eraser" else color
        if last_pos:
            pygame.draw.line(canvas, draw_color, last_pos, (x, y), 10)
        last_pos = (x, y)

    # ===== PREVIEW RECT =====
    if drawing and mode == "rect" and start_pos:
        rect = pygame.Rect(min(start_pos[0], x), min(start_pos[1], y),
                           abs(x - start_pos[0]), abs(y - start_pos[1]))
        pygame.draw.rect(preview, color, rect, 2)

    # ===== PREVIEW CIRCLE =====
    if drawing and mode == "circle" and start_pos:
        rect = pygame.Rect(min(start_pos[0], x), min(start_pos[1], y),
                           abs(x - start_pos[0]), abs(y - start_pos[1]))
        pygame.draw.ellipse(preview, color, rect, 2)

    # ===== PREVIEW SQUARE =====
    if drawing and mode == "square" and start_pos:
        size = min(abs(x - start_pos[0]), abs(y - start_pos[1]))
        rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
        pygame.draw.rect(preview, color, rect, 2)

    # ===== PREVIEW RIGHT TRIANGLE =====
    if drawing and mode == "triangle_right" and start_pos:
        points = [start_pos, (x, start_pos[1]), (x, y)]
        pygame.draw.polygon(preview, color, points, 2)

    # ===== PREVIEW EQUILATERAL TRIANGLE =====
    if drawing and mode == "triangle_eq" and start_pos:
        width = abs(x - start_pos[0])
        height = int(width * 0.866)
        points = [
            (start_pos[0], start_pos[1] + height),
            (start_pos[0] + width, start_pos[1] + height),
            (start_pos[0] + width // 2, start_pos[1])
        ]
        pygame.draw.polygon(preview, color, points, 2)

    # ===== PREVIEW RHOMBUS =====
    if drawing and mode == "rhombus" and start_pos:
        cx = (start_pos[0] + x) // 2
        cy = (start_pos[1] + y) // 2
        points = [
            (cx, start_pos[1]),
            (x, cy),
            (cx, y),
            (start_pos[0], cy)
        ]
        pygame.draw.polygon(preview, color, points, 2)

    # ===== RENDER =====
    screen.blit(canvas, (0, 0))
    screen.blit(preview, (0, 0))

    pygame.display.flip()
    clock.tick(144)

pygame.quit()

# ===== РЕЖИМЫ РИСОВАНИЯ =====
# D - обычная кисть (рисуешь как карандашом)
# E - ластик (рисует белым, стирает)
# R - прямоугольник
# O - круг (ellipse)
# S - квадрат
# T - прямоугольный треугольник
# Y - равносторонний треугольник
# H - ромб

# ===== ЦВЕТА =====
# 0 - белый
# 1 - чёрный
# 2 - красный
# 3 - зелёный
# 4 - синий