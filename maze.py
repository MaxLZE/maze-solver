from cell import Cell
class Maze:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(r,c) for c in range(self.columns)] for r in range(self.rows)]
        