# https://school.programmers.co.kr/learn/courses/30/lessons/142085

# 남은 병사 수와 단계를 패스할 수 있는 "무적권" 스킬을 이용해 얼마나 많은 단계를 넘을 수 있는지 구하는 문제
# 우선 병사로 막을 수 있는 만큼 막고 최대 힙을 이용해 값을 저장한 후에 병사가 부족해지는 순간에 최대값을 꺼내서 체력을 회복한 후에 무적권을 소모해서
# 최대 병사일때 무적권을 사용한 것과 같은 최적해를 구할 수 있다.

# 그리디 알고리즘

import heapq

def solution(n, k, enemy):
    answer = 0
    total_soldiers = n  # 남은 병사 수
    max_heap = []  # 최대 힙, 사용된 병사 수 기록

    for i in range(len(enemy)):
        total_soldiers -= enemy[i]  # 병사를 사용해 적을 막음
        heapq.heappush(max_heap, -enemy[i])  # 최대 힙에 삽입 (음수로 넣어 최대값을 쉽게 찾음)

        if total_soldiers < 0:  # 병사가 부족한 경우
            if k > 0:  # 무적권이 남아 있다면
                total_soldiers -= heapq.heappop(max_heap)  # 가장 큰 적을 무적권으로 막고 병사 회복
                k -= 1
            else:  # 무적권도 남아있지 않다면
                break  # 더 이상 막을 수 없으므로 중단

        answer += 1  # 라운드 성공적으로 막음

    return answer
