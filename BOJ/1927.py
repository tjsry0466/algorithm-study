# https://www.acmicpc.net/problem/1927

# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 출력한다.

# 첫째줄에 연산의 개수 N
# 다음 N개의 줄에는 연산에 대한 정보 x
# x가 자연수라면 배열에 x추가, x가 0이라면 배열에서 가장 작은 값을 출력하고 배열에서 제거

import heapq
import sys

input = sys.stdin.readline

N = int(input())

hq = []
for i in range(N):
    x = int(input())
    if x == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, x)
