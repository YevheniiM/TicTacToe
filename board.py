import numpy as np


class Move:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y


class Board:
    def __init__(self, board):
        """

        :param board: list(list) - actual board
        :param last: Move - the last move

        """
        self.board = board
        self.last_move = Move(None, -1, -1)

    def check_game_status(self):
        def _check_rows(board):
            for row in board:
                if len(set(row)) == 1:
                    return row[0]
            return 0

        def _check_diagonals(board):
            if len(set([board[i][i] for i in range(len(board))])) == 1:
                return board[0][0]
            if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
                return board[0][len(board) - 1]
            return 0

        # transposition to check rows, then columns
        for newBoard in [self.board, np.transpose(self.board)]:
            result = _check_rows(newBoard)
            if result:
                return result
        if _check_diagonals(self.board):
            return _check_diagonals(self.board)
        return self._check_full()

    def _check_full(self):
        for i in self.board:
            for j in i:
                if j == ' ':
                    return False
        return True

    def move(self, move):
        if self.board[move.x][move.y] == ' ':
            self.last_move = move

    def __str__(self):
        s = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                s += self.board[i][j]
            s += '\n'
        return s
