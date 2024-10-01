# 무한대 값을 설정 (노드 간 연결이 없는 경우)
INF = float("inf")

# 그래프의 인접 행렬 (초기 값)
graph = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]

# 노드 개수
n = len(graph)


# 플로이드 와샬 알고리즘 적용
def floyd_warshall(graph):
    # 거리 배열 초기화
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # 모든 노드 k를 중간 노드로 사용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # i에서 j로 가는 최단 경로를 갱신
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# 결과 출력
shortest_paths = floyd_warshall(graph)

print("모든 노드 쌍 간의 최단 경로:")
for row in shortest_paths:
    print(row)
