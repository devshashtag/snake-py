import numpy as np
import cv2

class Board(object):
    """window or page or board game"""

    def __init__(self, size_window=(800, 600), title='Simple Snake', bg_color=0):
        # initialize attribute board :
        self.size_window = size_window
        self.bg_color = bg_color
        self.title = title
        # - create window array(numpy zeros)
        # reverse window size for numpy arr (800 , 600) => (600 , 800)
        self.window = np.zeros(self.size_window[::-1], np.uint8)
        # background set
        self.clear_window()

    # clear window with background
    def clear_window(self):
        # - Clear all items with bg_color
        self.window[:] = self.bg_color

    # show window with title (scale 10x)
    def draw_window(self):
        x, y  = self.size_window

        # show window
        cv2.namedWindow(self.title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.title, x*10, y*10)
        cv2.imshow(self.title, self.window)

    # get keys from window
    def get_key(self, delay):
        # read key entered and sleep for fps
        return chr(cv2.waitKey(delay) & 0xFF)
