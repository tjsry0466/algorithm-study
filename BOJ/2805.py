# https://www.acmicpc.net/problem/2805

# 나무를 일정 위치에서 잘랐을때 남은 크기를 가져간다.
# 나무를 필요한 만큼만 잘라서 집으로 가져가려고 한다.
# 적어도 M미터를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 문제

# 이분탐색 활용
# count >= M
#   result = count
# 	start = mid + 1
# else
#   end = mid - 1

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)
result = 0
while start <= end:
	mid = (start+end) // 2

	count = sum(i - mid for i in arr if i > mid)
	if count >= M:
		result = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)