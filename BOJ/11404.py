# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    A, B, C = map(int, input().split())
    distance = min(graph[A][B], C)
    graph[A][B] = distance

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for row in graph[1:]:
    row = list(map(lambda x: 0 if x == float("inf") else x, row))
    print(" ".join(map(str, row[1:])))
