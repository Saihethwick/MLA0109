import heapq

class PuzzleState:
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __lt__(self, other):
        return (self.depth + self.h_cost()) < (other.depth + other.h_cost())

    def h_cost(self):
        return sum([1 if self.board[i] != self.goal_state[i] else 0 for i in range(8)])

    def possible_moves(self):
        moves = []
        index = self.board.index(0)
        if index not in [0, 1, 2]:
            moves.append(-3)  # Up
        if index not in [0, 3, 6]:
            moves.append(-1)  # Left
        if index not in [2, 5, 8]:
            moves.append(1)   # Right
        if index not in [6, 7, 8]:
            moves.append(3)   # Down
        return moves

    def generate_child(self, move):
        new_board = self.board[:]
        index = new_board.index(0)
        new_index = index + move
        new_board[index], new_board[new_index] = new_board[new_index], new_board[index]
        return PuzzleState(new_board, parent=self, move=move)

    def is_goal(self):
        return self.board == self.goal_state

    def print_path(self):
        if self.parent:
            self.parent.print_path()
        print(self)
        print()

    def __str__(self):
        return '\n'.join([str(self.board[i:i+3]) for i in range(0, 9, 3)])

def solve_puzzle(initial_state):
    open_list = []
    heapq.heappush(open_list, initial_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state.is_goal():
            current_state.print_path()
            print("Solution found in", current_state.depth, "moves.")
            break

        closed_set.add(current_state)
        for move in current_state.possible_moves():
            child = current_state.generate_child(move)
            if child in closed_set:
                continue
            if child not in open_list:
                heapq.heappush(open_list, child)

# Example usage:
initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
initial_state = PuzzleState(initial_board)
solve_puzzle(initial_state)
