#!/usr/bin/env python3

import random as R
import sys

moves = {2:"DOWN", 8:"UP", 4:"LEFT", 6:"RIGHT"}

class gBoard():
    def __init__(self, dimensions, start_count, seed):
        self.b_WH = dimensions
        self.start_count = start_count
        R.seed(seed)

        self.board = [[0 for x in range(self.b_WH)] for y in range(self.b_WH)]

        for i in range(self.start_count):
            while True:
                x = R.randint(0,self.b_WH-1)
                y = R.randint(0,self.b_WH-1)

                if(self.board[y][x] == 0):
                    if(R.random() <= 0.1):
                        self.board[y][x] = 4
                    else:
                        self.board[y][x] = 2
                    break
                else:
                    pass

    def print_board(self):
        for y in range(self.b_WH):
            print("|", end="")
            for x in range(self.b_WH):
                print("{:<4.0f}|".format(self.board[y][x]), end="")
            print("")

    def check_status(self):
        if not any(0 in x for x in self.board):
            for y in range(self.b_WH):
                for x in range(self.b_WH):
                    if(y == 0):
                        if(self.board[y][x] == self.board[y+1][x]):
                            return True
                    elif(y == b_WH-1):
                        if(self.board[y][x] == self.board[y-1][x]):
                            return True
                    else:
                        if(self.board[y][x] == self.board[y-1][x] and self.board[y][x] == self.board[y+1][x]):
                            return True

                    if(x == 0):
                        if(self.board[y][x] == self.board[y][x+1]):
                            return True
                    elif(x == b_WH-1):
                        if(self.board[y][x] == self.board[y][x-1]):
                            return True
                    else:
                        if(self.board[y][x] == self.board[y][x-1] and self.board[y][x] == self.board[y][x+1]):
                            return True
        else:
            return True
        
        return False

    def add_piece(self):
        while True:
            x = R.randint(0,self.b_WH-1)
            y = R.randint(0,self.b_WH-1)

            if(self.board[y][x] == 0):
                if(R.random() <= 0.1):
                    self.board[y][x] = 4
                else:
                    self.board[y][x] = 2
                break
            else:
                pass

    def __DOWN_MOVE__(self):
        oldBoard = [x[:] for x in self.board]

        for y in reversed(range(self.b_WH)):
            for x in range(self.b_WH):
                if(y != self.b_WH-1):
                    act = self.board[y][x]

                    if(act != 0): #FOUND NUMBER
                        moved = False

                        for _y in range(self.b_WH-1-y): #CHECK FROM FOUND TO SIDE 
                            __y = _y+1 #START ONE PLACE FROM FOUND
                            test = self.board[y+__y][x] 

                            if(test != 0): #IF FOUND PLACE WITH NUMBER
                                if(test == act): #IF NUMBER == FIRST FOUND
                                    self.board[y][x] = 0
                                    self.board[y+__y][x] *= 2
                                else: #IF NUMBER IS DIFFERENT FROM FIRST FOUND
                                    self.board[y][x] = 0
                                    self.board[y+__y-1][x] = act

                                moved = True
                                break

                        if not (moved): #IF IT WENT THROUGH FULL ROW/COLUMN PLACE AT THE SIDE "totally left/right/top/bot"
                            self.board[self.b_WH-1][x] = self.board[y][x]
                            self.board[y][x] = 0 

        if(oldBoard == self.board):
            return "InvalidMove"
        else:
            pass

    def __UP_MOVE__(self):
        oldBoard = [x[:] for x in self.board]

        for y in range(self.b_WH):
            for x in range(self.b_WH):
                if(y != 0):
                    act = self.board[y][x]

                    if(act != 0):
                        moved = False

                        for _y in range(y):
                            __y = _y+1
                            test = self.board[y-__y][x]

                            if(test != 0):
                                if(test == act):
                                    self.board[y][x] = 0
                                    self.board[y-__y][x] *= 2
                                else:
                                    self.board[y][x] = 0
                                    self.board[y-__y+1][x] = act

                                moved = True
                                break

                        if not (moved):
                            self.board[0][x] = self.board[y][x]
                            self.board[y][x] = 0 

        if(oldBoard == self.board):
            return "InvalidMove"

    def __LEFT_MOVE__(self):
        oldBoard = [x[:] for x in self.board]

        for y in range(self.b_WH):
            for x in range(self.b_WH):
                if(x != 0):
                    act = self.board[y][x]

                    if(act != 0):
                        moved = False

                        for _x in range(x):
                            __x = _x+1
                            test = self.board[y][x-__x]

                            if(test != 0):
                                if(test == act):
                                    self.board[y][x] = 0
                                    self.board[y][x-__x] *= 2
                                else:
                                    self.board[y][x] = 0
                                    self.board[y][x-__x+1] = act

                                moved = True
                                break

                        if not (moved):
                            self.board[y][0] = self.board[y][x]
                            self.board[y][x] = 0 

        if(oldBoard == self.board):
            return "InvalidMove"

    def __RIGHT_MOVE__(self):
        oldBoard = [x[:] for x in self.board]

        for y in range(self.b_WH):
            for x in reversed(range(self.b_WH)):
                if(x != self.b_WH-1):
                    act = self.board[y][x]

                    if(act != 0):
                        moved = False

                        for _x in range(self.b_WH-1-x):
                            __x = _x+1
                            test = self.board[y][x+__x]

                            if(test != 0):
                                if(test == act):
                                    self.board[y][x] = 0
                                    self.board[y][x+__x] *= 2
                                else:
                                    self.board[y][x] = 0
                                    self.board[y][x+__x-1] = act

                                moved = True
                                break

                        if not (moved):
                            self.board[y][self.b_WH-1] = self.board[y][x]
                            self.board[y][x] = 0 

        if(oldBoard == self.board):
            return "InvalidMove"

    def process_move(self, move):
        if(moves[move] == "DOWN"):
            m = self.__DOWN_MOVE__()
        if(moves[move] == "UP"):
            m = self.__UP_MOVE__()
        if(moves[move] == "LEFT"):
            m = self.__LEFT_MOVE__()
        if(moves[move] == "RIGHT"):
            m = self.__RIGHT_MOVE__()

        if(m == "InvalidMove"):
            return "Invalid"
        else:
            self.add_piece()

            #PLAYABLE?
            if(self.check_status()):
                return True
            else:
                return False
                pass

if __name__ == "__main__":
    # Board vars
    b_WH = 4
    STARTING_COUNT = 3
    seedArg = R.randint(1,1000) 

    try:
        args = sys.argv
        #DOCELA COOL, ALE ASI SE TO TAKHLE NEDĚLÁ :D
        seedArg = int([x.split("=")[1] for x in args if "seed" in x][0])
        dimArg = int([x.split("=")[1] for x in args if "dim" in x][0])
        sCountArg = int([x.split("=")[1] for x in args if "scount" in x][0])

        b_WH = dimArg
        STARTING_COUNT = sCountArg
    except:
        pass

    game = gBoard(b_WH, STARTING_COUNT, seedArg)

    loop = 1
    print("#"*50)
    print("Game loop: {}".format(loop))

    game.print_board()

    while True:
        loop += 1
        while True:
            print("        8   ")
            print("MOVE: 4   6 ")
            print("        2   ")
            print()

            status = game.process_move(int(input()))
            print(status)
            if(status== "Invalid"):
                print("INVALID MOVE")
                pass
            else:
                print("#"*50)
                print("Game loop: {}".format(loop))
                game.print_board()
                break

            if not (status):
                print("GAME OVER")
            break

