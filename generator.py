from maze import Maze
from cell import Cell
import random
class Generator:
    def __init__(self,maze):
        self.maze = maze
    def backtrack(self,cell):
        cell.visited = True
        neighbours = self.maze.get_neighbours(cell)
        unvisited = []
        for neighbour in neighbours: 
            if neighbour.visited == False:
                unvisited.append(neighbour)
        if len(unvisited) == 0:
            return
        next_cell = random.choice(unvisited)
        if next_cell.row > cell.row :
            cell.bottom = False
            next_cell.top= False
        elif next_cell.row < cell.row : 
            cell.top = False
            next_cell.bottom = False
        elif next_cell.column > cell.column:
            cell.right = False
            next_cell.left = False
        elif next_cell.column < cell.column:
            cell.left = False
            next_cell.right = False
        self.backtrack(next_cell)

        