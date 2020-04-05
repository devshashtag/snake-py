# gm : unprogramable@gmail.com
# tel: @unprogramable
# RedFox :)
import random
class AI(object):
    """ Simple AI for Snake"""

    def __init__(self):
        pass

    # check location is valid in board area
    def is_valid(self, point, board):
        y ,x = point
        h = len(board)    # height
        w = len(board[0]) # width
        # check in boarder and not visited and empty cells
        return ( 0 <= y < h  and 0 <= x < w )


    def path(self, board, src, dest, OPEN=[0]):
        """ find short path between two point """
        # Create a queue for BFS
        node_queue = []
        # dict for visit cells
        visited_nodes = {}
        # dest is open
        board[dest] = OPEN[0]

        # check source and destination cell
        # in boarder and not empty and not equal
        if not ( self.is_valid(src, board)  and \
                 self.is_valid(dest, board) and \
                 src != dest):
            return []

        # Mark the source cell as visited
        visited_nodes[src] = src

        # add source to queue
        node_queue.append([src, 0])
        fill = 0
        for i in board:
            for j in i:
                if j != OPEN:
                    fill += 1
        # BFS starting from source cell
        while node_queue != []:
            # fetch first item in listx
            if fill > 50:
                if 50 > len(node_queue) > 20  :
                    pt = node_queue.pop(random.randint(1,2))
                else:
                    pt = node_queue.pop(0)
            else:
                pt = node_queue.pop(0)

            # path finded if we are in dest
            #    y           y             x          x
            if pt[0] == dest:
                path = [ dest ]
                while src != dest:
                    dest = visited_nodes[dest]
                    path.append(dest)
                return path[::-1]

            # check other ways
            for pos in self.directions(pt[0]):
                # if adjacent cell is valid, has path and
                # not visited yet, enqueue it.
                if self.is_valid(pos, board) and \
                   (board[pos] in OPEN) and \
                   not visited_nodes.get(pos):
                    # mark cell as visited and enqueue it
                    visited_nodes[pos] = tuple(pt[0])
                    adjacent = [pos, pt[1]+1 ]
                    node_queue.append(adjacent)

        return []


    def directions(self, position):
        #         up 8
        #
        # 4 left  pos  right 6
        #
        #         down 2
        y, x = position
        return [(y  , x+1),  # RIGHT
                (y  , x-1),  # LEFT
                (y-1, x  ),  # UP
                (y+1, x  )]  # DOWN



    # convert position to symbol
    def convert_to_symbol(self, positions):
        arr_symbol =[]
        symbols = "6482"
        for i in range(len(positions)):
            if i < (len(positions) - 1): # count all array but (len -1)
                item = positions[i]    # current item
                nitem = positions[i+1] # next item
                dirs = list(self.directions(item)) # find all possible direction for item
                if nitem in dirs: # next_item in next direction
                    index = dirs.index(nitem)
                    arr_symbol.append(symbols[index])
        return arr_symbol

    # print arrays
    def ShowArray(self, arr):
        for row in arr:
            for col in row:
                print(col,end="")
            print("")
