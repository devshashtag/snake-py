import cv2
from board import Board
from snake import Snake


# - initilize Window
bg_color = 12
window_size = (800, 600)

# - Window for drawing objects ( array )
board = Board(window_size, bg_color)

# - SNAKE (player)
# calculate and return center position in window
def center_position(pos):
    return (pos[0]//2, pos[1]//2)

start_position = center_position(board.size_window)
window_limit = [(0, 0), board.size_window]

snake = Snake(board, start_position, window_limit, 100)

def render(snake):
    while True:
        # check move key
        if snake.direction in snake.directions:
            # clear snake  by default [color clear is bg_color]
            snake.draw(True)

            # increase length each move and decrease start length
            if snake.start_length > 0:
                snake.start_length -= 1
                snake.add_length()

            # move with snake.direction variable
            snake.move()
            # draw snake again
            snake.draw()
            # end game
            if snake.died and snake.positions[snake.length] == snake.positions[0]:
                # clear snake
                snake.draw(True)
                break

        # read key entered and sleep for control (speed snake)
        key = chr(cv2.waitKey(snake.speed) & 0xFF)

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
