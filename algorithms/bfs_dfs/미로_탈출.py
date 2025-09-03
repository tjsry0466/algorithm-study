from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]
result = 999999


def bfs(graph, visited, x, y):
    global result

    visited[x][y] = True
    queue = deque([(x, y, 1)])
    while queue:
        x, y, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny, count + 1))
                    visited[nx][ny] = True

                    if nx == n - 1 and ny == m - 1:
                        result = min(result, count + 1)
                        return


bfs(graph, visited, 0, 0)

print(result)
