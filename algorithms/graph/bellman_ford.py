def bellman_ford(vertices, edges, src):
    # 시작점에서 모든 정점까지의 거리 초기화 (무한대)
    distance = [float("inf")] * vertices
    distance[src] = 0

    # 정점 V-1번 동안 간선 완화
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # 음수 사이클 확인
    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            print("음수 사이클이 존재합니다.")
            return

    # 결과 출력
    print_solution(distance)


def print_solution(distance):
    print("정점까지의 최단 거리:")
    for i, dist in enumerate(distance):
        print(f"정점 {i} : 거리 {dist}")


# 정점의 개수 (5)
vertices = 5

# 간선 리스트 (u, v, w) 형식 (출발점 u, 도착점 v, 가중치 w)
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3),
]

# 0번 정점을 시작점으로 벨만 포드 알고리즘 실행
bellman_ford(vertices, edges, 0)
