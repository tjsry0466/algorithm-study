# https://www.acmicpc.net/problem/2660

import sys

input = sys.stdin.readline

n = int(input())
graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]
dist = graph[:]

for i in range(1, n + 1):
    dist[i][i] = 0

while True:
    A, B = map(int, input().split())
    if A == -1 and B == -1:
        break
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 각 회원의 점수 계산
scores = [0] * (n + 1)
for i in range(1, n + 1):
    scores[i] = max(dist[i][1:])  # 해당 회원이 다른 회원과의 최단 거리 중 가장 큰 값

# 회장 후보 찾기
min_score = min(scores[1:])  # 최소 점수
candidates = [i for i in range(1, n + 1) if scores[i] == min_score]

# 결과 출력
print(min_score, len(candidates))
print(" ".join(map(str, candidates)))
