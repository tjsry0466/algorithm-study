# 병사 배치하기 - LIS 활용
# 전투력이 감소하는 순서로 배치해야 하므로, 뒤집힌 배열에서 LIS를 구함

n = int(input())
arr = list(map(int, input().split()))

# 배열을 뒤집어서 LIS 문제로 변환
arr.reverse()

# dp[i] = i번째 원소를 마지막으로 하는 LIS의 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:  # 증가하는 수열
            dp[i] = max(dp[i], dp[j] + 1)

# 최대 LIS 길이 = 남을 수 있는 병사의 최대 수
max_soldiers = max(dp)

# 열외시켜야 하는 병사의 수
answer = n - max_soldiers

print(answer)

# ---
# 이진 탐색을 활용한 O(N log N) 해법
import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

lis = []
for num in arr:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(n - len(lis))
