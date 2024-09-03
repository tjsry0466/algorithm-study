# https://school.programmers.co.kr/learn/courses/30/lessons/43105

# 각 칸중 가장 합이 큰 숫자를 구하는 문제
# 제일 앞은 인덱스가 같은것만.
# 제일 마지막은 i-1만
# 그 외에 가운데는 i-1과 i+1 모두


def solution(triangle):

    dp = [[0] * (i + 1) for i in range(len(triangle) + 1)]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        row = triangle[i]
        for j in range(len(row)):
            # print(i, j)
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j >= len(row) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(
                    triangle[i][j] + dp[i - 1][j - 1], triangle[i][j] + dp[i - 1][j]
                )

    return max([max(i) for i in dp])
