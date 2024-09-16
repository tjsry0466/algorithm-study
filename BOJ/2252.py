# https://www.acmicpc.net/problem/2252

from collections import defaultdict, deque


def topological_sort(N, edges):
    # 그래프 및 진입 차수 초기화
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, N + 1)}

    # 간선 추가 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # 진입 차수가 0인 노드들을 큐에 추가
    queue = deque([node for node in range(1, N + 1) if in_degree[node] == 0])
    topological_sort = []

    while queue:
        current_node = queue.popleft()
        topological_sort.append(current_node)

        # 인접 노드의 진입 차수 감소
        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1

            # 진입 차수가 0이 되면 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topological_sort


# 입력 처리
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

result = topological_sort(N, edges)
print(" ".join(map(str, result)))
