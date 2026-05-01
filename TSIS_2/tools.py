import pygame
def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]
    while stack:
        px, py = stack.pop()

        if 0 <= px < width and 0 <= py < height:
            if surface.get_at((px, py)) == target_color:
                surface.set_at((px, py), new_color)

                stack.append((px + 1, py))
                stack.append((px - 1, py))
                stack.append((px, py + 1))
                stack.append((px, py - 1))

def draw_line(surface, color, start_pos, end_pos, width):
    pygame.draw.line(surface, color, start_pos, end_pos, width)


def draw_rect(surface, color, start_pos, end_pos, width):
    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
    pygame.draw.rect(surface, color, rect, width)


def draw_circle(surface, color, start_pos, end_pos, width):
    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
    pygame.draw.circle(surface, color, start_pos, radius, width)


def draw_square(surface, color, start_pos, end_pos, width):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    size = min(abs(dx), abs(dy))
    rect = pygame.Rect(start_pos, (size, size))
    pygame.draw.rect(surface, color, rect, width)


def draw_pencil(surface, color, last_pos, current_pos, width):
    if last_pos:
        pygame.draw.line(surface, color, last_pos, current_pos, width)