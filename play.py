import cv2
from board import Board
from snake import Snake


# - initilize Window
window_size = (800, 600)
title = 'Micro Robot: Snake'
bg_color = 12

# - Window for drawing objects ( array )
board = Board(window_size, title, bg_color)

# - SNAKE (player)
# calculate and return center position in window
def center_position(pos):
    return (pos[0]//2, pos[1]//2)

start_position = center_position(board.size_window)
window_limit = [(0, 0), board.size_window]

snake = Snake(board, start_position, window_limit, 100)

# - -  start game - -
def render(snake):
    while True:
        # clear snake  by default [color clear is bg_color]
        snake.draw(False)
        # move with snake.direction variable
        snake.move()
        # draw snake again
        snake.draw(True)
        # - - end game - -
        if snake.died and snake.positions[snake.length] == snake.positions[0]:
            # clear snake
            snake.draw(False)
            # - remove food
            snake.food.draw(snake.board.window, True, snake.board.bg_color)
            # delete objects
            del snake.food
            del snake
            break

        snake.board.draw_window()
        # read key and delay
        key = snake.board.get_key(snake.speed)

        # action is allowed directions(p for pause)
        if key in snake.directions or key == 'p':
            snake.direction = key
        # increase speed snake
        elif (key == '+'):
            if(snake.speed > 10):
                snake.speed -= 10
        # decrease speed snake
        elif (key == '-'):
            snake.speed += 10
        # quit from game
        elif (key == 'q'):
            snake.speed = 1
            snake.died = True


render(snake)

cv2.destroyAllWindows()
