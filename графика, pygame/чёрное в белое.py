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
        pygame.draw.rect(screen, 
                         WHITE, 
                         (self.left, self.top, 
                          self.cell_size * self.width + 1, 
                          self.cell_size * self.height + 1), 
                          0)
        for row in range(self.width):
            for col in range(self.height):
                pos_w = self.left + 1 + row * self.cell_size
                pos_h = self.top + 1 + col * self.cell_size
                #color_cell  = WHITE
                if self.board[col][row] == 0:
                    color_cell = BLACK             
                else:
                    color_cell = WHITE
                pygame.draw.rect(screen, 
                                 color_cell, 
                                 (pos_w, pos_h, 
                                  self.cell_size - 1, 
                                  self.cell_size - 1), 0)
                
        

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[1] < self.top \
                or mouse_pos[0] > self.left + self.width * self.cell_size \
                or mouse_pos[1] > self.top + self.height * self.cell_size:
            return None
        x = (mouse_pos[0] - self.left + self.cell_size) // self.cell_size
        y = (mouse_pos[1] - self.top + self.cell_size) // self.cell_size
        return [x, y]
 
        

    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[y - 1][x - 1] = int(not self.board[y - 1][x - 1])
        board.fill_row_col(cell_coords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        self.on_click(cell)

    def fill_row_col(self, point):
        x = point[0] - 1
        y = point[1] - 1
        for i in range(self.height):
            self.board[i][x] = int(not self.board[i][x])
        for j in range(self.width):
            self.board[y][j] = int(not self.board[y][j])


if __name__ == '__main__':
    size = width, height = 800, 600
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    pygame.display.set_caption('Board')
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    board = Board(5, 7)
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
    