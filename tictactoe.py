board = [" " for i in range(10)]
board[0] = None

def printboard(board):
    print(" "+" "+" | "+" "+" | "+" "+" ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print(" "+" "+" | "+" "+" | "+" "+" ")
    print("-----------")
    print(" "+" "+" | "+" "+" | "+" "+" ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print(" "+" "+" | "+" "+" | "+" "+" ")
    print("-----------")
    print(" "+" "+" | "+" "+" | "+" "+" ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print(" "+" "+" | "+" "+" | "+" "+" ")

def checkposition(pos):
    return board[pos] == " "

def insertpos(letter, pos):
    board[pos] = letter

def boardempty(board):
    if board.count(" ")>0:
        return True
    else:
        return False

def getwinner(letter, board):
    return ( (board[1]==letter and board[2]==letter and board[3]==letter) or
             (board[4]==letter and board[5]==letter and board[6]==letter) or
             (board[7]==letter and board[8]==letter and board[9]==letter) or
             (board[1]==letter and board[4]==letter and board[7]==letter) or
             (board[2]==letter and board[5]==letter and board[8]==letter) or
             (board[3]==letter and board[6]==letter and board[9]==letter) or
             (board[1]==letter and board[5]==letter and board[9]==letter) or
             (board[3]==letter and board[5]==letter and board[7]==letter)
    )

def selectRandom(l):
    import random
    ln = len(l)

    move = random.randrange(0, ln)
    return l[move]

def computermove():
    possiblemoves = [l for l, letter in enumerate(board) if letter==" " and l!=0 ]
    move = 0

    for letter in ["o", "X"]:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = letter

            if getwinner(letter, boardcopy):
                move = i
                return move
    
    cornersopen = []
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move = selectRandom(cornersopen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgeopen = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgeopen.append(i)
    if len(edgeopen)>0:
        move = selectRandom(edgeopen)
        return move

def cleanboard():
    global board
    board = [" " for i in range(10)]
    board[0] = None

def main():
    ch = 'y'
    print("Player sign is 'X' and computer's sign is 'o' ")

    while(ch=='y'):
        cleanboard()
        while(boardempty(board) and (not getwinner("X", board)) and (not getwinner("o", board)) ):
            run = True
            while run:
                printboard(board)
                pos = input("Enter number between 1 to 9:- ")
                try:
                    pos = int(pos)
                    if pos>0 and pos<10:
                        run = False
                    else:
                        print("Enter number from 1 to 9 only")
                        continue
                except:
                    print("Enter a number")
                    continue
                # check position is empty
                insertpossible = checkposition(pos)
                if insertpossible:
                    insertpos("X", pos)
                    if getwinner("X", board):
                        printboard(board)
                        print("You won the game")
                        break
                    if boardempty(board):
                        cm = computermove()
                        insertpos("o", cm)
                        if getwinner("o", board):
                            printboard(board)
                            print("You loose")
                            break                   
                        continue
                    elif not boardempty(board):
                        if getwinner("X", board):
                            printboard(board)
                            print("You Won game")
                            break
                        else:
                            printboard(board)
                            print("Game Tie")
                else:
                    print("position is not empty")
                    continue

        ch = input("Do you want to play again? Press y to continue:- ")

if __name__ == "__main__":
    main()