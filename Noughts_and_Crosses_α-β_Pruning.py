import math
import numpy as np
import copy

class NoughtsAndCrosses:
    """Represents the Noughts and Crosses game logic and state."""

    def __init__(self):
        self.EMPTY = ' '
        self.NOUGHT = 'O'
        self.CROSS = 'X'
        self.DRAW = 'DRAW'

        self.next_player = self.CROSS
        self.flip_player = {self.CROSS: self.NOUGHT, self.NOUGHT: self.CROSS}

        self.board = np.array([[self.EMPTY for _ in range(3)] for _ in range(3)])

    def valid_move(self, row, col):
        """Checks if a specific cell is empty."""
        return self.board[row, col] == self.EMPTY

    def move(self, row, col):
        """
        Returns a new game state after making a move.
        Deepcopy is used to ensure the original state remains unchanged.
        """
        if not self.valid_move(row, col):
            raise ValueError('Cell already taken!')

        new_state = copy.deepcopy(self)
        new_state.board[row,col] = self.next_player
        new_state.next_player = self.flip_player[self.next_player]
        return new_state

    def winner(self):
        """Checks the board for a winner or a draw."""

        # checks rows and columns
        for i in range(3):
            if np.all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != self.EMPTY:
                return self.board[i, 0]
            if np.all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != self.EMPTY:
                return self.board[0, i]

        # checks diagonals
        if self.board[0, 0] != self.EMPTY and self.board[0, 0] == self.board[1, 1] == self.board [2, 2]:
            return self.board[0, 0]
        if self.board[0, 2] != self.EMPTY and self.board[0, 2] == self.board[1, 1] == self.board [2, 0]:
            return self.board[0, 2]

        # checks for draw
        if not np.any(self.board == self.EMPTY):
            return self.DRAW

        return False

    def actions(self):
        """Returns a list of coordinate tuples (row, col) for all empty cells."""
        return [_ for _ in zip(np.nonzero(self.board == self.EMPTY)[0], np.nonzero(self.board == self.EMPTY)[1])]

class Minimax:
    """Implementation of the Minimax algorithm with Alpha-Beta pruning."""

    def next_move(self, state = NoughtsAndCrosses()):
        """Calls the get_value() method ta calculate the best possible move for the
        current player."""
        player = state.next_player
        best_action = None
        best_value = math.inf * -1

        for action in state.actions():
            new_state = state.move(action[0], action[1])
            # calls get_value to find the utility of this move
            action_value = self.get_value(new_state, player, get_min = True)

            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action

    def get_value(self, state, player, get_min, alpha = -math.inf, beta = math.inf):
        """
        Recursive function to calculate state utility using Alpha-Beta pruning.

        Alpha: Best score guaranteed for the Maximizer.
        Beta: Best score guaranteed for the Minimizer.
        """
        other_player = state.flip_player
        winner = state.winner()

        if winner == player:
            return 1
        if winner == other_player:
            return -1
        if winner == state.DRAW:
            return 0

        for action in state.actions():
            new_state = state.move(action[0], action[1])
            # calls itself recursively and switches the get_min attribute
            action_value = self.get_value(new_state, player, get_min = not get_min, alpha=alpha, beta=beta)

            # maximizing turn: updates alpha (lower bound)
            if not get_min and action_value > alpha:
                alpha = action_value

            # minimizing turn: updates beta (upper bound)
            if get_min and action_value < beta:
                beta = action_value

            # alpha-beta pruning: cuts the branch if alpha >= beta
            if alpha >= beta:
                return alpha if not get_min else beta

        return alpha if not get_min else beta