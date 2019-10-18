

from player import Player 
import random

class AIPlayer(Player):
    def __init__(self, p, depth = 4):
        self.playerN = p
        self.depth = depth

    def taketurn(self, board):
        board.print()
        
        v, action = self.alphaBeta(board, self.depth)
        return action
    
    # min_max with alpha Beta pruning and limit depth
    def alphaBeta(self, board, depth, alpha = float('-inf'), beta=float('inf')):

        player = board.player()

        # Return evaluation value if depth equals 0 or game terminal
        if depth == 0 or board.terminal():
            return self.evaluation(board), ()

        # Player 2 is max, and play 1 is min
        v = float('-inf') if player == 2 else float('inf')

        # best_action is the best action for cuurent board
        best_action = None
        for a in board.actions():
            # next board with action a
            next_board = board.result(a)
            # Recursive call alphaBeta
            val, next_action = self.alphaBeta(next_board, depth -1, alpha, beta)
            # max record its best action and update alpha
            if player == 2:
                if val > v:
                    v = val
                    best_action = a
                if v >= beta:
                    return v, best_action
                alpha = max(alpha, v)
            # min record its best action and update beta
            else:
                if val < v:
                    v = val
                    best_action = a
                if v <= alpha:
                    return v, best_action
                beta = min(beta, v)
        return v, best_action
            

    def evaluation(self, board):
        
        # weight score which comes from weight map
        weightScore = self.weightScore(board)
        mobilityScore = self.mobilityScore(board)
        
        # stable discs: the number of discs which cannot be flipped
        # more is better
        stable2 = self.stableScore(board, 2)
        stable1 = self.stableScore(board, 1)
        stableScore = stable2 - stable1
        
        # frontier dicss: the number of empty neighbouring squares
        # less is better
        frontierScore = self.frontierScore(board)

        return weightScore + 10 * mobilityScore + 15 * stableScore + 5 * frontierScore
    
    # Weight score
    def weightScore(self, board):
        
        # weight value for player1 and player2
        weight1 = 0
        weight2 = 0

        # weight map
        weight_scores = [[99, -8, 8, 6, 6, 8, -8, 99],
                         [-8, -24, -4, -3, -3, -4, -24, -8],
                         [8, -4, 7, 4, 4, 7, -4, 8],
                         [6, -3, 4, 0, 0, 4, -3, 6],
                         [6, -3, 4, 0, 0, 4, -3, 6],
                         [8, -4, 7, 4, 4, 7, -4, 8],
                         [-8, -24, -4, -3, -3, -4, -24, -8],
                         [99, -8, 8, 6, 6, 8, -8, 99]]
        
        # Calculate weight value for each player
        for r in range(8):
            for c in range(8):
                if board.data[r][c] == 2:
                    weight2 += weight_scores[r][c]
                if board.data[r][c] == 1:
                    weight1 += weight_scores[r][c]
    
        # Return max - min
        return (weight2 - weight1)
    
    
    # stable score: the number of dics which cannot be flipped
    def stableScore(self, board, player):
        
        # stable score
        stableScore = 0
        # Used to record cloumn for each row while searching the stable dics
        record_c = [0, 0, 0, 0, 0, 0, 0, 0]

        r = 0
        # Searching from the corner data[0][0]
        while r < 8 and board.data[r][0] == player:
            stableScore += 1
            c = 1
            while c < 8 and board.data[r][c] == player:
                stableScore += 1
                c += 1
            record_c[r] = c
            r += 1
        
        # Searching from the corner data[7][0]
        if r != 7:
            r = 7
            while r > 0 and board.data[r][0] == player:
                stableScore += 1
                c = 1
                while c < 8 and board.data[r][c] == player:
                    stableScore += 1
                    c += 1
                record_c[r] = c
                r -= 1
    
        # Searching from the corner data[0][7]
        r = 0
        while r < 8 and board.data[r][7] == player:
            if record_c[r] == 7:
                break
            else:
                c = 7
                stableScore += 1
                while c > 0 and board.data[r][c] == player:
                    stableScore += 1
                    c -= 1
            r += 1

        # Searching from the corner data[7][0]
        if r != 7:
            r = 7
            while r > 0 and board.data[r][7] == player:
                if record_c[r] == 7:
                    break
                else:
                    c = 7
                    stableScore += 1
                    while c > 0 and board.data[r][c] == player:
                        stableScore += 1
                        c -= 1
                r -= 1
        
        return stableScore
            
    # The number of possible moves
    def mobilityScore(self, board):

        mobilityScore = 0;
        
        # If player is 1, return the min value of mobility
        if board.player == 1:
            mobilityScore = -1 * len(board.actions())
        
        # If player is 2, return the min value of mobility
        else:
            mobilityScore = len(board.actions())

        return mobilityScore

    # frontier dicss: the number of empty neighbouring squares
    def frontierScore(self, board):
    
        # eight neighbors for each disc
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        spaces1 = []
        spaces2 = []
    
        for r in range(8):
            for c in range(8):
                # calculate frontier discs for player 1
                if board.data[r][c] == 1:
                    for i, j in dirs:
                        if 0<(r+i)<8 and 0<(c+j)<8 and board.data[r+i][c+j] == 0 and (r+i, c+j) not in spaces1:
                            spaces1.append((r+i, c+j))
                # calculate frontier discs for player 2
                if board.data[r][c] == 2:
                    for i, j in dirs:
                        if 0<(r+i)<8 and 0<(c+j)<8 and board.data[r+i][c+j] == 0 and (r+i, c+j) not in spaces2:
                            spaces2.append((r+i, c+j))
        # try to reduce frontier 
        return len(spaces1) - len(spaces2)


    def player(self):
        return self.playerN
    

