# 상대 팀 진영을 먼저 파괴하면 이기는 게임
# 가장 빠르게 상대방에게 도착해야함
# 길이 막혀있으면 도착 못함

# visited로 방문한 위치를 기록
# bfs로 넓이 우선 탐색

from collections import deque

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    row = len(maps)
    column = len(maps[0])
    
    visited = [[0] * column for _ in range(row)]
    visited[0][0] = 1
    
    queue = deque([(0, 0, 1)])  # x, y, distance
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == column - 1 and y == row - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < column and 0 <= ny < row and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = 1
                queue.append((nx, ny, dist + 1))
    
    return -1  # 목표 지점에 도달할 수 없는 경우
