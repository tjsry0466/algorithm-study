# https://school.programmers.co.kr/learn/courses/30/lessons/42628#

# 이중 우선순위 큐

# l 숫자 > 큐에 주어진 숫자를 삽입
# D 1 > 큐에서 최댓값을 삭제
# D - 1 > 큐에서 최솟값을 삭제

# 모든 연산을 처리한 후 큐가 비어있으면 [0, 0] 비어있지 않으면 [최댓값, 최솟값]
# 최솟값이나 최댓값 삭제 연산에서 최댓값이나 최솟값이 둘 이상인 경우, 하나만 삭제
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시

import heapq


def solution(operations):
    
    hq = []
    max_hq = []
    
    for i in operations:
        method, num = i.split()
        if (method == 'I'):
            heapq.heappush(hq, int(num))
            heapq.heappush(max_hq, -int(num))
        elif (method == 'D' and num == '1'):
            try:
                heapq.heappop(max_hq)
                hq.pop()
            except:
                pass
                
        elif (method == 'D' and num == '-1'):
            try:
                heapq.heappop(hq)
                max_hq.pop()
            except:
                pass

    
    min = 0
    try:
        min = heapq.heappop(hq)
    except:
        return [0, 0]
    
    max = 0
    try:
        max = heapq.heappop(max_hq)
    except:
        return [min, min]
    
    return [-max, min]