import numpy as np


class Board(object):
    """Board or window or page game"""

    def __init__(self, size_board=(800, 600), bg_color=0):
        # initialize attribute board :
        self.size_board = size_board
        self.bg_color = bg_color

        # - create board list (numpy zeros)
        # reverse arr for numpy
        self.board = np.zeros(self.size_board[::-1], np.uint8)

        # - set back groud color board
        self.board[:] = self.bg_color
