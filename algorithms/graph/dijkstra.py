import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[0] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_distance + weight

            if distances[adj] > distance:
                distances[adj] = distance
                heapq.heappush(queue, (distance, adj))

    return distances


# 예시 그래프 (딕셔너리로 표현)
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3},
    "E": {"C": 8, "D": 3},
}

# 시작 노드 'A'에서 다른 노드까지의 최단 경로 계산
start_node = "A"
shortest_paths = dijkstra(graph, start_node)

# 결과 출력
print(f"최단 경로: {shortest_paths}")
