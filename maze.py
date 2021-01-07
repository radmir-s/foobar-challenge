def solution(map):
    h = len(map)
    w = len(map[0])

    class cell:
        def __init__(self, wall, x, y):
            self.coord = x, y
            self.x = x
            self.y = y
            self.wall = bool(wall)
            self.walked = None
            self.left = None

        def __str__(self):
            return "wall" if self.wall else "({},{})".format(self.walked, self.left)

        def neigh(self):
            neigh_cells = []
            for i in (-1, 1):
                if 0 <= self.x + i < h:
                    if not board[self.x + i][self.y].wall:
                        neigh_cells.append(board[self.x + i][self.y])
                if 0 <= self.y + i < w:
                    if not board[self.x][self.y + i].wall:
                        neigh_cells.append(board[self.x][self.y + i])
            return neigh_cells

        def spread_walk(self):
            if not self.wall and self.walked:
                next_cells = [cell for cell in self.neigh() if not cell.walked]
                for cell in next_cells:
                    cell.walked = self.walked + 1
            return next_cells

        def spread_left(self):
            if not self.wall and self.left:
                next_cells = [cell for cell in self.neigh() if not cell.left]
                for cell in next_cells:
                    cell.left = self.left + 1
            return next_cells

    board = []
    for x, row in enumerate(map):
        Row = []
        for y, Cell in enumerate(row):
            Row.append(cell(Cell, x, y))
        board.append(Row)

    board[h - 1][w - 1].walked = 1
    just_walked_cells = [board[h - 1][w - 1]]

    board[0][0].left = 1
    just_left_cells = [board[0][0]]

    while True:
        next_cells = []
        for cell in just_walked_cells:
            next_cells += cell.spread_walk()
        just_walked_cells = next_cells
        if not next_cells:
            break

    while True:
        next_cells = []
        for cell in just_left_cells:
            next_cells += cell.spread_left()
        just_left_cells = next_cells
        if not next_cells:
            break

    walls = [board[i][j] for i in range(h) for j in range(w) if board[i][j].wall]

    optimals = []

    for cell in walls:
        walks = [c.walked for c in cell.neigh() if c.walked]
        lefts = [c.left for c in cell.neigh() if c.left]
        w_plus_l = [x + y + 1 for x in walks for y in lefts]
        optimals.append(None if not w_plus_l else min(w_plus_l))

    optimals.append(board[0][0].walked)
    optimals = [opt for opt in optimals if opt]
    return None if not optimals else min(optimals)
