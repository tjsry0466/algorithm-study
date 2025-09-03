# 0은 빈 칸, 1은 벽, 2는 바이러스
# 세곳을 골라 벽을 세우고, 바이러스가 퍼지지 않는 영역 크기의 최댓값 구하기

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))

result = 0


def spread_and_count_safe_after_walls(wall_pos1, wall_pos2, wall_pos3):
    x1, y1 = wall_pos1
    x2, y2 = wall_pos2
    x3, y3 = wall_pos3

    graph[x1][y1] = 1
    graph[x2][y2] = 1
    graph[x3][y3] = 1

    temp = [row[:] for row in graph]

    queue = deque()
    for r in range(n):
        for c in range(m):
            if temp[r][c] == 2:
                queue.append((r, c))

    while queue:
        x, y = queue.popleft()
        for dir_idx in range(4):
            nx = x + dx[dir_idx]
            ny = y + dy[dir_idx]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    safe_cells = 0
    for r in range(n):
        for c in range(m):
            if temp[r][c] == 0:
                safe_cells += 1

    graph[x1][y1] = 0
    graph[x2][y2] = 0
    graph[x3][y3] = 0

    return safe_cells


for i in range(len(empty)):
    for j in range(i + 1, len(empty)):
        for k in range(j + 1, len(empty)):
            safe = spread_and_count_safe_after_walls(empty[i], empty[j], empty[k])
            result = max(result, safe)

print(result)
