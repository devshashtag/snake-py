import numpy as np
import cv2

class Board(object):
    """Board or window or page game"""

    def __init__(self, size_board=(500, 500), bg_color=0):
            # initialize board :
            self.size_board = size_board
            self.bg_color = bg_color
            # - create board list (numpy zeros)
            self.board =np.zeros(self.size_board , np.uint8)
            # - set back groud color board
            self.board[:] = self.bg_color
            
