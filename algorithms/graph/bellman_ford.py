N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 시작점에서 모든 정점까지의 거리 초기화 (무한대)
distance = [float("inf")] * (N + 1)
distance[1] = 0

# 정점 V-1번 동안 간선 완화
for _ in range(N - 1):
    for u, v, w in edges:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w

# 음수 사이클 확인
for u, v, w in edges:
    if distance[u] != float("inf") and distance[u] + w < distance[v]:
        print(-1)
        exit()

for i, dist in enumerate(distance[2:]):
    if dist == float("inf"):
        print(-1)
    else:
        print(dist)
