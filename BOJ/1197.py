# https://www.acmicpc.net/problem/1197


# Union-Find 함수 정의
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
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def kruskal(graph, n):
    # graph는 (가중치, 정점1, 정점2) 형태의 리스트로 구성

    # n은 정점의 개수
    parent = [i for i in range(n + 1)]  # 초기화: 각 정점은 자기 자신이 부모
    rank = [0] * (n + 1)  # 각 정점의 랭크 초기화

    # 간선을 가중치 순으로 정렬
    graph.sort()

    total_weight = 0  # 최소 신장 트리의 가중치 합

    for edge in graph:
        weight, u, v = edge
        # 사이클을 형성하지 않으면 간선 추가
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_weight += weight

    return total_weight


N, M = map(int, input().split())

graph = []

for i in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

mst_weight = kruskal(graph, N)

# 최소 신장 트리의 가중치 합 출력
print(mst_weight)
