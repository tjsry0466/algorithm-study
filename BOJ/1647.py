# https://www.acmicpc.net/problem/1647

import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootY] > rank[rootX]:
            parent[rootX] = rootY
        else:
            parent[rootX] = rootY
            rank[rootY] += 1


graph = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

rank = [0] * (N + 1)
parent = [i for i in range(N + 1)]

graph.sort()

total_weight = 0

for edge in graph:
    weight, u, v = edge
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        total_weight += weight
        max_weight = weight

print(total_weight - max_weight)
