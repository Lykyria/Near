import pygame


def draw(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (2, 27, 189))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 162, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()





