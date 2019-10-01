import cv2
import random
from food import Food


class Snake(object):
    """ Snake """

    def __init__(self, window_limit, head_position=(0, 0), window_bg_color=0,
                 start_length=10, first_direction='6', step_size=12,
                 speed=100):
        # initialize attribute snake:
        self.window_limit = window_limit
        self.start_length = start_length
        self.window_bg_color = window_bg_color
        self.length = 0
        self.directions = list("2468")
        # size of each part
        self.step_size = step_size
        # speed snake
        self.speed = speed
        # controller head '6' = right
        self.direction = first_direction
        # initialize head
        self.positions = [head_position]
        # food
        self.food = Food(self.window_limit, self.step_size)

    # eat food by snake
    def eat_food(self, food):
        # - remove food

        # - stretch body
        # - add score
        # - new food
        pass

    # add length snake
    def add_length(self):
        # add snake body
        # add a new length at last tail
        new_position = self.positions[self.length]
        self.positions.append(new_position)
        self.length += 1

    # darw snake in window
    def draw(self, window, is_clear=False, clear_color=0):
        # - draw the snake with cv2
        if is_clear:
            # Note: after clear snake draw again snake
            # change clearn color to bg color
            if clear_color == 0:
                clear_color = self.window_bg_color
            # find last tail position
            last_tail = self.positions[self.length]
            # clear last position
            cv2.circle(window, last_tail, self.step_size // 2, clear_color, -1)
        else:
            for pos in self.positions:
                # print color snake random
                # color = random.randint(200, 250)
                # static color
                color = 250
                # head color
                if pos == self.positions[0]:
                    color = 180
                cv2.circle(window, tuple(pos), self.step_size // 2, color, -1)

        # show window after draw circles(body and head snake)
        cv2.imshow('Micro Robot: Snake', window)
        # draw food
        self.food.draw(window)

    # move snake in window
    def move(self):
        # - move up down left right with keys (with 2,4,6,8 and arrows)
        # unpack head locations for update
        x, y = self.positions[0]

        # detect key and move head snake
        if(self.direction == '8'):  # move up
            y -= self.step_size
        elif(self.direction == '2'):  # move down
            y += self.step_size
        elif(self.direction == '4'):  # move left
            x -= self.step_size
        elif(self.direction == '6'):  # move right
            x += self.step_size

        # new location of head but not save in self.positions
        head_new_position = (x, y)

        # - limit movement inside window(game) false is limited movement
        limit_check = self.dot_in_rectangle(
            self.window_limit, head_new_position)

        # collision detection body snake with head snake and window:
        # - self.positions : old locations of snake
        # - head_new_position : new location head snake at now
        # if head_new_position not in self.positions > update locations
        if head_new_position not in self.positions and limit_check:
            # body mover( delete last tail[shift all locations to new locations])
            del self.positions[-1:]
            # add new location of head to shited locations
            self.positions.insert(0, head_new_position)
        else:
            # just a log ...
            print("\033[31m u died \033[m")

    # limit checker for movment snake (window)
    def dot_in_rectangle(self, rectangle, pos):
        if rectangle[0][0] < pos[0] and rectangle[0][1] < pos[1] and \
           rectangle[1][0] > pos[0] and rectangle[1][1] > pos[1]:
            return True
        else:
            return False
