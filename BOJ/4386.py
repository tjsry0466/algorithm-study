# https://www.acmicpc.net/problem/4386

import heapq
import math


def calculate_distance(star1, star2):
    # 두 별 간의 유클리드 거리 계산
    return math.sqrt((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2)


def minimum_cost_to_connect_stars(n, stars):
    # 최소 신장 트리에 포함된 정점 집합
    visited = [False] * n
    # 우선순위 큐 (비용, 현재 정점)
    priority_queue = [(0, 0)]  # 비용 0으로 시작 정점을 0으로 설정
    total_cost = 0
    edges_used = 0

    while priority_queue and edges_used < n:
        cost, current = heapq.heappop(priority_queue)

        # 이미 방문한 정점이면 무시
        if visited[current]:
            continue

        # 정점 방문 처리
        visited[current] = True
        total_cost += cost
        edges_used += 1

        # 현재 정점에서 연결할 수 있는 모든 정점을 우선순위 큐에 추가
        for next in range(n):
            if not visited[next]:
                distance = calculate_distance(stars[current], stars[next])
                heapq.heappush(priority_queue, (distance, next))

    return total_cost


# 입력 처리
n = int(input())  # 별의 개수
stars = [tuple(map(float, input().split())) for _ in range(n)]  # 별의 좌표 입력

# 최소 비용 계산
result = minimum_cost_to_connect_stars(n, stars)

# 결과 출력 (소수점 둘째 자리까지)
print(f"{result:.2f}")
