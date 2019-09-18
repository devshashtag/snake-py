import cv2
# - - - - - - - - - - -
from board import Board
from snake import Snake
from food import Food
# - - - - - - - - - - -


def center_position(pos):
    return (pos[1]//2, pos[0]//2)


# initilize board
page = Board((200, 350), 0)


center_pos = center_position(page.size_board)
snake = Snake(page.size_board, center_pos)
