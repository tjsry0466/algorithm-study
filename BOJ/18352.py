import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 입력 처리
N, M, K, X = map(int, input().split())

# 그래프 생성
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS 초기화
distances = [-1] * (N + 1)  # 도시의 방문 여부 및 거리를 저장 (-1: 미방문)
distances[X] = 0  # 출발 도시는 거리가 0
queue = deque([X])  # BFS 탐색을 위한 큐 초기화

# BFS 탐색
while queue:
    current = queue.popleft()

    # 현재 도시에서 인접한 도시를 확인
    for neighbor in graph[current]:
        if distances[neighbor] == -1:  # 아직 방문하지 않은 도시
            distances[neighbor] = distances[current] + 1
            queue.append(neighbor)

# 최단 거리가 K인 도시들 추출
result = [i for i in range(1, N + 1) if distances[i] == K]

# 결과 출력
if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
