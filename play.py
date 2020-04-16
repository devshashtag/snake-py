from board import Board
from snake import Snake
from food  import Food
from ai import AI
import random
import cv2
#--------------------------------------
# BOARD GAME
# size
size = [(0, 0), (40, 60)]
# board title
title = 'A simple AI Snake'
# range ( 0, 255 )
background = 0
foreground = 250
# - Window for drawing objects ( array )
board = Board(size, title, background, foreground)
#---------------------
# SNAKE
# start position
sposition=(0,0)
# start length snake
slength=2
# - Snake
snake = Snake(board, sposition, slength)
#--------------------
# Foods
food = Food(board)
# random location
food.randomize()
#--------------------------------------
# ai
ai = AI()
#--------------------
# game functions
# wait for key or end delay
def get_key(wait):
    # read key entered or sleep for end time
    return chr(cv2.waitKey(wait) & 0xFF)

# game starter
def render(snake):
    game_speed=100
    scale = 15
    paths = []
    key = snake.direction
    level = 4
    while True:
        #--------------------------------------------------
        # check food need eated or not . always use this function after showing snake
        snake.check_food(food)
        # clear snake  by default [color clear is board.bg ]
        snake.draw(False)
        # move with snake.direction variable
        snake.move()
        # game over
        if snake.died: break
        # draw snake again
        snake.draw(True)
        food.draw(True)
        #
        snake_head = snake.positions[0]
        food_pos   = food.position

        board.board[snake_head] = 100
        board.board[food_pos] = 150
        # show board
        board.show(scale)

        MAP = board.board
        # free target
        MAP[food_pos] = board.bg
        MAP[snake_head] = board.bg

        if paths == []:
            paths = get_paths(MAP, snake_head, food_pos, key)
            try_times = level
            if snake.length > 100:
                while paths == [ key ] and try_times:
                    paths = get_paths(MAP, snake_head, random.choice(board.free()), key)
                    try_times -= 1
        # ai key
        key = paths.pop(0)

        # read key and delay
        user = get_key(game_speed)
        key = user if user in "+-[]2468q" else key

        # if is not allowed move around
        # layer 2 dont die please :)
        key = allowed_action(snake, board, key)

        # is allowed directions ?
        if key in snake.directions:
            snake.direction = key
        # increase gane speed
        elif key == '+' and  game_speed >= 10:
            game_speed -=10 if game_speed > 10 else 9
        # decrease speed snake
        elif key == '-' : game_speed += 10
        # increase gane speed
        elif key == ']' : scale += 1
        # decrease speed snake
        elif key == '[' and  scale > 2: scale -= 1
        # quit from game
        elif key == 'q':
            break

def is_valid(pos, board, board_size, OPEN):
    y, x = pos
    h, w = board_size
    # check in boarder and not visited and empty cells
    return ( 0 <= y < h  and 0 <= x < w ) and \
        board[y, x] in OPEN


def allowed_action(snake,board,key):
    if key in "4268":
        MAP  = board.board
        OPEN = [ board.bg ]
        snake_head = snake.positions[0]
        board_size = (board.size[1][0], board.size[1][1])
        next_action = snake.next_position(snake_head , key)

        if not is_valid(next_action, MAP, board_size, OPEN):
            # possible directions
            allowed_directions = []
            for direction in "4268":
                next_action = snake.next_position(snake_head, direction)

                if is_valid(next_action , MAP, board_size, OPEN):
                    allowed_directions.append(direction)
            print("allow:",allowed_directions)
            if allowed_directions != []:
                return allowed_directions.pop()
    return key


def get_paths(board, src, dest, key):
    keys = []
    try:
        path = ai.path(board, src, dest)
        print("==========================")
        print(src, dest, key)
        keys = ai.convert_paths_to_keys(path)
    except Exception as e:
        print(e)

    if keys == []:
        keys = [ key ]

    print(f"next actions: { keys }")
    return keys

if __name__ == "__main__":
    render(snake)
    cv2.destroyAllWindows()

print(__name__)
