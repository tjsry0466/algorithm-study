# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 모든 사람이 입국 심사를 받는데 걸리는 시간을 최소로 하기
# 입국 심사를 기다리는 사람 수 n (10억 이하)
# 각 심사관이 한 명을 심사하는데 걸리는 시간 times
# (심사관 수는 10만 이하, 심사 시간은 10억 이하)

# 첫 시작은 심사관 수만큼 바로 시작할 수 있음.
# 특정 수가 주어지면 그 시간에 심사관 한명이 처리할 수 있는 총 인원수가 나옴.
# 지난 시간이 50이고 7에 한명씩 처리가 가능하다고 가정하면 50/7 = 7 (몫)
# 모든 요소에 대해 계산 후 n을 만족하는 결과중 최소값을 출력


def solution(n, times):
    answer = 0

    start = 1
    end = max(times) * n
    result = float("inf")
    while start <= end:
        mid = (start + end) // 2

        count = sum([mid // i for i in times])

        if count >= n:
            result = min(result, mid)

        if count >= n:
            end = mid - 1
        else:
            start = mid + 1

    return result
