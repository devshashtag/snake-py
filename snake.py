import cv2
import random


class Snake(object):
    def __init__(self, board_limit, head_position=(0, 0), start_length=150,
                 first_direction='6', step_size=10, speed=100):
        # initialize attribute snake:
        self.board_limit = board_limit
        self.start_length = start_length
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

    def eat_food(self, food):
        # - remove food
        # - stretch body
        # - add score
        # - new food
        pass

    def add_length(self):
        # add snake body
        new_position = self.positions[self.length]
        self.positions.append(new_position)
        self.length += 1

    def draw(self, board, is_clear=False, color=0):
        # - draw the snake with cv2
        if is_clear:
            # Note: after clear snake draw again snake
            # find last tail position
            last_tail = self.positions[self.length]
            # clear last position
            cv2.circle(board, last_tail, self.step_size // 2, color, -1)
        else:
            for pos in self.positions:
                # print color snake random
                # color = random.randint(150, 250)
                # static color
                color = 255

                # head color
                if pos == self.positions[0]:
                    color = 80

                cv2.circle(board, tuple(pos), self.step_size // 2, color, -1)

        # show board after draw circles
        cv2.imshow('Micro Robot: AI Snake Q Learning', board)

    def move(self):
        # - move up down left right with keys (with 2,4,6,8 and arrows)
        # copy all positions
        positions_copy = self.positions.copy()

        # body mover( shift all location to next state)
        del self.positions[self.length]

        # head mover
        x, y = self.positions[0]

        # detect key and move head snake
        if(self.direction == '8'):
            y -= self.step_size
        elif(self.direction == '2'):
            y += self.step_size
        elif(self.direction == '4'):
            x -= self.step_size
        elif(self.direction == '6'):
            x += self.step_size

        # save new location head and append to body
        self.positions.insert(0, (x, y))

        # collision detection body snake with head snake:
        # - positions_copy : old locations of snake
        # - self.positions : updated locations of snake
        # - self.positions[0] : location head snake now
        # - if self.positions[0] in pos :if true: head inside body snake
        if self.positions[0] in positions_copy:
            # just a log ...
            print("\033[31m u died \033[m")
            # stop move (copy is recoverd)
            self.positions = positions_copy

        # - limit movement inside board(game)
        if self.dot_in_rectangle([[0, 0], self.board_limit],
                                 self.positions[0]):
            # stop move (copy is recoverd) Limit board
            self.positions = positions_copy

    # check snake inside limit word or not
    def dot_in_rectangle(self, rectangle, pos):
        if rectangle[0][0] >= pos[0] or \
           rectangle[0][1] >= pos[1] or \
           rectangle[1][1] <= pos[0] or \
           rectangle[1][0] <= pos[1]:
            return True
        else:
            return False
