
class Snake(object):
    """ Snake """
    def __init__(self, board_limit, position=(0, 0),
                 slength=1, sdirection='6'):
        # board limit
        self.board_limit = board_limit
        # start position
        self.positions = [ position ]
        # start direction is right by default
        self.direction = sdirection
        # start length snake
        self.start_length = slength
        # length snake
        self.length = 0
        # score snake
        self.score = 0
        # snake died
        self.died = False

        # Allowed Directions
        #       8:UP
        #4:LEFT       6:RIGHT
        #      2:DOWN
        self.directions = "2468"
        print("\033[1;33len      : ", self.length)


    # eat food by snake
    def check_food(self, board, food):
        # collision detection food and snake
        if food.position == self.positions[0]:
            # find new random loaction for food
            food.randomize(board)
            # add length snake
            self.add_length()
            # add score
            self.score += 1
            # if food eated return true
            return True


    # add length snake
    def add_length(self):
        # add snake body
        # add a new length at last tail
        new_position = self.positions[self.length]
        self.positions.append(new_position)
        self.length += 1


    # draw snake in board
    def draw(self, board, is_draw):
        # check direction is allow
        if self.direction in self.directions:
            # show
            if is_draw:
                board.draw(self.positions, board.fg)
            # hide
            else:
                board.draw(self.positions, board.bg)


    # move snake in board
    def move(self):

        # possible_direciton
        self.directions = self.possible_direciton()

        # check direction is allow
        if self.direction in self.directions:
            # increase length each move and decrease start length
            if self.start_length > 0:
                self.start_length -= 1
                self.add_length()

            # move snake
            # -------------------------------------------------
            # unpack head location for move head
            x, y = self.positions[0]

            # detect key and move head snake
            # move up
            if(self.direction  == '8'):  y -= 1
            # move down
            elif(self.direction == '2'): y += 1
            # move left
            elif(self.direction == '4'): x -= 1
            # move right
            elif(self.direction == '6'): x += 1

            # new location of head but not save in self.positions
            # becase we need to know we are in board limit or not
            moved_position = (x, y)
            # -------------------------------------------------

            # - limit movement inside board(game) false is limited movement
            limit_check = self.point_in_rectangle(moved_position, self.board_limit)
            #delete last tail for shift all locations . and new location added after checks
            del self.positions[-1:]

            # collision detection body snake with head snake or board:
            # - self.positions : old locations of snake
            # - moved_position : new location head snake at now
            # if moved_position not in self.positions
            if moved_position not in self.positions and limit_check:
                # add new location of head to shited locations
                self.positions.insert(0, moved_position)
            else:
                # just a log ...
                print("\033[31mGAME OVER \033[m")
                self.died = True


    # you cant move reverse inside youself( limit movement )
    def possible_direciton(self):
        # prevent snake colliding with second body
        ch = self.direction

        if   ch in "46": return ch + "82"
        elif ch in "82": return ch + "46"
        else: return []

   # point_in_rectangle
    def point_in_rectangle(self, pos, rectangle):
        if rectangle[0][0] <= pos[0] and rectangle[0][1] <= pos[1] and \
           rectangle[1][0] > pos[0] and rectangle[1][1] > pos[1]:
            return True
        else:
            return False
