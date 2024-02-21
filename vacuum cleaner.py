class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def clean_cell(self, x, y):
        if self.is_valid_move(x, y):
            self.grid[x][y] = "clean"
            print(f"Cleaned cell ({x}, {y})")
        else:
            print(f"Invalid cell ({x}, {y})")

    def move(self, x, y):
        if self.is_valid_move(x, y):
            print(f"Moving to cell ({x}, {y})")
        else:
            print(f"Invalid move to cell ({x}, {y})")

    def clean_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "dirty":
                    self.clean_cell(i, j)
                self.visited.add((i, j))
                for dx, dy in self.moves:
                    new_x, new_y = i + dx, j + dy
                    if (new_x, new_y) not in self.visited and self.is_valid_move(new_x, new_y):
                        self.move(new_x, new_y)
                        self.visited.add((new_x, new_y))

# Example usage:
grid = [["dirty", "clean", "dirty"],
        ["clean", "dirty", "clean"],
        ["dirty", "clean", "dirty"]]
vacuum = VacuumCleaner(grid)
vacuum.clean_grid()
