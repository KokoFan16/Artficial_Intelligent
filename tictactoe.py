import copy
class State:
    def __init__(self, board):
        self.board = board # -1 for opposite, 1 for us, 0 for empty

    def goal(self):
        return self.board.goal()

    def player(self):
        return self.board.player

    def printboard(self):
        return self.board.printboard()

    def successor(self):
        succs = []
        pos = self.board.get_avail_pos()
        for p in pos:
            board = copy.deepcopy(self.board)
            board.put(p)
            succs += State(board),
        return succs

class Board:
    def __init__(self, first_player):
        self.player = first_player # player, 1 is us, -1 is opposite
        self.data = [0] * 9 # -1 for opposite, 1 for us, 0 for empty
        self.point = [10, 5, -10, 0] # 10 for win, 5 for tie, -10 for lose, 0 for intermidiate
        self.win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]

    def goal(self):
        for state in self.win_states:
            sumboard = sum(self.data[i] for i in state)
            if sumboard == 3:
                return self.point[0] # 10
            elif sumboard == -3:
                return self.point[2] # -10

        for pos in self.data:
            if pos == 0:
                return self.point[3] # 0

        return self.point[1] # 5

    def get_avail_pos(self):
        pos = []
        for i, n in enumerate(self.data):
            if n == 0:
                pos += i,
        return pos

    def put(self, loc):
        if loc < 0 or loc > 8 or self.data[loc] != 0:
            return False
        else:
            self.data[loc] = self.player
            self.player = -self.player
            return True

    def printboard(self):
        s = ''
        for i, d in enumerate(self.data):
            if i % 3 == 0:
                s += '\n'
            if d == 1:
                s += 'X'
            if d == 0:
                s += str(i)
            if d == -1:
                s += 'O'
        print(s)


class Agent:
    def __init__(self, player):
        self.player = player
    def put(self, state):
        pass
    def comment(self, goal):
        pass

class Computer(Agent):

    def put(self, state):
        print("\nCOM %d says: My turn..." % self.player)
        val, nxt_state = self.abpruning(state)
        print("COM %d says: My move:" % self.player)
        nxt_state.printboard()
        return nxt_state

    def comment(self, goal):
        if goal == 5:
            print("COM %d says: I'm undefeated..." % self.player)
        elif goal*self.player > 0:
            print('COM %d says: GG, EZ' % self.player)
        else:
            print('COM %d says: No...' % self.player)

    def abpruning(self, cur, alpha=float('-inf'), beta=float('inf')):
        # print(alpha, beta)
        flag = cur.goal()
        if flag != 0:
            return flag, cur
        else:
            v = float('-inf') if cur.player() == 1 else float('inf')
            best_state = None
            for n in cur.successor():
                val, nxt_state = self.abpruning(n, alpha, beta)
                if cur.player() == 1:
                    if val > v:
                        v = val
                        best_state = n
                    if v >= beta:
                        return v, best_state
                    alpha = max(alpha, v)
                else:
                    if val < v:
                        v = val
                        best_state = n
                    if v <= alpha:
                        return v, best_state
                    beta = min(beta, v)
            return v, best_state


    def minimax(self, cur):
        flag = cur.goal()
        if flag != 0:
            return flag, cur
        else:
            values = []
            for n in cur.successor():
                val, nxt_state = self.minimax(n)
                values +=(val, n),
            if cur.player() == 1:
                return max(values, key = lambda x: x[0])
            else:
                return min(values, key = lambda x: x[0])

class User(Agent):

    def put(self, state):
        inserted = False
        while not inserted:
            pos = int(input('Please input (0-8):'))
            board = copy.deepcopy(state.board)
            inserted = board.put(pos)
        nxt_state = State(board)
        print('Your move:')
        nxt_state.printboard()
        return nxt_state

    def comment(self, goal):
        if goal == 5:
            print("Tied!")
        elif goal*self.player > 0:
            print("You Win!")
        else:
            print("You Lose...")


def gen_board(first_player=1, sequence=[]):
    board = Board(first_player)
    for p in sequence:
        board.put(p)
    return board


def main():
    startboard = gen_board(first_player=1, sequence=[])
    startstate = State(startboard)
    agents = [User(1), Computer(-1)]

    play(startstate, agents)

def play(state, agents):
    goal = state.goal()
    while goal == 0:
        for a in agents:
            state = a.put(state)
            goal = state.goal()
            if goal != 0:
                break
    for a in agents:
        a.comment(goal)



if __name__ == '__main__':
    main()
