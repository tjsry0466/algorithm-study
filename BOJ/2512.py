# https://www.acmicpc.net/problem/2512

# 정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정하는 방법을 구하는 문제

# 1. 모든 요청이 배정될 수 있는 경우엔 요청한 금액을 그대로 배정.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산해 그 이상인 예산 요청에는 모두 상한액을 배정.
#    상한액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정.

# 이분탐색 활용
# count = if 상한액 이상인 경우: 상한액 사용
# count = if 상한액 이하인 경우: 해당 값 사용

N = int(input())
arr = list(map(int,input().split()))
M = int(input())

start = 1
end = max(arr)
result = 0
while start <= end:
	mid = (start+end) // 2

	count = sum(i if mid >= i else mid for i in arr)
	# print(count, mid, M)
	if (M >= count):
		result = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)
