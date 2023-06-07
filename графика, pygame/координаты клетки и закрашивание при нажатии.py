import pygame


# клетчатое поле
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # создаёт поле
    def render(self, screen):
        for row in range(self.width):
            for col in range(self.height):
                if self.board[col][row] == 0:
                    width = 1
                elif self.board[col][row] == 1:
                    width = 0
                pos_w = self.left + row * self.cell_size
                pos_h = self.top + col * self.cell_size
                color = WHITE
                pygame.draw.rect(screen, color, (pos_w, pos_h, self.cell_size, self.cell_size), width)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[1] < self.top \
                or mouse_pos[0] > self.left + self.width * self.cell_size \
                or mouse_pos[1] > self.top + self.height * self.cell_size:
            return None
        x = (mouse_pos[0] - self.left + self.cell_size) // self.cell_size
        y = (mouse_pos[1] - self.top + self.cell_size) // self.cell_size
        return [x, y]
    '''
        pos_w = self.left + self.cell_size * self.width
        pos_h = self.top + self.cell_size * self.height
        if self.left < mouse_pos[0] < pos_w and self.top < mouse_pos[1] < pos_h:
            pos_w_new = pos_w - mouse_pos[0]
            pos_h_new = pos_h - mouse_pos[1]
           '''

        

    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[y - 1][x - 1] = int(not self.board[y - 1][x - 1])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        self.on_click(cell)


if __name__ == '__main__': 
    size = width, height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    pygame.display.set_caption('Board')
    WHITE = (255, 255, 255)
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_cell(event.pos))
                board.get_click(event.pos)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
    