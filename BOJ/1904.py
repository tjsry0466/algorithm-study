# https://www.acmicpc.net/problem/1904

# 타일들에는 1 혹은 00이 쓰여져 있다.
# 1이나 00을 붙여서 수열을 만들 수 있다.
# N이 주어졌을 때 지원이가 만들 수 있는 모든 경우의 수를 구하는 문제
# 경우의 수를 15746으로 나눈 나머지를 출력

# N = 1. [1]
# N = 2. [00, 11]
# N = 3. [001, 100, 111]
# N = 4. [0011, 0000, 1001, 1100, 1111]

"""
N = int(input())

def fibonacci(n):
	dp = [0] * (n)

	dp[0] = 1
	dp[1] = 2

	for i in range(2, n):
		dp[i] = dp[i-1] + dp[i - 2]

	return dp[n - 1]

# print(dp)
print(fibonacci(N) % 15746)
"""

# 위 풀이는 공간복잡도를 초과해 아래와 같이 풀이

N = int(input())

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, (a + b) % 15746

    return b

print(fibonacci(N))
