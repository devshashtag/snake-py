import numpy as np
import cv2

class Board(object):
    """window or page or board game"""

    def __init__(self, size_window=(800, 600), title='Micro Robot: Snake', bg_color=0):
        # initialize attribute board :
        self.size_window = size_window
        self.bg_color = bg_color
        self.title = title
        # - create window array(numpy zeros)
        # reverse window size for numpy arr
        self.window = np.zeros(self.size_window[::-1], np.uint8)
        # background set
        self.clear_window()

    # clear window with background
    def clear_window(self):
        # - Clear all items with bg_color
        self.window[:] = self.bg_color

    # show window with title
    def draw_window(self):
        # show window
        cv2.imshow(self.title, self.window)

    # get keys from window
    def get_key(self, delay):
        # read key entered and sleep for fps
        return chr(cv2.waitKey(delay) & 0xFF)
