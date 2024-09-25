# https://www.acmicpc.net/problem/5972

import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start_node = 1
distances = {node: float("inf") for node in range(N + 1)}
distances[start_node] = 0

queue = [(0, start_node)]

while queue:
    current_distance, current_node = heapq.heappop(queue)

    if current_distance > distances[current_node]:
        continue

    for neighbor, weight in graph[current_node]:
        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(queue, (distance, neighbor))

print(distances[N])
