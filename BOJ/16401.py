# https://www.acmicpc.net/problem/16401

# 최대한 긴 과자를 나눠주는 문제
# 동일한 길이의 과자를 나눠주어야 한다.
# M명의 조카, N개의 과자가 있을때 조카 1명에게 줄 수 있는 막대 과자의 최대 길이
# 조카의 수는 최대 백만, 과자의 수도 백만

# 정답을 몇으로 해야 정답으로 각 과자들을 나눴을 때 몫이 N이 되는지 구하는 문제
# start 1, end (막대 과자의 길이의 최대값)으로 이분탐색을 반복하며 몫이 N이 될때 가장 큰 정답을 구한다.

M, N = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)
result = 0
while start <= end:
	mid = (start+end) //2

	count = sum(i//mid for i in arr)

	if (count >= M):
		result = mid
		start = mid + 1 # 이미 기준을 만족한 경우라 더 mid가 큰 값을 찾기 위해 더 큰영역을 조회할 수 있도록 start를 mid+1로 옮겨줌
	else:
		end = mid - 1

print(result)