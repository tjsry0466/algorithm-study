# https://www.acmicpc.net/status?user_id=tjsry0466&problem_id=14938&from_mine=1

import heapq

N, M, R = map(int, input().split())
T = list(map(int, input().split()))

result = 0
graph = {i: [] for i in range(1, N + 1)}

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(graph, start):
    distances = {node: float("inf") for node in range(1, N + 1)}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    total = 0
    for item in distances.items():
        node, distance = item

        if distance <= M:
            total += T[node - 1]

    return total


for start in graph.keys():
    distance = dijkstra(graph, start)
    result = max(distance, result)

print(result)
