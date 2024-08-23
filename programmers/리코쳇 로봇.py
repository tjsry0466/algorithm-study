# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

def solution(board):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    row = len(board)
    column = len(board[0])
    
    queue = deque()
    visited = [[False] * column for _ in range(row)]
    
    for i in range(row):
        for j in range(column):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = True
                break
    

    while queue:
        x, y, steps = queue.popleft()
        
        if board[x][y] == 'G':
            return steps
        
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                
                if not (0 <= nx < row and 0 <= ny < column) or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    return -1
