import cv2
# import random
from food import Food


class Snake(object):
    """ Snake """

    def __init__(self, board, start_position=(10, 10), window_limit=0,
                 start_length=1, first_direction='6', step_size=10,
                 speed=100):
        # window
        # - center position of window
        head_position = start_position
        # - limit move items inside window
        if window_limit == 0:
            window_limit = [(0, 0), board.size_window]
        # - window for draw snake
        self.board = board
        # initialize attribute snake:
        self.window_limit = window_limit
        # start length from 0 to start_length
        self.start_length = start_length

        # 2:DOWN, 4:LEFT, 6:RIGHT, 8:UP
        self.directions = "6428"
        # size of each part
        self.step_size = step_size
        # speed snake
        self.speed = speed
        # score snake
        self.score = self.start_length
        # controller head '6' = right
        self.direction = first_direction
        # initialize head
        self.positions = [ head_position ]
        # length snake
        self.length = len(self.positions) - 1
        # snake died
        self.died = False

        # food
        self.food = Food(self.window_limit, self.step_size)

    # eat food by snake
    def eat_food(self):
        # - collision detection food and snake
        food_x = self.food.pos[0]
        food_y = self.food.pos[1]
        size_food = self.food.step_size
        # area food for detection
        area_food = [
            (food_x - size_food, food_y - size_food),
            (food_x + size_food, food_y + size_food)
        ]

        # just a log
        # print(area_food ,' : ', end="")
        # print(self.positions[0])

        # food inside head snake
        food_detection = self.dot_in_rectangle(
            area_food, self.positions[0])

        if food_detection:
            # - remove food
            self.food.draw(self.board.window, True, self.board.bg_color)
            print("Eat Food")
            # - add length snake
            self.add_length()
            # - add score
            self.score += 1
            # - generate position food
            self.food.randomize()
        # - always show food
        self.food.draw(self.board.window)

    # add length snake
    def add_length(self):
        # add snake body
        # add a new length at last tail
        new_position = self.positions[self.length]
        self.positions.append(new_position)
        self.length += 1

    # draw snake in window
    def draw(self, is_draw=True, clear_color=0):
        # check direction is allow
        if self.direction in self.directions:
            # - draw snake just into window(array)
            if is_draw:
                for pos in self.positions:
                    # print color snake random
                    # color = random.randint(200, 250)
                    # static color
                    color = 250
                    # head color
                    if pos == self.positions[0]:
                        color = 180
                    cv2.circle(self.board.window, tuple(pos),
                            self.step_size//2, color, -1)
            else:
                # Note: after clear snake draw again snake
                # change clearn color to bg color
                if clear_color == 0:
                    clear_color = self.board.bg_color
                # find last tail position
                last_tail = self.positions[self.length]
                # clear last position
                cv2.circle(self.board.window, last_tail, self.step_size//2, clear_color, -1)

    # move snake in window
    def move(self):
        # prevent snake colliding with second body
        if self.direction in "46":
            self.directions = self.direction + "82"
        elif self.direction in "82":
            self.directions = self.direction + "46"
        # just a log
        # print(f"\033[31m{self.directions}")

        # check direction is allow
        if self.direction in self.directions:

            # increase length each move and decrease start length
            if self.start_length > 0:
                self.start_length -= 1
                self.add_length()

            # - move up down left right with keys (with 2,4,6,8 and arrows)
            # unpack head locations for update
            x, y = self.positions[0]
            # if snake is died . dont move head so snake is hide
            if not self.died:
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
            # if snake is died hide snake
            if head_new_position not in self.positions and limit_check or self.died:
                # body mover( delete last tail[shift all locations to new locations])
                del self.positions[-1:]
                # add new location of head to shited locations
                self.positions.insert(0, head_new_position)
                self.eat_food()
            else:
                # just a log ...
                print("\033[31m u died \033[m")
                self.speed = 1
                self.died = True

    # limit checker for movment snake (window)
    def dot_in_rectangle(self, rectangle, pos):
        if rectangle[0][0] < pos[0] and rectangle[0][1] < pos[1] and \
           rectangle[1][0] > pos[0] and rectangle[1][1] > pos[1]:
            return True
        else:
            return False
