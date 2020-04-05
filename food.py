import random


class Food(object):
    """ make Food """

    def __init__(self, board):
        # board
        self.board = board

        # location
        self.position = (0, 0)

    def randomize(self):
        # hide
        self.draw(False)

        # find new free location
        self.position = random.choice(self.board.free())

        # show
        self.draw(True)

    def draw(self, is_draw):
        # show / hide by is_draw
        self.board.draw(self.position, is_draw)
