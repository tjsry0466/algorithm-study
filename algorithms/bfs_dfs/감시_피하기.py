# 임의의 세곳에 장애물을 놓는다.
# 한명의 선생님이라도 학생들을 발견한다면 NO를 반환한다.
# 모든 학생들이 선생님의 감시를 피한다면 YES를 반환한다.

from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().split()))


t_positions = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "T":
            t_positions.append((i, j))

wall_positions = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            wall_positions.append((i, j))

# T의 행/열 수집
t_rows = {x for x, y in t_positions}
t_cols = {y for x, y in t_positions}

# T의 행/열에 포함되는 X만 후보로
wall_candidates = [(i, j) for (i, j) in wall_positions if i in t_rows or j in t_cols]

# 벽 2개만 조합
wall_combinations = list(combinations(wall_candidates, 3))


def bfs(graph, x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "X":
                queue.append((nx, ny))
                # graph[nx][ny] = "T"
                if graph[nx][ny] == "S":
                    return False


for wall_combination in wall_combinations:
    for wall_position in wall_combination:
        graph[wall_position[0]][wall_position[1]] = "O"

    for t_position in t_positions:
        result = bfs(graph, t_position[0], t_position[1])
        if not result:
            print("NO")
            exit()

print("YES")

# --------------------------------
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().split()))


t_positions = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "T":
            t_positions.append((i, j))

wall_positions = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            wall_positions.append((i, j))

# T의 행/열 수집
t_rows = {x for x, y in t_positions}
t_cols = {y for x, y in t_positions}

# T의 행/열에 포함되는 X만 후보로
wall_candidates = [(i, j) for (i, j) in wall_positions if i in t_rows or j in t_cols]


# 벽 조합은 즉시 순회하여 메모리 사용 최소화
def safe_from_teacher(graph, x, y):
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if graph[nx][ny] == "O":
                break
            if graph[nx][ny] == "S":
                return False
    return True


for walls in combinations(wall_candidates, 3):
    for x, y in walls:
        graph[x][y] = "O"

    ok = True
    for tx, ty in t_positions:
        if not safe_from_teacher(graph, tx, ty):
            ok = False
            break

    for x, y in walls:
        graph[x][y] = "X"

    if ok:
        print("YES")
        exit()

print("NO")
