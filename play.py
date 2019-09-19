import cv2
# - - - - - - - - - - -
from board import Board
from snake import Snake
# - - - - - - - - - - -


def center_position(pos):
    return (pos[0] // 2, pos[1] // 2)


# initilize board
page = Board((800, 600), 0)


center_pos = center_position(page.size_board)
snake = Snake([(0, 0), page.size_board], center_pos)

# cv2.waitKey(10000)


while True:
    # check move key
    if snake.direction in snake.directions:
        # clear snake
        snake.draw(page.board, True, 0)
        if snake.start_length > 0:
            snake.start_length -= 1
            snake.add_length()
        # move with snake.direction variable
        snake.move()
        snake.draw(page.board)

    key = (cv2.waitKey(snake.speed) & 0xFF)

    if chr(key) in snake.directions:
        snake.direction = chr(key)
    elif (key == ord('+')):
        if(snake.speed > 10):
            snake.speed -= 5
    elif (key == ord('-')):
        snake.speed += 5
    elif (key == ord('p')):
        snake.direction = 'p'
    elif (key == ord('q')):
        break

cv2.destroyAllWindows()
