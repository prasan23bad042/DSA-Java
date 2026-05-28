import sys

def solve():
    board = [sys.stdin.readline().strip() for _ in range(3)]
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            print(board[i][0])
            return

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != '.':
            print(board[0][j])
            return

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        print(board[0][0])
        return

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        print(board[0][2])
        return

    print("DRAW")

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        board = [data[idx], data[idx+1], data[idx+2]]
        idx += 3
        
        winner = None
        
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
                winner = board[i][0]
        
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] and board[0][j] != '.':
                winner = board[0][j]
                
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
            winner = board[0][0]
            
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
            winner = board[0][2]
            
        if winner:
            print(winner)
        else:
            print("DRAW")

if __name__ == '__main__':
    main()
