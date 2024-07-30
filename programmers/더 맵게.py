# 모든 음식의 스코빌 지수를 K 이상으로 만들기
# 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 섞음
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# 모든 음식을 스코빌 지수가 K이상이 될 때까지 반복해서 섞음.
# 모든 음식의 스코빌 지수를 K이상으로 만들기 위해 섞어야 하는 최소 횟수를 리턴
# 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우에는 -1을 리턴

import heapq


def solution(scoville, K):
    hq = []
    
    answer = 0
    for i in scoville:
        heapq.heappush(hq, i)
    
    while len(hq) > 1:
        first = heapq.heappop(hq)
        if (first >= K):
            return answer        
        second = heapq.heappop(hq)
        heapq.heappush(hq, first + (second*2))
        answer +=1
    
    first = heapq.heappop(hq)
    if (first > K):
        return answer
    
    return -1