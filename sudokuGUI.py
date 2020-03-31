import pygame
import sys
from pygame.locals import *
import time





WINDOWHEIGHT = 450
WINDOWWIDTH = 450
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
box_size = 450 // 3
cell_size = box_size // 3


circle = pygame.Surface([20*2]*2, SRCALPHA, 32)
# circle = circle.convert_alpha()

def drawGrid():
    

    for x in range(0, WINDOWWIDTH, cell_size):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, GRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, cell_size):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, GRAY, (0, y), (WINDOWWIDTH, y))

    for x in range(0, WINDOWWIDTH, box_size):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, box_size):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    
    return None


def displayValue(cellData, x, y):
    x = (x + 0.5) * cell_size
    y = (y + 0.5) * cell_size
    cellSurf = BASICFONT.render('%s' % (cellData), True, GRAY)
    cellRect = cellSurf.get_rect()
    cellRect.center = (y, x)    
    DISPLAYSURF.blit(cellSurf, cellRect)
    pygame.display.update()

def populateCells(grid):
    DISPLAYSURF.fill(WHITE)
    drawGrid()
    for i in range(9):
        for j in range(9):
            displayValue(grid[i][j], i, j)
    


class Sudoku:
    def __init__(self, grid):
        super().__init__()
        self.grid = grid

    def possible(self, x, y, n):
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
                            populateCells(self.grid)
                            time.sleep(0.05)
                            self.solve()
                            self.grid[x][y] = 0
                    return
        # print(np.matrix(self.grid))
        # populateCells(self.grid)
        # input("More?")


def main():
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
    DISPLAYSURF.fill(WHITE)
    drawGrid()
    pygame.display.set_caption('Sudoku Solver')
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    sudoku = Sudoku(grid)
    sudoku.solve()
    
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS*5)

if __name__ == "__main__":
    main()



