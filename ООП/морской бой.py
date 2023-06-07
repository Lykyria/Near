class SeaMap:
    def __init__(self):
        self.map = [['.' for i in range(10)] for j in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        else:
            self.shoot(row, col, 'hit')
            ship = set()
            for i in range(row, row+4):
                if cell_in_map(i, col):
                    if self.map[i][col] == 'x':
                        ship.add((i, col))
                    else:
                        break
            for i in range(row, row-4, -1):
                if cell_in_map(i, col):
                    if self.map[i][col] == 'x':
                        ship.add((i, col))
                    else:
                        break
            for i in range(col, col+4):
                if cell_in_map(row, i):
                    if self.map[row][i] == 'x':
                        ship.add((row, i))
                    else:
                        break
            for i in range(col, col-4, -1):
                if cell_in_map(row, i):
                    if self.map[row][i] == 'x':
                        ship.add((row, i))
                    else:
                        break
            neighboard = set()
            for point in ship:
                row = point[0]
                col = point[1]
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        if cell_in_map(i, j):
                            neighboard.add((i, j))
            neighboard -= ship

            for point in neighboard:
                self.shoot(*point, 'miss')

    def cell(self, row, col):
        return self.map[row][col]


def cell_in_map(row, col):
    if 0 <= row < 10 and 0 <= col < 10:
        return True
    return False


sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(4, 4, 'miss')
sm.shoot(9, 8, 'hit')
sm.shoot(9, 9, 'sink')
for i in range(10):
    for j in range(10):
        print(sm.cell(i, j), end=' ')
    print()