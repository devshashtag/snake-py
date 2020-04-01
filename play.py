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
background = 12
# - Window for drawing objects ( array )
board = Board(size, title, background)


# SNAKE
# start position
sposition=(1, 1)
# objects cant exit from this border
board_limit = board.size
# start length snake
slength=50
# - Snake
snake = Snake(board_limit, sposition, slength)


# Foods
food = Food()
food.randomize(board)

# game functions

# wait for key or end delay
def getch_or_delay(time):
    # read key entered or sleep for end time
    return chr(cv2.waitKey(time) & 0xFF)

# game starter
def render(snake):

    game_speed=300
    scale = 10
    while True:
        #--------------------------------------------------
        # check food need eated or not . always use this function after showing snake
        snake.check_food(board, food)

        # clear snake  by default [color clear is board.bg ]
        snake.draw(board, False)

        # move with snake.direction variable
        snake.move()

        # game over
        if snake.died: break

        # draw snake again
        snake.draw(board, True)

        # display board
        board.show(scale)
        #---------------------LOGS-------------------------
        print("\033[1;33mpossible direction : ", list(snake.possible_direciton()) ,"=> now " ,snake.direction)
        print("\033[1;33mmy length          : ",  snake.length, "Score: ",snake.score)
        #--------------------------------------------------
        # read key and delay
        key = getch_or_delay(game_speed)

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
