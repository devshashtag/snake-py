import random
import cv2


class Food(object):
    def __init__(self, board_limit, step_size):
        # initialize Food :
        self.board_limit = board_limit

        # size of food(set grid game)
        self.step_size = step_size
        # initial location
        self.pos = (self.step_size - 1, self.step_size - 1)
        # - set random x, y position
        self.randomize()

    def draw(self, board, is_clear=False, color=0):
        # - draw food in board
        if is_clear:
            # Note: before change location food . food must be clear
            # clear food with back groud board color
            cv2.circle(board, self.pos, self.step_size // 2, color, -1)
        else:
            # check color is 0 change it
            if not color:
                color = 180
            # draw food
            cv2.circle(board, self.pos, self.step_size // 2, color, -1)

        # show board after draw circles
        cv2.imshow('Micro Robot: AI Snake Q Learning', board)

    def randomize(self):
        # generate random location for food
        self.pos = (random.randint(self.board_limit[0][0] + self.step_size,
                                   self.board_limit[1][0] - self.step_size),
                    random.randint(self.board_limit[0][0] + self.step_size,
                                   self.board_limit[1][0] - self.step_size))
