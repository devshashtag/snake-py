# gm : unprogramable@gmail.com
# tel: @unprogramable
# RedFox :)
class AI(object):
    """ Simple AI for Snake"""

    def __init__(self):
        # possible movement
        #           [x+0, y-1]
        #  [x-1,y+0]{src: x,y}[x+1,y+0]
        #           [x+0, y+1]
        #-----------------------------
        # y + row_num[i]
        # x + col_num[i]
        self.row_num = [1,  0, 0, -1]
        self.col_num = [0, -1, 1, 0 ]
        self.symbols = "2468"

    # check location is valid in board area
    def is_valid(self, point, board, allowed_cells):
        x, y = point
        h = len(board)    # height
        w = len(board[0]) # width
        # check in boarder and not visited and empty cells
        return ( 0 <= y < h  and 0 <= x < w ) and \
               ( board[x][y] in allowed_cells )


    def path(self, board, src, dest, allowed_cells=[0]):
        self.ShowArray(board)
        """ find short path between two point """
        # source (x, y)
        src = tuple(src)
        # destination (x, y)
        dest = tuple(dest)
        # Create a queue for BFS
        node_queue = []
        # dict for visit cells
        visited_nodes = {}

        # check source and destination cell
        # in boarder and not empty and not equal
        if not (( self.is_valid(src,  board, allowed_cells) and \
                 self.is_valid(dest, board, allowed_cells)) or \
                 src is dest):
            return []
        # Mark the source cell as visited
        visited_nodes[src] = src

        # add source to queue
        node_queue.append([src, 0])

        # BFS starting from source cell
        while node_queue != []:
            # fetch first item in list
            pt = node_queue.pop(0)
            # If we have reached the destination cell, we are done return path
            #  x,y      x,y
            if pt[0] == dest:
                dest = dest
                path = [ dest ]
                while src != dest:
                    dest = visited_nodes[dest]
                    path.append(dest)
                return path[::-1]

            for pos in self.directions(pt[0]):
                # if adjacent cell is valid, has path and
                # not visited yet, enqueue it.
                if self.is_valid(pos, board, allowed_cells) and \
                   not visited_nodes.get(pos):
                    # mark cell as visited and enqueue it
                    visited_nodes[pos] = tuple(pt[0])
                    adjacent = [pos, pt[1]+1 ]
                    node_queue.append(adjacent)
        return []


    # find all direction left, right, up, down
    def directions(self, position):
        x, y = position
        positions = []
        for i in range(4):
            positions.append((x+self.col_num[i],
                              y+self.row_num[i]))
        return positions

    # convert position to symbol
    def convert_to_symbol(self, positions):
        arr_symbol =[]
        length = len(positions)
        for i in range(length):
            # count all array but (len -1)
            if i < (length - 1):
                # current item
                item = positions[i]
                # next item
                nitem = positions[i+1]
                # find all possible direction for item
                dirs = list(self.directions(item))
                # next_item in next direction
                if nitem in dirs:
                    index = dirs.index(nitem)
                    arr_symbol.append(self.symbols[index])
        return arr_symbol

    # print arrays
    def ShowArray(self, arr):
        for row in arr:
            for col in row:
                print(col,end="")
            print("")
