class TictacToe
 def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_winner = None  # Keep track of the winner!

def print_board(self):
        # This is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')