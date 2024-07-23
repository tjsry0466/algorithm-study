import sys

board = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zero_index_list = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_index_list.append([i,j])
            
def row(y, v):
    for x in range(9):
        if board[y][x] == v:
            return False
    return True

def column(x, v):
    for y in range(9):
        if board[y][x] == v:
            return False
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if board[y//3 * 3 + i][x//3 * 3 + j] == n:
                return False
    return True
            
def dfs(n):
    if n == len(zero_index_list): # 빈 공간 만큼 사용했으면
        for i in board: # 출력 후
            print(*i) 
        exit() # 강제 종료

    y, x = zero_index_list[n]
    for i in range(1, 10):
        if row(y, i) and column(x, i) and square(y, x, i):
            board[y][x] = i
            dfs(n + 1)
            board[y][x] = 0
    
dfs(0)
