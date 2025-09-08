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

import copy

# --------------------------------
import sys
from collections import deque
from itertools import combinations

# 입력 및 초기 설정은 동일

# 빈칸 위치 미리 저장
empty_spaces = []
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:
            empty_spaces.append((r, c))

max_safe_area = 0

# 빈칸 3개를 선택하는 모든 조합에 대해 반복
for walls in combinations(empty_spaces, 3):
    temp_graph = copy.deepcopy(graph)

    # 선택된 3개의 위치에 벽 세우기
    for r, c in walls:
        temp_graph[r][c] = 1

    # BFS를 이용한 바이러스 전파 시뮬레이션
    queue = deque(viruses)
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and temp_graph[nr][nc] == 0:
                temp_graph[nr][nc] = 2
                queue.append((nr, nc))

    # 안전 영역 계산 및 최댓값 갱신
    safe_area = sum(row.count(0) for row in temp_graph)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
