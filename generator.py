from maze import Maze
from cell import Cell
import random

class Generator:
    def __init__(self, maze):
        self.maze = maze

    def backtrack(self, cell):
        stack = []
        stack.append(cell)
        cell.visited = True
        while len(stack) > 0:
            current = stack.pop()
            neighbours = self.maze.get_neighbours(current)
            unvisited = []
            for neighbour in neighbours:
                if neighbour.visited == False:
                    unvisited.append(neighbour)
            if len(unvisited) == 0:
                continue
            next_cell = random.choice(unvisited)
            if next_cell.row > current.row:
                current.bottom = False
                next_cell.top = False
            elif next_cell.row < current.row:
                current.top = False
                next_cell.bottom = False
            elif next_cell.column > current.column:
                current.right = False
                next_cell.left = False
            elif next_cell.column < current.column:
                current.left = False
                next_cell.right = False
            stack.append(current)
            next_cell.visited = True
            stack.append(next_cell)

        