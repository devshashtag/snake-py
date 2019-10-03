import cv2
import random


class Food(object):
    """ food """

    def __init__(self, window_limit, step_size):
        # initialize Food :
        self.window_limit = window_limit

        # size of food(set grid game)
        self.step_size = step_size
        # initial location
        self.pos = (self.step_size - 1, self.step_size - 1)
        # - set random x, y position
        self.randomize()

    def draw(self, window, is_clear=False, color=0):
        # - draw food in window
        if is_clear:
            # Note: before change location food . food must be clear
            # clear food with backgroud window
            cv2.circle(window, self.pos, self.step_size//2, color, -1)
        else:
            # check color is 0 change it
            if color == 0:
                color = 180
            # draw food
            cv2.circle(window, self.pos, self.step_size//2, color, -1)

    def randomize(self):
        # location of window
        window_x = self.window_limit[0][0] + self.step_size
        window_y = self.window_limit[0][1] + self.step_size
        window_width = self.window_limit[1][0] - self.step_size
        window_height = self.window_limit[1][1] - self.step_size
        # generate random location and free location in window
        food_loc_x = random.randint(window_x, window_width)
        food_loc_y = random.randint(window_y, window_height)
        # location of food
        self.pos = (food_loc_x, food_loc_y)
        # print locations
        print(window_x, window_y)
        print(window_width, window_height)
        print(self.pos)
        offset=(self.step_size + (self.step_size//2))
        if(self.pos[0] % offset != 0 and
           self.pos[1] % offset != 0 ):
           self.randomize()
