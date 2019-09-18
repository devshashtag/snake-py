
import random
import cv2
# - - - - - - - - - - -
from board import Board
from snake import Snake
from food import Food
# - - - - - - - - - - -


page = Board((200,350),130)
cv2.imshow('Snake Q Learning', page.board)
cv2.waitKey(500000)
