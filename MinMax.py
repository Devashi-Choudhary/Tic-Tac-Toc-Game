import copy
import time
count=0
def CreateBoard():
    Board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    for i in range(Side):
        print(Board[i])
    return Board

def show_Board(Board):
    for i in range(3):
        print(Board[i])

def Success_Game(Board):
    for i in range(Side):
        if(Board[i][0]=='O' and Board[i][1]=='O'and Board[i][2]=='O'):
           return True
    for j in range(Side):
        if(Board[0][j]=='O'and Board[1][j]=='O' and Board[2][j]=='O'):
           return True
    if(Board[0][0]=='O' and Board[1][1]=='O'and Board[2][2]=='O'):
        return True
    if(Board[0][2]=='O'and Board[1][1]=='O' and Board[2][0]=='O'):
        return True
    return False

def Lose_Game(Board):
    for i in range(Side):
        if(Board[i][0]=='X' and Board[i][1]=='X'and Board[i][2]=='X'):
           return True
    for j in range(Side):
        if(Board[0][j]=='X'and Board[1][j]=='X' and Board[2][j]=='X'):
           return True
    if(Board[0][0]=='X' and Board[1][1]=='X'and Board[2][2]=='X'):
        return True
    if(Board[0][2]=='X'and Board[1][1]=='X' and Board[2][0]=='X'):
        return True
    return False

def Draw_Game(Board):
    for i in range(3):
        for j in range(Side):
            if(Board[i][j]=='-'):
                return False
    return True

def StartUser():
    Board=CreateBoard()
    print(Board)
    for moves in range(Side*Side):
        if(moves%2==1):
            computer = int(Best_Move(Board))
            x=int((computer - 1) / Side)
            y=int((computer - 1) % Side)
            Board[x][y] = "X"
            show_Board(Board)
        else:
            user = int(input("Enter the cell"))
            x = int((user - 1) / Side)
            y = int((user - 1) % Side)
            Board[x][y] = "O"
            show_Board(Board)
        if (Success_Game(Board)):
            print("You win")
            return

        elif(Lose_Game(Board)):
            print("You lose")
            return
        elif(Draw_Game(Board)):
            print("Game draw!")
            return


def Min_Max(Board,depth,turn):
    global count
    if(Success_Game(Board)):
        return 1
    if(Lose_Game(Board)):
        return -1
    if(Draw_Game(Board)):
        return 0
    if (turn=="2"):
        best =-10
        for i in range(Side):
            for j in range(Side):
                if (Board[i][j]=='-'):
                    TempoararyBoard = copy.deepcopy(Board)
                    TempoararyBoard[i][j]="O"
                    count = count + 1
                    best = max(best, Min_Max(TempoararyBoard,depth,"1"))
                    #for i in range(Side):
                         #print(Board[i])
        print(count)
        #print("\n")
        return best

    elif(turn=="1"):
        best=10
        for i in range(Side):
            for j in range(Side):
                if(Board[i][j]=="-"):
                    TempoararyBoard=copy.deepcopy(Board)
                    TempoararyBoard[i][j] = "X"
                    count=count+1
                    best=min(best,Min_Max( TempoararyBoard,depth,"2"))
                    #for i in range(Side):
                            # print(Board[i])
        #print("\n")
        print(count)
        return best



def Best_Move(Board):
    Combest=1
    Comlevel=0
    depth=0
    for i in range(Side):
        for j in range(Side):
            depth=depth+1
            if (Board[i][j] =='-') :
                TemporaryBoard=copy.deepcopy(Board)
                TemporaryBoard[i][j]='X'
                move=(Min_Max(TemporaryBoard,depth,"2"))
                if(Combest>move):
                    Combest=move
                    Comlevel=depth
    return Comlevel
Side=3
Board=[]
Start=time.time()
StartUser()
End = time.time()
print(End - Start)
print(count)