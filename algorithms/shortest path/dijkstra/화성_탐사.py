import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    n = int(input())

    distance = [[INF] * n for _ in range(n)]
    graph = [[] for _ in range(n)]

    for i in range(n):
        arr = list(map(int, input().split()))
        graph[i] = arr

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            cost = dist + graph[nx][ny]

            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])
