# https://school.programmers.co.kr/learn/courses/30/lessons/154540 

# 지도에는 바다와 무인도들에 대한 정보가 표시되어 있음
# 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지 나타냄
# 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬 정하기

# 접근 방법
# 2차원 배열 bfs.
# visited 2차원 배열 활용
# for문으로 각 행렬의 요소에서 시작하고, visited되지 않은곳만 돌면서 처리
# 다 돌았는데도 추가된게 없다면 [-1] 반환

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def solution(maps):
    arr = []
    
    row_count = len(maps)
    column_count = len(maps[0])
    
    def bfs(start_x, start_y, visited):
        global answer
        
        q = deque()
        q.append((start_x, start_y))
        visited[start_x][start_y] = 1
        result = 0
        result = int(maps[start_x][start_y])
        
        while len(q) > 0:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if (0 <= nx <row_count and 0 <= ny < column_count and visited[nx][ny] != 1 and maps[nx][ny] != 'X'):
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    print(int(maps[nx][ny]))
                    result += int(maps[nx][ny])
                    
        print("----")
        return result
    
    visited = [[0] * column_count for _ in range(row_count)]
    
    for i in range(row_count):
        for j in range(column_count):
            if (visited[i][j] != 1 and maps[i][j] != 'X'):
                arr.append(bfs(i, j, visited))
    
    if (len(arr) < 1):
        return [-1]
    
    arr.sort()
    return arr