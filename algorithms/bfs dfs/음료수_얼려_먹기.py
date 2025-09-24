import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visited, x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
visited = [[False] * m for _ in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(graph, visited, i, j)
            result += 1

print(result)
