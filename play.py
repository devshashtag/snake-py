from board import Board
from snake import Snake
from food  import Food
import cv2

# BOARD GAME
# size
size = [(0, 0), (80, 60)]
# board title
title = 'A simple AI Snake'
# range ( 0, 255 )
background = 0
foreground = 250
# - Window for drawing objects ( array )
board = Board(size, title, background, foreground)

# SNAKE
# start position
sposition=(1, 1)
# start length snake
slength=4
# - Snake
snake = Snake(board, sposition, slength)

# Foods
food = Food(board)
# random location
food.randomize()

# game functions
# wait for key or end delay
def get_key(wait):
    # read key entered or sleep for end time
    return chr(cv2.waitKey(wait) & 0xFF)

# game starter
def render(snake):

    game_speed=300
    scale = 30

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

        board.show(scale)
        # read key and delay
        key = get_key(game_speed)

        # is allowed directions ?(p for pause)
        if key in snake.directions or key == 'p':
            snake.direction = key
        # increase gane speed
        elif key == '+' and  game_speed > 10: game_speed -= 10
        # decrease speed snake
        elif key == '-' : game_speed += 10
        # increase gane speed
        elif key == ']' : scale += 1
        # decrease speed snake
        elif key == '[' and  scale > 2: scale -= 1
        # quit from game
        elif key == 'q':
            break


render(snake)
cv2.destroyAllWindows()
