# https://www.acmicpc.net/problem/11047

# 동전은 총 N종류
# 동전을 적절히 사용해 가치의 합을 K로 만들려고 함.
# 필요한 동전 개수의 최솟값을 구하는 프로그램 작성

# 동전의 종류는 10개, 가치의 합은 최대 1억
# A1이 1이고, i >= 2인 경우에 Ai는 Ai-1의 배수이므로
# 항상 가치의 합을 초과하기 전까지 가장 비싼 동전을 사용하면 됨
# 특정 동전으로 나누었을때 몫이 1이상이면 몫만큼 사용.

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

answer = 0

for coin in coins:
    mok = K // coin
    if mok:
        answer += mok
        K -= coin * mok

print(answer)
