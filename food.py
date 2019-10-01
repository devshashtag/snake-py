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
        cv2.imshow('Micro Robot: Snake', board)

    def randomize(self):
        # location of board
        board_x = self.board_limit[0][0] + self.step_size
        board_y = self.board_limit[0][1] + self.step_size
        board_width = self.board_limit[1][0] - self.step_size
        board_height = self.board_limit[1][1] - self.step_size
        # generate random location and free location in board
        food_loc_x = random.randint(board_x, board_width)
        food_loc_y = random.randint(board_y, board_height)
        # location of food
        self.pos = (food_loc_x, food_loc_y)
        # print locations
        print(board_x, board_y)
        print(board_width, board_height)
        print(self.pos)
