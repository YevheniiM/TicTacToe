class Node:
    def __init__(self, board, parent, left, right):
        self.board = board
        self.parent = parent
        self.left = left
        self.right = right

class GameTree:
    def __init__(self, board):
        self._root = board
