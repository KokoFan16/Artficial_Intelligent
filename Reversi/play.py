
from reversiboard import *
from player import *
from aiplayer import *
from time import time


print("""
Welcome to an interface for playing Reversi!

Select an option
  1) You vs Yourself
  2) You vs AI
  3) Random vs You
  4) Random vs AI
""")

# User choice which mode (1, 2, 3, 4)
choice = int(input("? "))
if 0 < choice < 5:
    ps = [None, None, None]
    # For the first two choice, the player1 is youself
    if choice < 3:
        ps[1] = HumanPlayer(1)
    # For the last two choice, the player1 is random player
    else:
        ps[1] = RandomPlayer(1)
    # For odd choice, the player2 is youself
    if choice % 2 == 1:
        ps[2] = HumanPlayer(2)
    # For even choice, the player2 is AI player
    else:
        ps[2] = AIPlayer(2)

    # Start game loop
    starttime = int(time())
    board = RBoard()
    # Loop until reach the terminal
    while board.terminal() == False:
        # action for each player
        act = ps[board.player()].taketurn(board)
        print(act)
        print("Player "+str(board.player())+" picked "+str(act[0])+","+str(act[1]))
        print("")
        # new board for each action
        board = board.result(act)
    print("")
    # Print terminal board
    board.print()
    print("")
    # Calculate the pieces number for each player when it reachs ternimal
    if board.utility(1) > board.utility(2):
        print("\n\nPlayer 1 wins!")
    elif board.utility(1) == 0:
        print("\n\nPlayer 1 and 2 tied!")
    else:
        print("\n\nPlayer 2 wins!")
    # If Random vs AI, print timing info
    if choice == 4:
        if starttime + (60*5) > int(time()):
            print("Great. Your AI averaged <5sec per move.")
        else:
            print("Uh oh. Your AI averaged >5sec per move!")
    #print(int(time())-starttime)
else:
    print("Sorry...")
    exit(1)

