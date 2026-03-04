class Cell:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.top = True
        self.bottom = True
        self.left = True
        self.right = True
        self.visited = False
        