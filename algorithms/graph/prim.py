import heapq


def prim(graph, start):
    """
    Prim 알고리즘으로 최소 신장 트리를 구하는 함수.

    graph: 인접 리스트로 표현된 그래프 (정점과 간선 가중치 정보)
    start: 시작 정점
    """
    # MST에 포함된 간선들을 저장할 리스트
    mst = []
    # 이미 방문한 정점을 기록할 리스트
    visited = [False] * len(graph)
    # 최소 신장 트리의 총 가중치
    total_weight = 0
    # 우선순위 큐 (heapq는 기본적으로 최소 힙을 사용)
    pq = [(0, start)]  # (간선 가중치, 시작 정점)

    while pq:
        weight, u = heapq.heappop(pq)  # 가중치가 가장 작은 간선 선택

        # 이미 방문한 정점은 무시
        if visited[u]:
            continue

        # 정점 방문 처리
        visited[u] = True
        total_weight += weight  # 간선 가중치를 더함

        # 간선(u, v) 추가 (시작 간선은 제외)
        if weight != 0:
            mst.append((u, weight))

        # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return mst, total_weight


# 예제 사용법
if __name__ == "__main__":
    # 인접 리스트로 그래프 정의
    # 정점 i에 연결된 간선들: (목적 정점, 가중치)
    graph = {
        0: [(1, 1), (2, 2)],
        1: [(0, 1), (2, 3), (3, 4)],
        2: [(0, 2), (1, 3), (3, 5), (4, 6)],
        3: [(1, 4), (2, 5), (4, 7)],
        4: [(2, 6), (3, 7)],
    }

    start_vertex = 0
    mst, total_weight = prim(graph, start_vertex)

    print("MST에 포함된 간선:")
    for u, weight in mst:
        print(f"정점 {u}에 연결된 간선 (가중치: {weight})")
    print(f"최소 신장 트리의 총 가중치: {total_weight}")
