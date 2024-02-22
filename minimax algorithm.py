import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(position, maximizing_player, alpha, beta):
    if position.current_winner == 'X':
        return {'position': None, 'score': -1}
    elif position.current_winner == 'O':
        return {'position': None, 'score': 1}
    elif not position.empty_squares():
        return {'position': None, 'score': 0}

    if maximizing_player:
        max_eval = {'position': None, 'score': -math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, 'O')
            sim_score = minimax(position, False, alpha, beta)
            position.board[possible_move] = ' '
            position.current_winner = None
            sim_score['position'] = possible_move
            if sim_score['score'] > max_eval['score']:
                max_eval = sim_score
            alpha = max(alpha, sim_score['score'])
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = {'position': None, 'score': math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, 'X')
            sim_score = minimax(position, True, alpha, beta)
            position.board[possible_move] = ' '
            position.current_winner = None
            sim_score['position'] = possible_move
            if sim_score['score'] < min_eval['score']:
                min_eval = sim_score
            beta = min(beta, sim_score['score'])
            if beta <= alpha:
                break
        return min_eval

def play_game():
    t = TicTacToe()
    t.print_board_nums()
    while t.empty_squares():
        if t.num_empty_squares() % 2 == 0:
            move = int(input("Enter your move (0-8): "))
            t.make_move(move, 'X')
        else:
            best_move = minimax(t, True, -math.inf, math.inf)
            t.make_move(best_move['position'], 'O')
            print(f"Computer made move to square {best_move['position']}")
        t.print_board()
        print()
        if t.current_winner:
            if t.current_winner == 'X':
                print("You won!")
            else:
                print("Computer won!")
            break
    if not t.current_winner:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
