import random,sys,time
n=[j for j in range(1,10)]
board=[' 'for i in range(9)]
print("tic-tac-toe")
print()
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move(mark):
    if mark=="X":
        number=1
        
    elif mark=="O":
        number=2
    print("Your turn player{}".format(number))
    choice1=int(input("Enter your move(1-9):"))
    if choice1>0 and choice1<=9:
        if board[choice1-1]==" ":
            board[choice1-1]=mark
        else:
            print()
            print("the space was taken...")
            print()
            player_move(mark)
    else:
        print("invalid move.... please enter again ")
        player_move(mark)
def player_moves(mark):
    n1=random.choice(n)
    print("computer turn:")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if board[n1-1]==" ":
        board[n1-1]=mark
    else:
        print("the space have been taken...")
        print()
        player_moves(mark)
def is_victory(mark):
    if(board[0]==mark and board[1]==mark and board[2]==mark)or\
      (board[3]==mark and board[4]==mark and board[5]==mark)or\
      (board[6]==mark and board[7]==mark and board[8]==mark)or\
      (board[0]==mark and board[3]==mark and board[6]==mark)or\
      (board[1]==mark and board[4]==mark and board[7]==mark)or\
      (board[2]==mark and board[5]==mark and board[8]==mark)or\
      (board[6]==mark and board[4]==mark and board[2]==mark)or\
      (board[0]==mark and board[4]==mark and board[8]==mark):
        return True
    else:
        return False
def is_draw():
    if" "not in board:
        return True
    else:
        return False
while True:
    ch=int(input("which mode do u wanna play \n1. computer vs player \n2. player vs player \n choice:"))
    if ch==1:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("player(X)wins..Congratulations")
                sys.exit()
            elif is_draw():
                print("Its a draw")
                sys.exit()
            player_moves("O")
            if is_victory("O"):
                print_board()
                print("player(O)wins..Congratulations")
                sys.exit()
            elif is_draw():
                print("Its a draw")
                sys.exit()
    elif ch==2:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("player(X)wins..Congratulations")
                sys.exit()
            elif is_draw():
                print("Its a draw")
                sys.exit()
            player_move("O")
            if is_victory("O"):
                print_board()
                print("player(O)wins..Congratulations")
                sys.exit()
            elif is_draw():
                print("Its a draw")
                sys.exit()
            else:
                print("Enter again")
    
            
            
                
      
       
    
