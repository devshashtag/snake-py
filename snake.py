import cv2
import random


class Snake(object):
    def __init__(self, board_limit, head_position=(0, 0), start_length=5,
                 first_direction='6', step_size=5, speed=150):
        # initialize attribute snake:
        self.snake_limit = board_limit
        self.start_length = start_length
        self._length = 0
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
        new_position = self.positions[self._length]
        self.positions.append(new_position)
        self._length += 1

    def draw(self, board, is_clear=False, color=0):
        # - draw the snake with cv2
        if is_clear:
            # Note: after clear snake draw again snake
            # find last tail position
            last_tail = self.positions[self._length]
            # clear last position
            cv2.circle(board, last_tail, self.step_size, color, -1)
        else:
            for pos in self.positions:
                # print color snake
                color = random.randint(150, 250)
                cv2.circle(board, tuple(pos), self.step_size, color, -1)

        # show board after draw circles
        cv2.imshow('Micro Robot: AI Snake Q Learning', board)

    def move(self):
        # - move up down left right with keys (with 2,4,6,8 and arrows)
        # copy all positions
        positions_copy = self.positions.copy()

        # body mover( shift all location to next state)
        del self.positions[self._length]

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

        # Collision detection body snake:
        # - positions_copy : old locations of snake
        # - self.positions : updated locations of snake
        # - self.positions[0] : location head snake now
        # - if self.positions[0] in pos : true head inside body snake
        if self.positions[0] in positions_copy:
            # just a log ...
            print("\033[31m this is bad \033[m")
            # stop move (copy is recoverd)
            self.positions = positions_copy

        # - limit movement inside board(game)
