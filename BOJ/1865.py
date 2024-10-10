# https://www.acmicpc.net/problem/1865

import sys

input = sys.stdin.readline

mii = lambda: map(int, input().split())

# 거리가 무한대라는 것은 단절되어 있다는 것을 뜻함.
# 음의 사이클이 있는지 확인하기 위해서 임의의 큰 수(1e9 사용)
INF = 1e9


def bellman_ford():
    time = [INF] * (N + 1)
    time[1] = 0

    for i in range(N):
        for s, e, t in arr:
            next_time = time[s] + t
            if next_time < time[e]:
                time[e] = next_time
                # 벨만 포드 알고리즘은 모든 간선을 최대 N-1번 반복해서 탐색
                # N번째 반복에서 여전히 업데이트가 발생하면, 이는 음의 사이클이 존재한다는 의미
                if i == N - 1:
                    return True
    return False


T = int(input())

for _ in range(T):
    N, M, W = mii()

    arr = []
    for _ in range(M):
        s, e, t = mii()
        arr.append((s, e, t))
        arr.append((e, s, t))

    for _ in range(W):
        s, e, t = mii()
        arr.append((s, e, -t))  # 웜홀은 가중치가 -인 간선으로 처리

    if bellman_ford():
        print("YES")
    else:
        print("NO")
