import numpy as np


class Sudoku:
    def __init__(self, grid):
        super().__init__()
        self.grid = grid

    def possible(self, x , y, n):
        for i in range(9):
            if self.grid[x][i] == n:
                return False
        for i in range(9):
            if self.grid[i][y] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[x0 + i][y0 + j] == n:
                    return False
        return True

    def solve(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[x][y] = n
                            self.solve()
                            self.grid[x][y] = 0
                    return
        print(np.matrix(self.grid))
        input("More?")


if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],  
            [5, 2, 0, 0, 0, 0, 0, 0, 0],  
            [0, 8, 7, 0, 0, 0, 0, 3, 1],  
            [0, 0, 3, 0, 1, 0, 0, 8, 0],  
            [9, 0, 0, 8, 6, 3, 0, 0, 5],  
            [0, 5, 0, 0, 9, 0, 6, 0, 0],  
            [1, 3, 0, 0, 0, 0, 2, 5, 0],  
            [0, 0, 0, 0, 0, 0, 0, 7, 4],  
            [0, 0, 5, 2, 0, 6, 3, 0, 0]];
    sudoku = Sudoku(grid)
    sudoku.solve()
