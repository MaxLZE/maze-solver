from cell import Cell
class Maze:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(r,c) for c in range(self.columns)] for r in range(self.rows)]
    def get_neighbours(self,cell):
        validneighbours = []
        r = cell.row
        c = cell.column
        neighbours = (r+1,c) , (r-1,c), (r,c-1), (r,c+1)
        for nr,nc in neighbours:
            if 0 <= nr < self.rows and 0 <= nc < self.columns:
                validneighbours.append(self.grid[nr][nc])
        return validneighbours
                    