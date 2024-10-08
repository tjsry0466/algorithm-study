# https://www.acmicpc.net/problem/1654

# K개의 랜선을 만들어야 한다.

# 랜선을 모두 K개의 같은 길이로 만들고 싶음
# N개의 랜선을 잘라서 만들어야 함.
# 잘라서 남은 길이는 버려야 한다.
# 랜선의 길이는 2^31보다 작거나 같은 자연수

# 접근 방법
# 이분 탐색을 이용
# 수 하나를 정하고 랜선을 잘라서 몇개가 나오는지(몫) 구한다.
# 수 하나는 랜선의 최대 길이인것과 1 사이의 중간값으로 한다.
# 각 랜선을 구한 수로 자른 몫을 더했을 때 K 보다 크다면 start를 mid + 1로 설정한다.
# 각 랜선을 구한 수로 자른 몫을 더했을 때 K 보다 작다면 end값을 mid - 1로 설정한다.
# K와 같다면 mid값을 출력한다.

# 4 11
# 802
# 743
# 457
# 539

# 위 값을 기준으로 구해보자

# 최대값 802
# 1: start 1, end 802, mid 401 -> 2, 1, 1, 1 
# -> K = 5므로 max를 400으로 설정
# 2: start: 1, end: 401, mid: 200 -> 4, 3, 2, 2
# -> K = 11이므로 mid의 값인 200이 정답

import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)
mid = end // 2

result = 0
while start <= end:
	mid = (start+end) // 2
	count = sum(i // mid for i in arr)

	if count >= N:
		result = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)