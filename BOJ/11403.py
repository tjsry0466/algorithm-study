# https://www.acmicpc.net/problem/11403

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dist = graph[:]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] == 1 and dist[k][j] == 1:
                dist[i][j] = 1

for i in dist:
    print(" ".join(map(str, i)))
