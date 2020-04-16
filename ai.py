# gm : unprogramable@gmail.com
# tel: @unprogramable
# RedFox :)

class AI(object):
    """ Simple AI for Snake"""

    # check location is valid in board area
    def is_valid(self, point, board, OPEN):
        y ,x = point
        h = len(board)    # height
        w = len(board[0]) # width
        # check in boarder and not visited and empty cells
        return ( 0 <= y < h  and 0 <= x < w ) and \
               ( board[point] in OPEN )


    def path(self, board, src, dest, OPEN=[0]):
        """ find short path between two point """

        # check source and destination cell
        # in boarder and not empty and not equal
        if not (self.is_valid(src , board, OPEN) and \
                self.is_valid(dest, board, OPEN) and \
                src != dest):
            return []

        # Add source cell to queue
        node_queue = [ [src, 0] ]
        # Mark the source cell as visited
        visited_nodes = { src: src }

        # path starting from source cell (BFS algorithm)
        while node_queue != []:
            # fetch first item in list
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
                # if pos not visited. visit and enqueue it.
                if ( self.is_valid(pos, board, OPEN) ) and \
                   ( not visited_nodes.get(pos) ):
                    # mark cell as visited and enqueue it
                    visited_nodes[pos] = tuple( pt[0] )
                    node_queue.append([pos, pt[1]+1 ])
        return []


    def directions(self, position):
        y, x = position
        return [(y  , x+1),  # RIGHT 6 >
                (y  , x-1),  # LEFT  4 <
                (y-1, x  ),  # UP    8 ^
                (y+1, x  )]  # DOWN  2 v


    def convert_paths_to_keys(self, positions):
        keys =[]
        symbols = "6482"
        for i in range(len(positions)):
            if i < (len(positions) - 1):           # count all array but (len -1)
                item = positions[i]                # current item
                nitem = positions[i+1]             # next item
                dirs = list(self.directions(item)) # find all possible direction for item
                if nitem in dirs:                  # next_item in next direction
                    index = dirs.index(nitem)
                    keys.append(symbols[index])
        return keys

    # print arrays
    def ShowArray(self, arr):
        for row in arr:
            for col in row:
                print(col,end="")
                print("")
