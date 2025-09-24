# 각 위치에 대해서 최단거리 저장
# 다 끝이 있어서 방문 여부에 상관없이 방문해도 괜찮음

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

distance = [-1] * (n + 1)
distance[x] = 0

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, distance, x):
    queue = deque([(x, 0)])

    while queue:
        v, count = queue.popleft()

        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = count + 1
                queue.append((i, count + 1))


bfs(graph, distance, x)

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)

if k not in distance:
    print(-1)
