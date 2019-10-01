import numpy as np


class Window(object):
    """window or page or board game"""

    def __init__(self, size_window=(800, 600), bg_color=0):
        # initialize attribute board :
        self.size_window = size_window
        self.bg_color = bg_color

        # - create window array(numpy zeros)
        # reverse window size for numpy arr
        self.window = np.zeros(self.size_window[::-1], np.uint8)

        # - change color backgroud to bg_color
        self.window[:] = self.bg_color
