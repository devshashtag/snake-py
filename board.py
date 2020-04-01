import numpy as np
import cv2

class Board(object):
    """window or page or board game"""

    def __init__(self, size=[(0, 0), (80, 60)], title='Simple Snake', bg=0, fg=255):
        # board size
        self.size = size
        # board title
        self.title = title
        # background color
        self.bg = bg
        # forground color
        self.fg = fg
        # - create board array(numpy zeros)
        # reverse board size for numpy arr (80, 60) => (60, 80)
        self.board = np.zeros(self.size[1][::-1], np.uint8)
        # background set
        self.clear()


    # clear board with background
    def clear(self):
        # - Clear all items with bg
        self.board[:] = self.bg

    # show board with title (scale x)
    def show(self, scale=10):
        x, y  = self.size[1]

        # show board
        cv2.namedWindow(self.title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.title, x*scale, y*scale)
        cv2.imshow(self.title, self.board)


    # draw a point in board
    def draw(self, positions, color):
        if type(positions) == list:
            for position in positions:
                cv2.circle(self.board, tuple(position), 0, color, 1)
        else:
            position = positions
            cv2.circle(self.board, tuple(position), 0, color, 1)

    # return free sections in board
    def freeSections(self):
        return list(zip(*np.where(self.board == self.bg)[::-1]))
