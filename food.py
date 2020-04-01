import random


class Food(object):
    """ make Food """

    def __init__(self):
        # initial location
        self.position = (0, 0)

    def randomize(self, board):
        # remove food
        board.draw(self.position, board.bg)
        # find new free location
        self.position = random.choice(board.freeSections())
        # show into new location
        board.draw(self.position, 111)
