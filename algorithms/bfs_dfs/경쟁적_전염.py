from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, k, x, y, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    graph[nx][ny] = k
                    visited[nx][ny] = True


visited = [[False] * n for _ in range(n)]
for i in range(1, s + 1):
    for j in range(1, k + 1):
        for l in range(n):
            for m in range(n):
                if graph[l][m] == j and not visited[l][m]:
                    bfs(graph, j, l, m, visited)

print(graph[x - 1][y - 1])
