

import copy, queue

class Board:
    # initial board
    # for each tile, its domain is {1,2,3,4,5,6,7,8,9},
    # which means all possible values for each tile
    def __init__(self):
        self.assignedset = set()
        self.data = []
        for r in range(9):
            rowdata = []
            for c in range(9):
                rowdata.append({1,2,3,4,5,6,7,8,9})
            self.data.append(rowdata)
    
    def result(self, coord, v):
        r,c = coord
        # if value of the tile is included in its domain, else return None
        if v in self.data[r][c]:
            res = copy.deepcopy(self)
            # assign {v} as its new domain
            res.data[r][c] = {v}
            # This queue is used to record all the tiles with single domain
            propqueue = queue.Queue()
            propqueue.put((r,c))
            # For each tile with single domain, remove this value from same row, column and 3*3 group
            while propqueue.qsize() > 0:
                r,c = propqueue.get()
                v = list(res.data[r][c])[0]
                # If this tile has been visited before, just skip it
                if (r,c) in res.assignedset:
                    continue
                # Add the current tile into seen set
                res.assignedset.add((r,c))
                # Remove it from same row
                for i in range(9):
                    if i != r:
                        res.data[i][c].discard(v)
                        # If there is no any value in domian after remove, it means invild board
                        if not res.data[i][c]:
                            return None
                        # If there is only one value in domian, add it to the queue
                        if len(res.data[i][c]) == 1:
                            propqueue.put((i,c))
                # Remove it from same column
                for i in range(9):
                    if i != c:
                        res.data[r][i].discard(v)
                        if not res.data[r][i]:
                            return None
                        if len(res.data[r][i]) == 1:
                            propqueue.put((r,i))
                # Remove it from the 3*3 group
                gr = int(r/3)*3
                gc = int(c/3)*3
                for i in range(gr,gr+3):
                    for j in range(gc,gc+3):
                        if i!=r and j!=c:
                            res.data[i][j].discard(v)
                            if not res.data[i][j]:
                                return None
                            if len(res.data[i][j]) == 1:
                                propqueue.put((i,j))
            return res
        else:
            return None

    # Print the current board.
    # For each tile, print all the current possile values.
    def printboard(self):
        for r in range(9):
            for c in range(9):
                d = self.data[r][c]
                st = ''
                for v in d: st += str(v)
                while len(st) < 10: st += ' '
                print(st, end='')
            print("")

# DFS search
def solve(board):
    # If all the 81 tiles in the board has been visited, just end search
    if len(board.assignedset) == 81:
        return board
    # DFS for all the tile which domain has more than one value
    for r in range(9):
        for c in range(9):
            d = board.data[r][c]
            if len(d) > 1:
                for v in d:
                    b = board.result((r, c), v)
                    if b:
                        # Recursive call
                        b = solve(b)
                        if b: return b
                return None



# Input a vaild suduko question row by row
# For each tile, the value should be (1~9)
# After input one row, call result function for each tile.
def inputboard():
    print("Enter each row. A 0 is blank.")
    b = Board()
    for r in range(9):
        rowstr = input("row "+str(r+1)+": ")
        for c in range(9):
            v = int(rowstr[c])
            if 10 > v > 0:
                b = b.result((r,c), v)
                if b == None:
                    print("Invalid assignment "+str(r)+","+str(c)+","+str(v))
                    exit(1)
    return b


b = inputboard()
b = solve(b)
if b:
    b.printboard()



