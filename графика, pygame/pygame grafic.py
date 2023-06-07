import pygame


def draw_cross(screen, a, b):
    pygame.display.set_caption('Крест')
    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, pygame.Color(225, 225, 255), [(0, 0), (a, b)], 5)
    pygame.draw.polygon(screen, pygame.Color("white"), [(0, b), (a, 0)], 5)


def draw_rectangle(screen, a, b):
    pygame.display.set_caption('Прямоугольник')
    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, pygame.Color("red"), [(10, 10), (a - 10, 10), (a - 10, b - 10), (10, b - 10)], 0)
    

'''
if __name__ == '__main__':
    a, b = list(map(float, input().split()))
    if a % 1 != 0 or b % 1 != 0 or a <= 0 or b <= 0:
        print('Неправильный формат ввода')
        exit()
    pygame.init()
    size = width, height = a, b
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        #draw_cross(screen, a, b)
        #draw_rectangle(screen, a, b)
        pygame.display.flip()
    pygame.quit()
'''

'''
def draw_chess(screen, a, n):
    pygame.display.set_caption('Шахматная доска')   
    n = int(n)
    a = int(a)
    c = a // n
    if n % 2 == 1:
        screen.fill((255, 255, 255))
        for i in range(0, a, c):
            for j in range(0, a, c):
                pygame.draw.rect(screen, (0, 0, 0), (a - i * 2, a - j * 2, c, c), 0)
                pygame.draw.rect(screen, (0, 0 ,0), (a - c - i * 2, a - c - j * 2, c, c), 0)
    else:
        screen.fill((0, 0, 0))
        for i in range(0, a, c):
            for j in range(0, a, c):
                pygame.draw.rect(screen, (255, 255, 255), (a - i * 2, a - j * 2, c, c), 0)
                pygame.draw.rect(screen, (255, 255, 255), (a - c - i * 2, a - c - j * 2, c, c), 0)
    


# для доски
if __name__ == '__main__':
    a, b = list(map(float, input().split()))
    if a % 1 != 0 or b % 1 != 0 or a <= 0 or b <= 0 or a % b != 0:
        print('Неправильный формат ввода')
        exit()
    pygame.init()
    size = width, height = a, a
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw_chess(screen, a, b)
        pygame.display.flip()
    pygame.quit()
'''

'''
def draw_target(screen, count, radius, width):
    color_dict = {0: pygame.Color('red'),
                  1: pygame.Color('blue'),
                  2: pygame.Color('green')}
    pygame.display.set_caption('Мишень') 
    screen.fill((0, 0, 0))
    for i in range(count):
        color = color_dict[i % 3]
        pygame.draw.circle(screen, 
                           color, 
                           (width // 2, width // 2), 
                           (width // 2) - i * radius, 
                           0)


if __name__ == '__main__':
    count, radius = input().split()
    if not count.isdigit() or not radius.isdigit() or int(count) < 0 or int(radius) < 0:
        print('Неправильный формат ввода')
        exit()
    count, radius = int(count), int(radius)
    pygame.init()
    size = width, height = count * radius * 2, count * radius * 2
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw_target(screen, count, radius, width)
        pygame.display.flip()
    pygame.quit()
'''


'''
def draw_sphere(screen, count):
    screen.fill((0, 0, 0))
    size = 300 // count
    for i in range(count // 2):
        pygame.draw.ellipse(screen, (255, 255, 255),(0, 0 + i * size, 300, 300 - i * 2 * size), 1)
        pygame.draw.ellipse(screen, (255, 255, 255),(0 + i * size, 0, 300 - i * 2 * size, 300), 1)


if __name__ == '__main__':
    count = input()
    if not count.isdigit() or int(count) < 0:
        print('Неправильный формат ввода')
        exit()
    count = int(count)
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw_sphere(screen, count)
        pygame.display.flip()
    pygame.quit()
'''



def draw_romb(screen, count):
    screen.fill(pygame.color('yellow'))


if __name__ == '__main__':
    count = input()
    if not count.isdigit() or int(count) < 0:
        print('Неправильный формат ввода')
        exit()
    count = int(count)
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw_romb(screen, count)
        pygame.display.flip()
    pygame.quit()






